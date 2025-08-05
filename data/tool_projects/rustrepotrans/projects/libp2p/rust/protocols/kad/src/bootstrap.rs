use futures::FutureExt;
use std::task::{Context, Poll, Waker};
use std::time::Duration;

use futures_timer::Delay;

/// Default value chosen at `<https://github.com/libp2p/rust-libp2p/pull/4838#discussion_r1490184754>`.
pub(crate) const DEFAULT_AUTOMATIC_THROTTLE: Duration = Duration::from_millis(500);

#[derive(Debug)]
pub(crate) struct Status {
    /// If the user did not disable periodic bootstrap (by providing `None` for `periodic_interval`)
    /// this is the periodic interval and the delay of the current period. When `Delay` finishes,
    /// a bootstrap will be triggered and the `Delay` will be reset.
    interval_and_delay: Option<(Duration, Delay)>,

    /// Configured duration to wait before triggering a bootstrap when a new peer
    /// is inserted in the routing table. `None` if automatic bootstrap is disabled.
    automatic_throttle: Option<Duration>,
    /// Timer that will be set (if automatic bootstrap is not disabled) when a new peer is inserted
    /// in the routing table. When it finishes, it will trigger a bootstrap and will be set to `None`
    /// again. If an other new peer is inserted in the routing table before this timer finishes,
    /// the timer is reset.
    throttle_timer: Option<ThrottleTimer>,

    /// Number of bootstrap requests currently in progress. We ensure neither periodic bootstrap
    /// or automatic bootstrap trigger new requests when there is still some running.
    current_bootstrap_requests: usize,
    /// Waker to wake up the `poll` method if progress is ready to be made.
    waker: Option<Waker>,
}

impl Status {
    pub(crate) fn new(
        periodic_interval: Option<Duration>,
        automatic_throttle: Option<Duration>,
    ) -> Self {
        Self {
            interval_and_delay: periodic_interval.map(|interval| (interval, Delay::new(interval))),
            waker: None,
            automatic_throttle,
            throttle_timer: None,
            current_bootstrap_requests: 0,
        }
    }

    /// Trigger a bootstrap now or after the configured `automatic_throttle` if configured.
    pub(crate) fn trigger(&mut self) {
        // Registering `self.throttle_timer` means scheduling a bootstrap.
        // A bootstrap will be triggered when `self.throttle_timer` finishes.
        // A `throttle_timer` is useful to not trigger a batch of bootstraps when a
        // batch of peers is inserted into the routing table.
        if let Some(throttle_duration) = self.automatic_throttle {
            self.throttle_timer = Some(throttle_duration.into());
        } else {
            // The user disabled bootstrapping on new peer in the routing table.
        }

        // Waking up the waker that could have been registered.
        if let Some(waker) = self.waker.take() {
            waker.wake()
        }
    }

    pub(crate) fn reset_timers(&mut self) {
        // Canceling the `throttle_timer` if any and resetting the `delay` if any.
        self.throttle_timer = None;

        if let Some((interval, delay)) = self.interval_and_delay.as_mut() {
            delay.reset(*interval);
        }
    }

    pub(crate) fn on_started(&mut self) {
        // No periodic or automatic bootstrap will be triggered as long as
        // `self.current_bootstrap_requests > 0` but the user could still manually
        // trigger a bootstrap.
        self.current_bootstrap_requests += 1;

        // Resetting the Status timers since a bootstrap request is being triggered right now.
        self.reset_timers();
    }

    pub(crate) fn on_finish(&mut self) {
        if let Some(value) = self.current_bootstrap_requests.checked_sub(1) {
            self.current_bootstrap_requests = value;
        } else {
            debug_assert!(
                false,
                "Could not decrement current_bootstrap_requests because it's already 0"
            );
        }

        // Waking up the waker that could have been registered.
        if let Some(waker) = self.waker.take() {
            waker.wake();
        }
    }

    pub(crate) fn poll_next_bootstrap(&mut self, cx: &mut Context<'_>) -> Poll<()> {
        if self.current_bootstrap_requests > 0 {
            // Some bootstrap request(s) is(are) currently running.
            self.waker = Some(cx.waker().clone());
            return Poll::Pending;
        }

        if let Some(throttle_delay) = &mut self.throttle_timer {
            // A `throttle_timer` has been registered. It means one or more peers have been
            // inserted into the routing table and that a bootstrap request should be triggered.
            // However, to not risk cascading bootstrap requests, we wait a little time to ensure
            // the user will not add more peers in the routing table in the next "throttle_timer" remaining.
            if throttle_delay.poll_unpin(cx).is_ready() {
                // The `throttle_timer` is finished, triggering bootstrap right now.
                // The call to `on_started` will reset `throttle_delay`.
                return Poll::Ready(());
            }

            // The `throttle_timer` is not finished but the periodic interval for triggering bootstrap might be reached.
        } else {
            // No new peer has recently been inserted into the routing table or automatic bootstrap is disabled.
        }

        // Checking if the user has enabled the periodic bootstrap feature.
        if let Some((_, delay)) = self.interval_and_delay.as_mut() {
            if let Poll::Ready(()) = delay.poll_unpin(cx) {
                // It is time to run the periodic bootstrap.
                // The call to `on_started` will reset `delay`.
                return Poll::Ready(());
            }
        } else {
            // The user disabled periodic bootstrap.
        }

        // Registering the `waker` so that we can wake up when calling `on_new_peer_in_routing_table`.
        self.waker = Some(cx.waker().clone());
        Poll::Pending
    }

    #[cfg(test)]
    async fn next(&mut self) {
        std::future::poll_fn(|cx| self.poll_next_bootstrap(cx)).await
    }
}

/// Simple enum to indicate when the throttle timer resolves.
/// A dedicated `Immediate` variant is necessary because creating
/// `Delay::new(Duration::ZERO)` does not always actually resolve
/// immediately.
#[derive(Debug)]
enum ThrottleTimer {
    Immediate,
    Delay(Delay),
}

impl From<Duration> for ThrottleTimer {
    fn from(value: Duration) -> Self {
        if value.is_zero() {
            Self::Immediate
        } else {
            Self::Delay(Delay::new(value))
        }
    }
}

impl futures::Future for ThrottleTimer {
    type Output = ();

    fn poll(self: std::pin::Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        match self.get_mut() {
            Self::Immediate => Poll::Ready(()),
            Self::Delay(delay) => delay.poll_unpin(cx),
        }
    }
}

