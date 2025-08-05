//! # Handle webxdc messages.
//!
//! Internally status updates are stored in the `msgs_status_updates` SQL table.
//! `msgs_status_updates` contains the following columns:
//! - `id` - status update serial number
//! - `msg_id` - ID of the message in the `msgs` table
//! - `update_item` - JSON representation of the status update
//! - `uid` - "id" field of the update, used for deduplication
//!
//! Status updates are scheduled for sending by adding a record
//! to `smtp_status_updates_table` SQL table.
//! `smtp_status_updates` contains the following columns:
//! - `msg_id` - ID of the message in the `msgs` table
//! - `first_serial` - serial number of the first status update to send
//! - `last_serial` - serial number of the last status update to send
//! - `descr` - text to send along with the updates

mod integration;
mod maps_integration;

use std::path::Path;

use anyhow::{anyhow, bail, ensure, format_err, Context as _, Result};

use deltachat_contact_tools::strip_rtlo_characters;
use deltachat_derive::FromSql;
use lettre_email::PartBuilder;
use rusqlite::OptionalExtension;
use serde::{Deserialize, Serialize};
use serde_json::Value;
use tokio::io::AsyncReadExt;

use crate::chat::{self, Chat};
use crate::constants::Chattype;
use crate::contact::ContactId;
use crate::context::Context;
use crate::events::EventType;
use crate::message::{Message, MessageState, MsgId, Viewtype};
use crate::mimefactory::wrapped_base64_encode;
use crate::mimeparser::SystemMessage;
use crate::param::Param;
use crate::param::Params;
use crate::tools::create_id;
use crate::tools::{create_smeared_timestamp, get_abs_path};

/// The current API version.
/// If `min_api` in manifest.toml is set to a larger value,
/// the Webxdc's index.html is replaced by an error message.
/// In the future, that may be useful to avoid new Webxdc being loaded on old Delta Chats.
const WEBXDC_API_VERSION: u32 = 1;

/// Suffix used to recognize webxdc files.
pub const WEBXDC_SUFFIX: &str = "xdc";
const WEBXDC_DEFAULT_ICON: &str = "__webxdc__/default-icon.png";

/// Raw information read from manifest.toml
#[derive(Debug, Deserialize, Default)]
#[non_exhaustive]
pub struct WebxdcManifest {
    /// Webxdc name, used on icons or page titles.
    pub name: Option<String>,

    /// Minimum API version required to run this webxdc.
    pub min_api: Option<u32>,

    /// Optional URL of webxdc source code.
    pub source_code_url: Option<String>,

    /// If the webxdc requests network access.
    pub request_internet_access: Option<bool>,
}

/// Parsed information from WebxdcManifest and fallbacks.
#[derive(Debug, Serialize)]
pub struct WebxdcInfo {
    /// The name of the app.
    /// Defaults to filename if not set in the manifest.
    pub name: String,

    /// Filename of the app icon.
    pub icon: String,

    /// If the webxdc represents a document and allows to edit it,
    /// this is the document name.
    /// Otherwise an empty string.
    pub document: String,

    /// Short description of the webxdc state.
    /// For example, "7 votes".
    pub summary: String,

    /// URL of webxdc source code or an empty string.
    pub source_code_url: String,

    /// If the webxdc is allowed to access the network.
    /// It should request access, be encrypted
    /// and sent to self for this.
    pub internet_access: bool,
}

/// Status Update ID.
#[derive(
    Debug,
    Copy,
    Clone,
    Default,
    PartialEq,
    Eq,
    Hash,
    PartialOrd,
    Ord,
    Serialize,
    Deserialize,
    FromSql,
    FromPrimitive,
)]
pub struct StatusUpdateSerial(u32);

impl StatusUpdateSerial {
    /// Create a new [StatusUpdateSerial].
    pub fn new(id: u32) -> StatusUpdateSerial {
        StatusUpdateSerial(id)
    }

    /// Gets StatusUpdateSerial as untyped integer.
    /// Avoid using this outside ffi.
    pub fn to_u32(self) -> u32 {
        self.0
    }
}

