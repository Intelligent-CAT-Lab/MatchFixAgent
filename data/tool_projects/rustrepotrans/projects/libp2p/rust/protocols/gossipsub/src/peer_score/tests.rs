// Copyright 2020 Sigma Prime Pty Ltd.
//
// Permission is hereby granted, free of charge, to any person obtaining a
// copy of this software and associated documentation files (the "Software"),
// to deal in the Software without restriction, including without limitation
// the rights to use, copy, modify, merge, publish, distribute, sublicense,
// and/or sell copies of the Software, and to permit persons to whom the
// Software is furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
// OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
// DEALINGS IN THE SOFTWARE.

/// A collection of unit tests mostly ported from the go implementation.
use super::*;

use crate::types::RawMessage;
use crate::{IdentTopic as Topic, Message};

// estimates a value within variance
fn within_variance(value: f64, expected: f64, variance: f64) -> bool {
    if expected >= 0.0 {
        return value > expected * (1.0 - variance) && value < expected * (1.0 + variance);
    }
    value > expected * (1.0 + variance) && value < expected * (1.0 - variance)
}

// generates a random gossipsub message with sequence number i
fn make_test_message(seq: u64) -> (MessageId, RawMessage) {
    let raw_message = RawMessage {
        source: Some(PeerId::random()),
        data: vec![12, 34, 56],
        sequence_number: Some(seq),
        topic: Topic::new("test").hash(),
        signature: None,
        key: None,
        validated: true,
    };

    let message = Message {
        source: raw_message.source,
        data: raw_message.data.clone(),
        sequence_number: raw_message.sequence_number,
        topic: raw_message.topic.clone(),
    };

    let id = default_message_id()(&message);
    (id, raw_message)
}

fn default_message_id() -> fn(&Message) -> MessageId {
    |message| {
        // default message id is: source + sequence number
        // NOTE: If either the peer_id or source is not provided, we set to 0;
        let mut source_string = if let Some(peer_id) = message.source.as_ref() {
            peer_id.to_base58()
        } else {
            PeerId::from_bytes(&[0, 1, 0])
                .expect("Valid peer id")
                .to_base58()
        };
        source_string.push_str(&message.sequence_number.unwrap_or_default().to_string());
        MessageId::from(source_string)
    }
}

