//! # Time smearing.
//!
//! As e-mails typically only use a second-based-resolution for timestamps,
//! the order of two mails sent within one second is unclear.
//! This is bad e.g. when forwarding some messages from a chat -
//! these messages will appear at the recipient easily out of order.
//!
//! We work around this issue by not sending out two mails with the same timestamp.
//! For this purpose, in short, we track the last timestamp used in `last_smeared_timestamp`
//! when another timestamp is needed in the same second, we use `last_smeared_timestamp+1`
//! after some moments without messages sent out,
//! `last_smeared_timestamp` is again in sync with the normal time.
//!
//! However, we do not do all this for the far future,
//! but at max `MAX_SECONDS_TO_LEND_FROM_FUTURE`

use std::cmp::{max, min};
use std::sync::atomic::{AtomicI64, Ordering};

pub(crate) const MAX_SECONDS_TO_LEND_FROM_FUTURE: i64 = 5;

/// Smeared timestamp generator.
#[derive(Debug)]
pub struct SmearedTimestamp {
    /// Next timestamp available for allocation.
    smeared_timestamp: AtomicI64,
}

impl SmearedTimestamp {
    /// Creates a new smeared timestamp generator.
    pub fn new() -> Self {
        Self {
            smeared_timestamp: AtomicI64::new(0),
        }
    }

    /// Allocates `count` unique timestamps.
    ///
    /// Returns the first allocated timestamp.
    pub fn create_n(&self, now: i64, count: i64) -> i64 {
        let mut prev = self.smeared_timestamp.load(Ordering::Relaxed);
        loop {
            // Advance the timestamp if it is in the past,
            // but keep `count - 1` timestamps from the past if possible.
            let t = max(prev, now - count + 1);

            // Rewind the time back if there is no room
            // to allocate `count` timestamps without going too far into the future.
            // Not going too far into the future
            // is more important than generating unique timestamps.
            let first = min(t, now + MAX_SECONDS_TO_LEND_FROM_FUTURE - count + 1);

            // Allocate `count` timestamps by advancing the current timestamp.
            let next = first + count;

            if let Err(x) = self.smeared_timestamp.compare_exchange_weak(
                prev,
                next,
                Ordering::Relaxed,
                Ordering::Relaxed,
            ) {
                prev = x;
            } else {
                return first;
            }
        }
    }

    /// Creates a single timestamp.
    pub fn create(&self, now: i64) -> i64 {
        self.create_n(now, 1)
    }

    /// Returns the current smeared timestamp.
    pub fn current(&self) -> i64 {
        self.smeared_timestamp.load(Ordering::Relaxed)
    }
}