impl rusqlite::types::ToSql for StatusUpdateSerial {
    fn to_sql(&self) -> rusqlite::Result<rusqlite::types::ToSqlOutput> {
        let val = rusqlite::types::Value::Integer(i64::from(self.0));
        let out = rusqlite::types::ToSqlOutput::Owned(val);
        Ok(out)
    }
}

// Array of update items as sent on the wire.
#[derive(Debug, Deserialize)]
struct StatusUpdates {
    updates: Vec<StatusUpdateItem>,
}

/// Update items as sent on the wire and as stored in the database.
#[derive(Debug, Serialize, Deserialize, Default)]
pub struct StatusUpdateItem {
    /// The playload of the status update.
    pub payload: Value,

    /// Optional short info message that will be displayed in the chat.
    /// For example "Alice added an item" or "Bob voted for option x".
    #[serde(skip_serializing_if = "Option::is_none")]
    pub info: Option<String>,

    /// The new name of the editing document.
    /// This is not needed if the webxdc doesn't edit documents.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub document: Option<String>,

    /// Optional summary of the status update which will be shown next to the
    /// app icon. This should be short and can be something like "8 votes"
    /// for a voting app.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub summary: Option<String>,

    /// Unique ID for deduplication.
    /// This can be used if the message is sent over multiple transports.
    ///
    /// If there is no ID, message is always considered to be unique.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub uid: Option<String>,
}

/// Update items as passed to the UIs.
#[derive(Debug, Serialize, Deserialize)]
pub(crate) struct StatusUpdateItemAndSerial {
    #[serde(flatten)]
    item: StatusUpdateItem,

    serial: StatusUpdateSerial,
    max_serial: StatusUpdateSerial,
}

/// Returns an entry index and a reference.
fn find_zip_entry<'a>(
    file: &'a async_zip::ZipFile,
    name: &str,
) -> Option<(usize, &'a async_zip::StoredZipEntry)> {
    for (i, ent) in file.entries().iter().enumerate() {
        if ent.entry().filename() == name {
            return Some((i, ent));
        }
    }
    None
}

impl Context {
    /// check if a file is an acceptable webxdc for sending or receiving.
    pub(crate) async fn is_webxdc_file(&self, filename: &str, file: &[u8]) -> Result<bool> {
        if !filename.ends_with(WEBXDC_SUFFIX) {
            return Ok(false);
        }

        let archive = match async_zip::read::mem::ZipFileReader::new(file.to_vec()).await {
            Ok(archive) => archive,
            Err(_) => {
                info!(self, "{} cannot be opened as zip-file", &filename);
                return Ok(false);
            }
        };

        if find_zip_entry(archive.file(), "index.html").is_none() {
            info!(self, "{} misses index.html", &filename);
            return Ok(false);
        }

        Ok(true)
    }

    /// Ensure that a file is an acceptable webxdc for sending.
    pub(crate) async fn ensure_sendable_webxdc_file(&self, path: &Path) -> Result<()> {
        let filename = path.to_str().unwrap_or_default();
        if !filename.ends_with(WEBXDC_SUFFIX) {
            bail!("{} is not a valid webxdc file", filename);
        }

        let valid = match async_zip::read::fs::ZipFileReader::new(path).await {
            Ok(archive) => {
                if find_zip_entry(archive.file(), "index.html").is_none() {
                    warn!(self, "{} misses index.html", filename);
                    false
                } else {
                    true
                }
            }
            Err(_) => {
                warn!(self, "{} cannot be opened as zip-file", filename);
                false
            }
        };

        if !valid {
            bail!("{} is not a valid webxdc file", filename);
        }

        Ok(())
    }

