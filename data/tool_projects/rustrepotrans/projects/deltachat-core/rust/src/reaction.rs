//! # Reactions.
//!
//! Reactions are short messages consisting of emojis sent in reply to
//! messages. Unlike normal messages which are added to the end of the chat,
//! reactions are supposed to be displayed near the original messages.
//!
//! RFC 9078 specifies how reactions are transmitted in MIME messages.
//!
//! Reaction update semantics is not well-defined in RFC 9078, so
//! Delta Chat uses the same semantics as in
//! [XEP-0444](https://xmpp.org/extensions/xep-0444.html) section
//! "3.2 Updating reactions to a message". Received reactions override
//! all previously received reactions from the same user and it is
//! possible to remove all reactions by sending an empty string as a reaction,
//! even though RFC 9078 requires at least one emoji to be sent.

use std::cmp::Ordering;
use std::collections::BTreeMap;
use std::fmt;

use anyhow::Result;

use crate::chat::{send_msg, Chat, ChatId};
use crate::chatlist_events;
use crate::contact::ContactId;
use crate::context::Context;
use crate::events::EventType;
use crate::message::{rfc724_mid_exists, Message, MsgId, Viewtype};
use crate::param::Param;

/// A single reaction consisting of multiple emoji sequences.
///
/// It is guaranteed to have all emojis sorted and deduplicated inside.
#[derive(Debug, Default, Clone)]
pub struct Reaction {
    /// Canonical representation of reaction as a string of space-separated emojis.
    reaction: String,
}

// We implement From<&str> instead of std::str::FromStr, because
// FromStr requires error type and reaction parsing never returns an
// error.
impl From<&str> for Reaction {
    /// Parses a string containing a reaction.
    ///
    /// Reaction string is separated by spaces or tabs (`WSP` in ABNF),
    /// but this function accepts any ASCII whitespace, so even a CRLF at
    /// the end of string is acceptable.
    ///
    /// Any short enough string is accepted as a reaction to avoid the
    /// complexity of validating emoji sequences as required by RFC
    /// 9078. On the sender side UI is responsible to provide only
    /// valid emoji sequences via reaction picker. On the receiver
    /// side, abuse of the possibility to use arbitrary strings as
    /// reactions is not different from other kinds of spam attacks
    /// such as sending large numbers of large messages, and should be
    /// dealt with the same way, e.g. by blocking the user.
    fn from(reaction: &str) -> Self {
        let mut emojis: Vec<&str> = reaction
            .split_ascii_whitespace()
            .filter(|&emoji| emoji.len() < 30)
            .collect();
        emojis.sort_unstable();
        emojis.dedup();
        let reaction = emojis.join(" ");
        Self { reaction }
    }
}

impl Reaction {
    /// Returns true if reaction contains no emojis.
    pub fn is_empty(&self) -> bool {
        self.reaction.is_empty()
    }

    /// Returns a vector of emojis composing a reaction.
    pub fn emojis(&self) -> Vec<&str> {
        self.reaction.split(' ').collect()
    }

    /// Returns space-separated string of emojis
    pub fn as_str(&self) -> &str {
        &self.reaction
    }

    /// Appends emojis from another reaction to this reaction.
    pub fn add(&self, other: Self) -> Self {
        let mut emojis: Vec<&str> = self.emojis();
        emojis.append(&mut other.emojis());
        emojis.sort_unstable();
        emojis.dedup();
        let reaction = emojis.join(" ");
        Self { reaction }
    }
}

/// Structure representing all reactions to a particular message.
#[derive(Debug)]
pub struct Reactions {
    /// Map from a contact to its reaction to message.
    reactions: BTreeMap<ContactId, Reaction>,
}

impl Reactions {
    /// Returns vector of contacts that reacted to the message.
    pub fn contacts(&self) -> Vec<ContactId> {
        self.reactions.keys().copied().collect()
    }

    /// Returns reaction of a given contact to message.
    ///
    /// If contact did not react to message or removed the reaction,
    /// this method returns an empty reaction.
    pub fn get(&self, contact_id: ContactId) -> Reaction {
        self.reactions.get(&contact_id).cloned().unwrap_or_default()
    }

