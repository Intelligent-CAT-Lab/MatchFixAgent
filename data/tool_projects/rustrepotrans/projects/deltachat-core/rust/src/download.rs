//! # Download large messages manually.

use std::cmp::max;
use std::collections::BTreeMap;

use anyhow::{anyhow, bail, Result};
use deltachat_derive::{FromSql, ToSql};
use serde::{Deserialize, Serialize};

use crate::config::Config;
use crate::context::Context;
use crate::imap::session::Session;
use crate::message::{Message, MsgId, Viewtype};
use crate::mimeparser::{MimeMessage, Part};
use crate::tools::time;
use crate::{chatlist_events, stock_str, EventType};

/// Download limits should not be used below `MIN_DOWNLOAD_LIMIT`.
///
/// For better UX, some messages as add-member, non-delivery-reports (NDN) or read-receipts (MDN)
/// should always be downloaded completely to handle them correctly,
/// also in larger groups and if group and contact avatar are attached.
/// Most of these cases are caught by `MIN_DOWNLOAD_LIMIT`.
pub(crate) const MIN_DOWNLOAD_LIMIT: u32 = 163840;

/// If a message is downloaded only partially
/// and `delete_server_after` is set to small timeouts (eg. "at once"),
/// the user might have no chance to actually download that message.
/// `MIN_DELETE_SERVER_AFTER` increases the timeout in this case.
pub(crate) const MIN_DELETE_SERVER_AFTER: i64 = 48 * 60 * 60;

/// Download state of the message.
#[derive(
    Debug,
    Default,
    Display,
    Clone,
    Copy,
    PartialEq,
    Eq,
    FromPrimitive,
    ToPrimitive,
    FromSql,
    ToSql,
    Serialize,
    Deserialize,
)]
#[repr(u32)]
pub enum DownloadState {
    /// Message is fully downloaded.
    #[default]
    Done = 0,

    /// Message is partially downloaded and can be fully downloaded at request.
    Available = 10,

    /// Failed to fully download the message.
    Failure = 20,

    /// Undecipherable message.
    Undecipherable = 30,

    /// Full download of the message is in progress.
    InProgress = 1000,
}

impl Context {
    // Returns validated download limit or `None` for "no limit".
    pub(crate) async fn download_limit(&self) -> Result<Option<u32>> {
        let download_limit = self.get_config_int(Config::DownloadLimit).await?;
        if download_limit <= 0 {
            Ok(None)
        } else {
            Ok(Some(max(MIN_DOWNLOAD_LIMIT, download_limit as u32)))
        }
    }
}

impl MsgId {
    /// Schedules full message download for partially downloaded message.
    pub async fn download_full(self, context: &Context) -> Result<()> {
        let msg = Message::load_from_db(context, self).await?;
        match msg.download_state() {
            DownloadState::Done | DownloadState::Undecipherable => {
                return Err(anyhow!("Nothing to download."))
            }
            DownloadState::InProgress => return Err(anyhow!("Download already in progress.")),
            DownloadState::Available | DownloadState::Failure => {
                self.update_download_state(context, DownloadState::InProgress)
                    .await?;
                context
                    .sql
                    .execute("INSERT INTO download (msg_id) VALUES (?)", (self,))
                    .await?;
                context.scheduler.interrupt_inbox().await;
            }
        }
        Ok(())
    }

    pub(crate) async fn update_download_state(
        self,
        context: &Context,
        download_state: DownloadState,
    ) -> Result<()> {
        let msg = Message::load_from_db(context, self).await?;
        context
            .sql
            .execute(
                "UPDATE msgs SET download_state=? WHERE id=?;",
                (download_state, self),
            )
            .await?;
        context.emit_event(EventType::MsgsChanged {
            chat_id: msg.chat_id,
            msg_id: self,
        });
        chatlist_events::emit_chatlist_item_changed(context, msg.chat_id);
        Ok(())
    }
}

impl Message {
    /// Returns the download state of the message.
    pub fn download_state(&self) -> DownloadState {
        self.download_state
    }
}

/// Actually download a message partially downloaded before.
///
/// Most messages are downloaded automatically on fetch instead.
pub(crate) async fn download_msg(
    context: &Context,
    msg_id: MsgId,
    session: &mut Session,
) -> Result<()> {
    let msg = Message::load_from_db(context, msg_id).await?;
    let row = context
        .sql
        .query_row_optional(
            "SELECT uid, folder, uidvalidity FROM imap WHERE rfc724_mid=? AND target!=''",
            (&msg.rfc724_mid,),
            |row| {
                let server_uid: u32 = row.get(0)?;
                let server_folder: String = row.get(1)?;
                let uidvalidity: u32 = row.get(2)?;
                Ok((server_uid, server_folder, uidvalidity))
            },
        )
        .await?;

    let Some((server_uid, server_folder, uidvalidity)) = row else {
        // No IMAP record found, we don't know the UID and folder.
        return Err(anyhow!("Call download_full() again to try over."));
    };

    session
        .fetch_single_msg(
            context,
            &server_folder,
            uidvalidity,
            server_uid,
            msg.rfc724_mid.clone(),
        )
        .await?;
    Ok(())
}

impl Session {
    /// Download a single message and pipe it to receive_imf().
    ///
    /// receive_imf() is not directly aware that this is a result of a call to download_msg(),
    /// however, implicitly knows that as the existing message is flagged as being partly.
    async fn fetch_single_msg(
        &mut self,
        context: &Context,
        folder: &str,
        uidvalidity: u32,
        uid: u32,
        rfc724_mid: String,
    ) -> Result<()> {
        if uid == 0 {
            bail!("Attempt to fetch UID 0");
        }

        self.select_folder(context, Some(folder)).await?;

        // we are connected, and the folder is selected
        info!(context, "Downloading message {}/{} fully...", folder, uid);

        let mut uid_message_ids: BTreeMap<u32, String> = BTreeMap::new();
        uid_message_ids.insert(uid, rfc724_mid);
        let (last_uid, _received) = self
            .fetch_many_msgs(
                context,
                folder,
                uidvalidity,
                vec![uid],
                &uid_message_ids,
                false,
                false,
            )
            .await?;
        if last_uid.is_none() {
            bail!("Failed to fetch UID {uid}");
        }
        Ok(())
    }
}

impl MimeMessage {
    /// Creates a placeholder part and add that to `parts`.
    ///
    /// To create the placeholder, only the outermost header can be used,
    /// the mime-structure itself is not available.
    ///
    /// The placeholder part currently contains a text with size and availability of the message;
    /// in the future, we may do more advanced things as previews here.
    pub(crate) async fn create_stub_from_partial_download(
        &mut self,
        context: &Context,
        org_bytes: u32,
    ) -> Result<()> {
        let mut text = format!(
            "[{}]",
            stock_str::partial_download_msg_body(context, org_bytes).await
        );
        if let Some(delete_server_after) = context.get_config_delete_server_after().await? {
            let until = stock_str::download_availability(
                context,
                time() + max(delete_server_after, MIN_DELETE_SERVER_AFTER),
            )
            .await;
            text += format!(" [{until}]").as_str();
        };

        info!(context, "Partial download: {}", text);

        self.parts.push(Part {
            typ: Viewtype::Text,
            msg: text,
            ..Default::default()
        });

        Ok(())
    }
}