    /// Check if the last message of a chat is an info message belonging to the given instance and sender.
    /// If so, the id of this message is returned.
    async fn get_overwritable_info_msg_id(
        &self,
        instance: &Message,
        from_id: ContactId,
    ) -> Result<Option<MsgId>> {
        if let Some((last_msg_id, last_from_id, last_param, last_in_repl_to)) = self
            .sql
            .query_row_optional(
                r#"SELECT id, from_id, param, mime_in_reply_to
                    FROM msgs
                    WHERE chat_id=?1 AND hidden=0
                    ORDER BY timestamp DESC, id DESC LIMIT 1"#,
                (instance.chat_id,),
                |row| {
                    let last_msg_id: MsgId = row.get(0)?;
                    let last_from_id: ContactId = row.get(1)?;
                    let last_param: Params = row.get::<_, String>(2)?.parse().unwrap_or_default();
                    let last_in_repl_to: String = row.get(3)?;
                    Ok((last_msg_id, last_from_id, last_param, last_in_repl_to))
                },
            )
            .await?
        {
            if last_from_id == from_id
                && last_param.get_cmd() == SystemMessage::WebxdcInfoMessage
                && last_in_repl_to == instance.rfc724_mid
            {
                return Ok(Some(last_msg_id));
            }
        }
        Ok(None)
    }

    /// Takes an update-json as `{payload: PAYLOAD}`
    /// writes it to the database and handles events, info-messages, document name and summary.
    async fn create_status_update_record(
        &self,
        instance: &Message,
        status_update_item: StatusUpdateItem,
        timestamp: i64,
        can_info_msg: bool,
        from_id: ContactId,
    ) -> Result<Option<StatusUpdateSerial>> {
        let Some(status_update_serial) = self
            .write_status_update_inner(&instance.id, &status_update_item, timestamp)
            .await?
        else {
            return Ok(None);
        };

        if can_info_msg {
            if let Some(ref info) = status_update_item.info {
                if let Some(info_msg_id) =
                    self.get_overwritable_info_msg_id(instance, from_id).await?
                {
                    chat::update_msg_text_and_timestamp(
                        self,
                        instance.chat_id,
                        info_msg_id,
                        info.as_str(),
                        timestamp,
                    )
                    .await?;
                } else {
                    chat::add_info_msg_with_cmd(
                        self,
                        instance.chat_id,
                        info.as_str(),
                        SystemMessage::WebxdcInfoMessage,
                        timestamp,
                        None,
                        Some(instance),
                        Some(from_id),
                    )
                    .await?;
                }
            }
        }

        let mut param_changed = false;

        let mut instance = instance.clone();
        if let Some(ref document) = status_update_item.document {
            if instance
                .param
                .update_timestamp(Param::WebxdcDocumentTimestamp, timestamp)?
            {
                instance.param.set(Param::WebxdcDocument, document);
                param_changed = true;
            }
        }

        if let Some(ref summary) = status_update_item.summary {
            if instance
                .param
                .update_timestamp(Param::WebxdcSummaryTimestamp, timestamp)?
            {
                instance
                    .param
                    .set(Param::WebxdcSummary, strip_rtlo_characters(summary));
                param_changed = true;
            }
        }

        if param_changed {
            instance.update_param(self).await?;
            self.emit_msgs_changed(instance.chat_id, instance.id);
        }

        if instance.viewtype == Viewtype::Webxdc {
            self.emit_event(EventType::WebxdcStatusUpdate {
                msg_id: instance.id,
                status_update_serial,
            });
        }

        Ok(Some(status_update_serial))
    }

    /// Inserts a status update item into `msgs_status_updates` table.
    ///
    /// Returns serial ID of the status update if a new item is inserted.
    pub(crate) async fn write_status_update_inner(
        &self,
        instance_id: &MsgId,
        status_update_item: &StatusUpdateItem,
        timestamp: i64,
    ) -> Result<Option<StatusUpdateSerial>> {
        let uid = status_update_item.uid.as_deref();
        let status_update_item = serde_json::to_string(&status_update_item)?;
        let trans_fn = |t: &mut rusqlite::Transaction| {
            t.execute(
                "UPDATE msgs SET timestamp_rcvd=? WHERE id=?",
                (timestamp, instance_id),
            )?;
            let rowid = t
                .query_row(
                    "INSERT INTO msgs_status_updates (msg_id, update_item, uid) VALUES(?, ?, ?)
                     ON CONFLICT (uid) DO NOTHING
                     RETURNING id",
                    (instance_id, status_update_item, uid),
                    |row| {
                        let id: u32 = row.get(0)?;
                        Ok(id)
                    },
                )
                .optional()?;
            Ok(rowid)
        };
        let Some(rowid) = self.sql.transaction(trans_fn).await? else {
            let uid = uid.unwrap_or("-");
            info!(self, "Ignoring duplicate status update with uid={uid}");
            return Ok(None);
        };
        let status_update_serial = StatusUpdateSerial(rowid);
        Ok(Some(status_update_serial))
    }