    /// Returns true if the message has no reactions.
    pub fn is_empty(&self) -> bool {
        self.reactions.is_empty()
    }

    /// Returns a map from emojis to their frequencies.
    pub fn emoji_frequencies(&self) -> BTreeMap<String, usize> {
        let mut emoji_frequencies: BTreeMap<String, usize> = BTreeMap::new();
        for reaction in self.reactions.values() {
            for emoji in reaction.emojis() {
                emoji_frequencies
                    .entry(emoji.to_string())
                    .and_modify(|x| *x += 1)
                    .or_insert(1);
            }
        }
        emoji_frequencies
    }

    /// Returns a vector of emojis
    /// sorted in descending order of frequencies.
    ///
    /// This function can be used to display the reactions in
    /// the message bubble in the UIs.
    pub fn emoji_sorted_by_frequency(&self) -> Vec<(String, usize)> {
        let mut emoji_frequencies: Vec<(String, usize)> =
            self.emoji_frequencies().into_iter().collect();
        emoji_frequencies.sort_by(|(a, a_count), (b, b_count)| {
            match a_count.cmp(b_count).reverse() {
                Ordering::Equal => a.cmp(b),
                other => other,
            }
        });
        emoji_frequencies
    }
}

impl fmt::Display for Reactions {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let emoji_frequencies = self.emoji_sorted_by_frequency();
        let mut first = true;
        for (emoji, frequency) in emoji_frequencies {
            if !first {
                write!(f, " ")?;
            }
            first = false;
            write!(f, "{emoji}{frequency}")?;
        }
        Ok(())
    }
}

async fn set_msg_id_reaction(
    context: &Context,
    msg_id: MsgId,
    chat_id: ChatId,
    contact_id: ContactId,
    timestamp: i64,
    reaction: Reaction,
) -> Result<()> {
    if reaction.is_empty() {
        // Simply remove the record instead of setting it to empty string.
        context
            .sql
            .execute(
                "DELETE FROM reactions
                 WHERE msg_id = ?1
                 AND contact_id = ?2",
                (msg_id, contact_id),
            )
            .await?;
    } else {
        context
            .sql
            .execute(
                "INSERT INTO reactions (msg_id, contact_id, reaction)
                 VALUES (?1, ?2, ?3)
                 ON CONFLICT(msg_id, contact_id)
                 DO UPDATE SET reaction=excluded.reaction",
                (msg_id, contact_id, reaction.as_str()),
            )
            .await?;
        let mut chat = Chat::load_from_db(context, chat_id).await?;
        if chat
            .param
            .update_timestamp(Param::LastReactionTimestamp, timestamp)?
        {
            chat.param
                .set_i64(Param::LastReactionMsgId, i64::from(msg_id.to_u32()));
            chat.param
                .set_i64(Param::LastReactionContactId, i64::from(contact_id.to_u32()));
            chat.update_param(context).await?;
        }
    }

    context.emit_event(EventType::ReactionsChanged {
        chat_id,
        msg_id,
        contact_id,
    });
    chatlist_events::emit_chatlist_item_changed(context, chat_id);
    Ok(())
}

/// Sends a reaction to message `msg_id`, overriding previously sent reactions.
///
/// `reaction` is a string consisting of space-separated emoji. Use
/// empty string to retract a reaction.
pub async fn send_reaction(context: &Context, msg_id: MsgId, reaction: &str) -> Result<MsgId> {
    let msg = Message::load_from_db(context, msg_id).await?;
    let chat_id = msg.chat_id;

    let reaction: Reaction = reaction.into();
    let mut reaction_msg = Message::new(Viewtype::Text);
    reaction_msg.text = reaction.as_str().to_string();
    reaction_msg.set_reaction();
    reaction_msg.in_reply_to = Some(msg.rfc724_mid);
    reaction_msg.hidden = true;

    // Send message first.
    let reaction_msg_id = send_msg(context, chat_id, &mut reaction_msg).await?;

    // Only set reaction if we successfully sent the message.
    set_msg_id_reaction(
        context,
        msg_id,
        msg.chat_id,
        ContactId::SELF,
        reaction_msg.timestamp_sort,
        reaction,
    )
    .await?;
    Ok(reaction_msg_id)
}

