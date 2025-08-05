//! # Maps Webxdc Integration.
//!
//! A Maps Webxdc Integration uses `sendUpdate()` and `setUpdateListener()` as usual,
//! however, it agrees with the core on the following update format:
//!
//! ## Setting POIs via `sendUpdate()`
//!
//! ```json
//! payload: {
//!     action: "pos",
//!     lat:    53.550556,
//!     lng:    9.993333,
//!     label:  "my poi"
//! }
//! ```
//!
//! Just sent POI are received via `setUpdateListener()`, as well as old POI.
//!
//! ## Receiving Locations via `setUpdateListener()`
//!
//! ```json
//! payload: {
//!     action:     "pos",
//!     lat:        47.994828,
//!     lng:        7.849881,
//!     timestamp:  1712928222,
//!     contactId:  123,    // can be used as a unique ID to differ tracks etc
//!     name:       "Alice",
//!     color:      "#ff8080",
//!     independent: false, // false: current or past position of contact, true: a POI
//!     label:       ""     // used for POI only
//! }
//! ```

use crate::{chat, location};
use std::collections::{hash_map, HashMap};

use crate::context::Context;
use crate::message::{Message, MsgId, Viewtype};

use crate::chat::ChatId;
use crate::color::color_int_to_hex_string;
use crate::contact::{Contact, ContactId};
use crate::tools::time;
use crate::webxdc::{StatusUpdateItem, StatusUpdateItemAndSerial, StatusUpdateSerial};
use anyhow::Result;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct MapsActionPayload {
    action: String,
    lat: Option<f64>,
    lng: Option<f64>,
    label: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct LocationItem {
    action: String,
    #[serde(rename = "contactId")]
    contact_id: u32,
    lat: f64,
    lng: f64,
    independent: bool,
    timestamp: i64,
    label: String,
    name: String,
    color: String,
}

pub(crate) async fn intercept_send_update(
    context: &Context,
    chat_id: Option<ChatId>,
    status_update: StatusUpdateItem,
) -> Result<()> {
    let payload = serde_json::from_value::<MapsActionPayload>(status_update.payload)?;
    let lat = payload.lat.unwrap_or_default();
    let lng = payload.lng.unwrap_or_default();
    let label = payload.label.unwrap_or_default();

    if payload.action == "pos" && !label.is_empty() {
        let chat_id = if let Some(chat_id) = chat_id {
            chat_id
        } else {
            ChatId::create_for_contact(context, ContactId::SELF).await?
        };

        let mut poi_msg = Message::new(Viewtype::Text);
        poi_msg.text = label;
        poi_msg.set_location(lat, lng);
        chat::send_msg(context, chat_id, &mut poi_msg).await?;
    } else {
        warn!(context, "unknown maps integration action");
    }

    Ok(())
}

pub(crate) async fn intercept_get_updates(
    context: &Context,
    chat_id: Option<ChatId>,
    last_known_serial: StatusUpdateSerial,
) -> Result<String> {
    let mut json = String::default();
    let mut contact_data: HashMap<ContactId, (String, String)> = HashMap::new();

    let begin = time() - 24 * 60 * 60;
    let locations = location::get_range(context, chat_id, None, begin, 0).await?;
    for location in locations.iter().rev() {
        if location.location_id > last_known_serial.to_u32() {
            let (name, color) = match contact_data.entry(location.contact_id) {
                hash_map::Entry::Vacant(e) => {
                    let contact = Contact::get_by_id(context, location.contact_id).await?;
                    let name = contact.get_display_name().to_string();
                    let color = color_int_to_hex_string(contact.get_color());
                    e.insert((name, color)).clone()
                }
                hash_map::Entry::Occupied(e) => e.get().clone(),
            };

            let mut label = String::new();
            if location.independent != 0 {
                if let Some(marker) = &location.marker {
                    label = marker.to_string() // marker contains one-char labels only
                } else if location.msg_id != 0 {
                    if let Some(msg) =
                        Message::load_from_db_optional(context, MsgId::new(location.msg_id)).await?
                    {
                        label = msg.get_text()
                    }
                }
            }

            let location_item = LocationItem {
                action: "pos".to_string(),
                contact_id: location.contact_id.to_u32(),
                lat: location.latitude,
                lng: location.longitude,
                independent: location.independent != 0,
                timestamp: location.timestamp,
                label,
                name,
                color,
            };

            let update_item = StatusUpdateItemAndSerial {
                item: StatusUpdateItem {
                    payload: serde_json::to_value(location_item)?,
                    info: None,
                    document: None,
                    summary: None,
                    uid: None,
                },
                serial: StatusUpdateSerial(location.location_id),
                max_serial: StatusUpdateSerial(location.location_id),
            };

            if !json.is_empty() {
                json.push_str(",\n");
            }
            json.push_str(&serde_json::to_string(&update_item)?);
        }
    }

    Ok(format!("[{json}]"))
}