    /// Returns the update_item with `status_update_serial` from the webxdc with message id `msg_id`.
    pub async fn get_status_update(
        &self,
        msg_id: MsgId,
        status_update_serial: StatusUpdateSerial,
    ) -> Result<String> {
        self.sql
            .query_get_value(
                "SELECT update_item FROM msgs_status_updates WHERE id=? AND msg_id=? ",
                (status_update_serial.0, msg_id),
            )
            .await?
            .context("get_status_update: no update item found.")
    }

    /// Sends a status update for an webxdc instance.
    ///
    /// If the instance is a draft,
    /// the status update is sent once the instance is actually sent.
    /// Otherwise, the update is sent as soon as possible.
    pub async fn send_webxdc_status_update(
        &self,
        instance_msg_id: MsgId,
        update_str: &str,
        descr: &str,
    ) -> Result<()> {
        let status_update_item: StatusUpdateItem = serde_json::from_str(update_str)
            .with_context(|| format!("Failed to parse webxdc update item from {update_str:?}"))?;
        self.send_webxdc_status_update_struct(instance_msg_id, status_update_item, descr)
            .await?;
        Ok(())
    }

    /// Sends a status update for an webxdc instance.
    /// Also see [Self::send_webxdc_status_update]
    pub async fn send_webxdc_status_update_struct(
        &self,
        instance_msg_id: MsgId,
        mut status_update: StatusUpdateItem,
        descr: &str,
    ) -> Result<()> {
        let instance = Message::load_from_db(self, instance_msg_id)
            .await
            .with_context(|| {
                format!("Failed to load message {instance_msg_id} from the database")
            })?;
        let viewtype = instance.viewtype;
        if viewtype != Viewtype::Webxdc {
            bail!("send_webxdc_status_update: message {instance_msg_id} is not a webxdc message, but a {viewtype} message.");
        }

        if instance.param.get_int(Param::WebxdcIntegration).is_some() {
            return self
                .intercept_send_webxdc_status_update(instance, status_update)
                .await;
        }

        let chat_id = instance.chat_id;
        let chat = Chat::load_from_db(self, chat_id)
            .await
            .with_context(|| format!("Failed to load chat {chat_id} from the database"))?;
        if let Some(reason) = chat.why_cant_send(self).await.with_context(|| {
            format!("Failed to check if webxdc update can be sent to chat {chat_id}")
        })? {
            bail!("Cannot send to {chat_id}: {reason}.");
        }

        let send_now = !matches!(
            instance.state,
            MessageState::Undefined | MessageState::OutPreparing | MessageState::OutDraft
        );

        status_update.uid = Some(create_id());
        let status_update_serial: StatusUpdateSerial = self
            .create_status_update_record(
                &instance,
                status_update,
                create_smeared_timestamp(self),
                send_now,
                ContactId::SELF,
            )
            .await
            .context("Failed to create status update")?
            .context("Duplicate status update UID was generated")?;

        if send_now {
            self.sql.insert(
                "INSERT INTO smtp_status_updates (msg_id, first_serial, last_serial, descr) VALUES(?, ?, ?, ?)
                 ON CONFLICT(msg_id)
                 DO UPDATE SET last_serial=excluded.last_serial, descr=excluded.descr",
                (instance.id, status_update_serial, status_update_serial, descr),
            ).await.context("Failed to insert webxdc update into SMTP queue")?;
            self.scheduler.interrupt_smtp().await;
        }
        Ok(())
    }