/// Adds given reaction to message `msg_id` and sends an update.
///
/// This can be used to implement advanced clients that allow reacting
/// with multiple emojis. For a simple messenger UI, you probably want
/// to use [`send_reaction()`] instead so reacting with a new emoji
/// removes previous emoji at the same time.
pub async fn add_reaction(context: &Context, msg_id: MsgId, reaction: &str) -> Result<MsgId> {
    let self_reaction = get_self_reaction(context, msg_id).await?;
    let reaction = self_reaction.add(Reaction::from(reaction));
    send_reaction(context, msg_id, reaction.as_str()).await
}

/// Updates reaction of `contact_id` on the message with `in_reply_to`
/// Message-ID. If no such message is found in the database, reaction
/// is ignored.
///
/// `reaction` is a space-separated string of emojis. It can be empty
/// if contact wants to remove all reactions.
pub(crate) async fn set_msg_reaction(
    context: &Context,
    in_reply_to: &str,
    chat_id: ChatId,
    contact_id: ContactId,
    timestamp: i64,
    reaction: Reaction,
) -> Result<()> {
    if let Some((msg_id, _)) = rfc724_mid_exists(context, in_reply_to).await? {
        set_msg_id_reaction(context, msg_id, chat_id, contact_id, timestamp, reaction).await
    } else {
        info!(
            context,
            "Can't assign reaction to unknown message with Message-ID {}", in_reply_to
        );
        Ok(())
    }
}

/// Get our own reaction for a given message.
async fn get_self_reaction(context: &Context, msg_id: MsgId) -> Result<Reaction> {
    let reaction_str: Option<String> = context
        .sql
        .query_get_value(
            "SELECT reaction
             FROM reactions
             WHERE msg_id=? AND contact_id=?",
            (msg_id, ContactId::SELF),
        )
        .await?;
    Ok(reaction_str
        .as_deref()
        .map(Reaction::from)
        .unwrap_or_default())
}

/// Returns a structure containing all reactions to the message.
pub async fn get_msg_reactions(context: &Context, msg_id: MsgId) -> Result<Reactions> {
    let reactions = context
        .sql
        .query_map(
            "SELECT contact_id, reaction FROM reactions WHERE msg_id=?",
            (msg_id,),
            |row| {
                let contact_id: ContactId = row.get(0)?;
                let reaction: String = row.get(1)?;
                Ok((contact_id, reaction))
            },
            |rows| {
                let mut reactions = Vec::new();
                for row in rows {
                    let (contact_id, reaction) = row?;
                    reactions.push((contact_id, Reaction::from(reaction.as_str())));
                }
                Ok(reactions)
            },
        )
        .await?
        .into_iter()
        .collect();
    Ok(Reactions { reactions })
}

impl Chat {
    /// Check if there is a reaction newer than the given timestamp.
    ///
    /// If so, reaction details are returned and can be used to create a summary string.
    pub async fn get_last_reaction_if_newer_than(
        &self,
        context: &Context,
        timestamp: i64,
    ) -> Result<Option<(Message, ContactId, String)>> {
        if self
            .param
            .get_i64(Param::LastReactionTimestamp)
            .filter(|&reaction_timestamp| reaction_timestamp > timestamp)
            .is_none()
        {
            return Ok(None);
        };
        let reaction_msg_id = MsgId::new(
            self.param
                .get_int(Param::LastReactionMsgId)
                .unwrap_or_default() as u32,
        );
        let Some(reaction_msg) = Message::load_from_db_optional(context, reaction_msg_id).await?
        else {
            // The message reacted to may be deleted.
            // These are no errors as `Param::LastReaction*` are just weak pointers.
            // Instead, just return `Ok(None)` and let the caller create another summary.
            return Ok(None);
        };
        let reaction_contact_id = ContactId::new(
            self.param
                .get_int(Param::LastReactionContactId)
                .unwrap_or_default() as u32,
        );
        if let Some(reaction) = context
            .sql
            .query_get_value(
                "SELECT reaction FROM reactions WHERE msg_id=? AND contact_id=?",
                (reaction_msg.id, reaction_contact_id),
            )
            .await?
        {
            Ok(Some((reaction_msg, reaction_contact_id, reaction)))
        } else {
            Ok(None)
        }
    }
}
