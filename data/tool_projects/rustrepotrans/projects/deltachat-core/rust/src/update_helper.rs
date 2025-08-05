//! # Functions to update timestamps.

use anyhow::Result;

use crate::chat::ChatId;
use crate::contact::ContactId;
use crate::context::Context;
use crate::param::{Param, Params};

impl Context {
    /// Updates a contact's timestamp, if reasonable.
    /// Returns true if the caller shall update the settings belonging to the scope.
    /// (if we have a ContactId type at some point, the function should go there)
    pub(crate) async fn update_contacts_timestamp(
        &self,
        contact_id: ContactId,
        scope: Param,
        new_timestamp: i64,
    ) -> Result<bool> {
        self.sql
            .transaction(|transaction| {
                let mut param: Params = transaction.query_row(
                    "SELECT param FROM contacts WHERE id=?",
                    [contact_id],
                    |row| {
                        let param: String = row.get(0)?;
                        Ok(param.parse().unwrap_or_default())
                    },
                )?;
                let update = param.update_timestamp(scope, new_timestamp)?;
                if update {
                    transaction.execute(
                        "UPDATE contacts SET param=? WHERE id=?",
                        (param.to_string(), contact_id),
                    )?;
                }
                Ok(update)
            })
            .await
    }
}

impl ChatId {
    /// Updates a chat id's timestamp on disk, if reasonable.
    /// Returns true if the caller shall update the settings belonging to the scope.
    pub(crate) async fn update_timestamp(
        &self,
        context: &Context,
        scope: Param,
        new_timestamp: i64,
    ) -> Result<bool> {
        context
            .sql
            .transaction(|transaction| {
                let mut param: Params =
                    transaction.query_row("SELECT param FROM chats WHERE id=?", [self], |row| {
                        let param: String = row.get(0)?;
                        Ok(param.parse().unwrap_or_default())
                    })?;
                let update = param.update_timestamp(scope, new_timestamp)?;
                if update {
                    transaction.execute(
                        "UPDATE chats SET param=? WHERE id=?",
                        (param.to_string(), self),
                    )?;
                }
                Ok(update)
            })
            .await
    }
}

impl Params {
    /// Updates a param's timestamp in memory, if reasonable.
    /// Returns true if the caller shall update the settings belonging to the scope.
    pub(crate) fn update_timestamp(&mut self, scope: Param, new_timestamp: i64) -> Result<bool> {
        let old_timestamp = self.get_i64(scope).unwrap_or_default();
        if new_timestamp >= old_timestamp {
            self.set_i64(scope, new_timestamp);
            return Ok(true);
        }
        Ok(false)
    }
}