    /// Pops one record of queued webxdc status updates.
    /// This function exists to make the sqlite statement testable.
    async fn pop_smtp_status_update(
        &self,
    ) -> Result<Option<(MsgId, StatusUpdateSerial, StatusUpdateSerial, String)>> {
        let _lock = self.sql.write_lock().await;
        let res = self
            .sql
            .query_row_optional(
                "DELETE FROM smtp_status_updates
                     WHERE msg_id IN (SELECT msg_id FROM smtp_status_updates LIMIT 1)
                     RETURNING msg_id, first_serial, last_serial, descr",
                (),
                |row| {
                    let instance_id: MsgId = row.get(0)?;
                    let first_serial: StatusUpdateSerial = row.get(1)?;
                    let last_serial: StatusUpdateSerial = row.get(2)?;
                    let descr: String = row.get(3)?;
                    Ok((instance_id, first_serial, last_serial, descr))
                },
            )
            .await?;
        Ok(res)
    }

    /// Attempts to send queued webxdc status updates.
    pub(crate) async fn flush_status_updates(&self) -> Result<()> {
        loop {
            let (instance_id, first_serial, last_serial, descr) =
                match self.pop_smtp_status_update().await? {
                    Some(res) => res,
                    None => return Ok(()),
                };

            if let Some(json) = self
                .render_webxdc_status_update_object(instance_id, Some((first_serial, last_serial)))
                .await?
            {
                let instance = Message::load_from_db(self, instance_id).await?;
                let mut status_update = Message {
                    chat_id: instance.chat_id,
                    viewtype: Viewtype::Text,
                    text: descr.to_string(),
                    hidden: true,
                    ..Default::default()
                };
                status_update
                    .param
                    .set_cmd(SystemMessage::WebxdcStatusUpdate);
                status_update.param.set(Param::Arg, json);
                status_update.set_quote(self, Some(&instance)).await?;
                status_update.param.remove(Param::GuaranteeE2ee); // may be set by set_quote(), if #2985 is done, this line can be removed
                chat::send_msg(self, instance.chat_id, &mut status_update).await?;
            }
        }
    }

    pub(crate) fn build_status_update_part(&self, json: &str) -> PartBuilder {
        let encoded_body = wrapped_base64_encode(json.as_bytes());

        PartBuilder::new()
            .content_type(&"application/json".parse::<mime::Mime>().unwrap())
            .header((
                "Content-Disposition",
                "attachment; filename=\"status-update.json\"",
            ))
            .header(("Content-Transfer-Encoding", "base64"))
            .body(encoded_body)
    }

    /// Receives status updates from receive_imf to the database
    /// and sends out an event.
    ///
    /// `instance` is a webxdc instance.
    ///
    /// `from_id` is the sender.
    ///
    /// `timestamp` is the timestamp of the update.
    ///
    /// `json` is an array containing one or more update items as created by send_webxdc_status_update(),
    /// the array is parsed using serde, the single payloads are used as is.
    pub(crate) async fn receive_status_update(
        &self,
        from_id: ContactId,
        instance: &Message,
        timestamp: i64,
        can_info_msg: bool,
        json: &str,
    ) -> Result<()> {
        let chat_id = instance.chat_id;

        if from_id != ContactId::SELF && !chat::is_contact_in_chat(self, chat_id, from_id).await? {
            let chat_type: Chattype = self
                .sql
                .query_get_value("SELECT type FROM chats WHERE id=?", (chat_id,))
                .await?
                .with_context(|| format!("Chat type for chat {chat_id} not found"))?;
            if chat_type != Chattype::Mailinglist {
                bail!("receive_status_update: status sender {from_id} is not a member of chat {chat_id}")
            }
        }

        let updates: StatusUpdates = serde_json::from_str(json)?;
        for update_item in updates.updates {
            self.create_status_update_record(
                instance,
                update_item,
                timestamp,
                can_info_msg,
                from_id,
            )
            .await?;
        }

        Ok(())
    }

    /// Returns status updates as an JSON-array, ready to be consumed by a webxdc.
    ///
    /// Example: `[{"serial":1, "max_serial":3, "payload":"any update data"},
    ///            {"serial":3, "max_serial":3, "payload":"another update data"}]`
    /// Updates with serials larger than `last_known_serial` are returned.
    /// If no last serial is known, set `last_known_serial` to 0.
    /// If no updates are available, an empty JSON-array is returned.
    pub async fn get_webxdc_status_updates(
        &self,
        instance_msg_id: MsgId,
        last_known_serial: StatusUpdateSerial,
    ) -> Result<String> {
        let param = instance_msg_id.get_param(self).await?;
        if param.get_int(Param::WebxdcIntegration).is_some() {
            let instance = Message::load_from_db(self, instance_msg_id).await?;
            return self
                .intercept_get_webxdc_status_updates(instance, last_known_serial)
                .await;
        }

        let json = self
            .sql
            .query_map(
                "SELECT update_item, id FROM msgs_status_updates WHERE msg_id=? AND id>? ORDER BY id",
                (instance_msg_id, last_known_serial),
                |row| {
                    let update_item_str = row.get::<_, String>(0)?;
                    let serial = row.get::<_, StatusUpdateSerial>(1)?;
                    Ok((update_item_str, serial))
                },
                |rows| {
                    let mut rows_copy : Vec<(String, StatusUpdateSerial)> = Vec::new(); // `rows_copy` needed as `rows` cannot be iterated twice.
                    let mut max_serial = StatusUpdateSerial(0);
                    for row in rows {
                        let row = row?;
                        if row.1 > max_serial {
                            max_serial = row.1;
                        }
                        rows_copy.push(row);
                    }

                    let mut json = String::default();
                    for row in rows_copy {
                        let (update_item_str, serial) = row;
                        let update_item = StatusUpdateItemAndSerial
                        {
                            item: StatusUpdateItem {
                                uid: None, // Erase UIDs, apps, bots and tests don't need to know them.
                                ..serde_json::from_str(&update_item_str)?
                            },
                            serial,
                            max_serial,
                        };

                        if !json.is_empty() {
                            json.push_str(",\n");
                        }
                        json.push_str(&serde_json::to_string(&update_item)?);
                    }
                    Ok(json)
                },
            )
            .await?;
        Ok(format!("[{json}]"))
    }

    /// Renders JSON-object for status updates as used on the wire.
    ///
    /// Example: `{"updates": [{"payload":"any update data"},
    ///                        {"payload":"another update data"}]}`
    ///
    /// `range` is an optional range of status update serials to send.
    /// If it is `None`, all updates are sent.
    /// This is used when a message is resent using [`crate::chat::resend_msgs`].
    pub(crate) async fn render_webxdc_status_update_object(
        &self,
        instance_msg_id: MsgId,
        range: Option<(StatusUpdateSerial, StatusUpdateSerial)>,
    ) -> Result<Option<String>> {
        let json = self
            .sql
            .query_map(
                "SELECT update_item FROM msgs_status_updates WHERE msg_id=? AND id>=? AND id<=? ORDER BY id",
                (
                    instance_msg_id,
                    range.map(|r|r.0).unwrap_or(StatusUpdateSerial(0)),
                    range.map(|r|r.1).unwrap_or(StatusUpdateSerial(u32::MAX)),
                ),
                |row| row.get::<_, String>(0),
                |rows| {
                    let mut json = String::default();
                    for row in rows {
                        let update_item = row?;
                        if !json.is_empty() {
                            json.push_str(",\n");
                        }
                        json.push_str(&update_item);
                    }
                    Ok(json)
                },
            )
            .await?;
        if json.is_empty() {
            Ok(None)
        } else {
            Ok(Some(format!(r#"{{"updates":[{json}]}}"#)))
        }
    }
}

fn parse_webxdc_manifest(bytes: &[u8]) -> Result<WebxdcManifest> {
    let s = std::str::from_utf8(bytes)?;
    let manifest: WebxdcManifest = toml::from_str(s)?;
    Ok(manifest)
}

async fn get_blob(archive: &async_zip::read::fs::ZipFileReader, name: &str) -> Result<Vec<u8>> {
    let (i, _) = find_zip_entry(archive.file(), name)
        .ok_or_else(|| anyhow!("no entry found for {}", name))?;
    let mut reader = archive.entry(i).await?;
    let mut buf = Vec::new();
    reader.read_to_end(&mut buf).await?;
    Ok(buf)
}

impl Message {
    /// Get handle to a webxdc ZIP-archive.
    /// To check for file existence use archive.by_name(), to read a file, use get_blob(archive).
    async fn get_webxdc_archive(
        &self,
        context: &Context,
    ) -> Result<async_zip::read::fs::ZipFileReader> {
        let path = self
            .get_file(context)
            .ok_or_else(|| format_err!("No webxdc instance file."))?;
        let path_abs = get_abs_path(context, &path);
        let archive = async_zip::read::fs::ZipFileReader::new(path_abs).await?;
        Ok(archive)
    }

    /// Return file from inside an archive.
    /// Currently, this works only if the message is an webxdc instance.
    ///
    /// `name` is the filename within the archive, e.g. `index.html`.
    pub async fn get_webxdc_blob(&self, context: &Context, name: &str) -> Result<Vec<u8>> {
        ensure!(self.viewtype == Viewtype::Webxdc, "No webxdc instance.");

        if name == WEBXDC_DEFAULT_ICON {
            return Ok(include_bytes!("../assets/icon-webxdc.png").to_vec());
        }

        // ignore first slash.
        // this way, files can be accessed absolutely (`/index.html`) as well as relatively (`index.html`)
        let name = if name.starts_with('/') {
            name.split_at(1).1
        } else {
            name
        };

        let archive = self.get_webxdc_archive(context).await?;

        if name == "index.html" {
            if let Ok(bytes) = get_blob(&archive, "manifest.toml").await {
                if let Ok(manifest) = parse_webxdc_manifest(&bytes) {
                    if let Some(min_api) = manifest.min_api {
                        if min_api > WEBXDC_API_VERSION {
                            return Ok(Vec::from(
                                "<!DOCTYPE html>This Webxdc requires a newer Delta Chat version.",
                            ));
                        }
                    }
                }
            }
        }

        get_blob(&archive, name).await
    }

    /// Return info from manifest.toml or from fallbacks.
    pub async fn get_webxdc_info(&self, context: &Context) -> Result<WebxdcInfo> {
        ensure!(self.viewtype == Viewtype::Webxdc, "No webxdc instance.");
        let archive = self.get_webxdc_archive(context).await?;

        let mut manifest = get_blob(&archive, "manifest.toml")
            .await
            .map(|bytes| parse_webxdc_manifest(&bytes).unwrap_or_default())
            .unwrap_or_default();

        if let Some(ref name) = manifest.name {
            let name = name.trim();
            if name.is_empty() {
                warn!(context, "empty name given in manifest");
                manifest.name = None;
            }
        }

        let internet_access = manifest.request_internet_access.unwrap_or_default()
            && self.chat_id.is_self_talk(context).await.unwrap_or_default()
            && self.get_showpadlock();

        Ok(WebxdcInfo {
            name: if let Some(name) = manifest.name {
                name
            } else {
                self.get_filename().unwrap_or_default()
            },
            icon: if find_zip_entry(archive.file(), "icon.png").is_some() {
                "icon.png".to_string()
            } else if find_zip_entry(archive.file(), "icon.jpg").is_some() {
                "icon.jpg".to_string()
            } else {
                WEBXDC_DEFAULT_ICON.to_string()
            },
            document: self
                .param
                .get(Param::WebxdcDocument)
                .unwrap_or_default()
                .to_string(),
            summary: if internet_access {
                "Dev Mode: Do not enter sensitive data!".to_string()
            } else {
                self.param
                    .get(Param::WebxdcSummary)
                    .unwrap_or_default()
                    .to_string()
            },
            source_code_url: if let Some(url) = manifest.source_code_url {
                url
            } else {
                "".to_string()
            },
            internet_access,
        })
    }
}
