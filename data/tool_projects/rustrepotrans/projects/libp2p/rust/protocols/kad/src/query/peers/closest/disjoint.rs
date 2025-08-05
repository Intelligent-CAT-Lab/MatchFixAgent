// Copyright 2020 Parity Technologies (UK) Ltd.
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

use super::*;
use std::{
    collections::HashMap,
    iter::{Cycle, Map, Peekable},
    ops::{Index, IndexMut, Range},
};

/// Wraps around a set of [`ClosestPeersIter`], enforcing a disjoint discovery
/// path per configured parallelism according to the S/Kademlia paper.
pub(crate) struct ClosestDisjointPeersIter {
    target: KeyBytes,

    /// The set of wrapped [`ClosestPeersIter`].
    iters: Vec<ClosestPeersIter>,
    /// Order in which to query the iterators ensuring fairness across
    /// [`ClosestPeersIter::next`] calls.
    iter_order: Cycle<Map<Range<usize>, fn(usize) -> IteratorIndex>>,

    /// Mapping of contacted peers by their [`PeerId`] to [`PeerState`]
    /// containing the corresponding iterator indices as well as the response
    /// state.
    ///
    /// Used to track which iterator contacted which peer. See [`PeerState`]
    /// for details.
    contacted_peers: HashMap<PeerId, PeerState>,
}

impl ClosestDisjointPeersIter {
    /// Creates a new iterator with a default configuration.
    #[cfg(test)]
    pub(crate) fn new<I>(target: KeyBytes, known_closest_peers: I) -> Self
    where
        I: IntoIterator<Item = Key<PeerId>>,
    {
        Self::with_config(
            ClosestPeersIterConfig::default(),
            target,
            known_closest_peers,
        )
    }

    /// Creates a new iterator with the given configuration.
    pub(crate) fn with_config<I, T>(
        config: ClosestPeersIterConfig,
        target: T,
        known_closest_peers: I,
    ) -> Self
    where
        I: IntoIterator<Item = Key<PeerId>>,
        T: Into<KeyBytes> + Clone,
    {
        let peers = known_closest_peers
            .into_iter()
            .take(K_VALUE.get())
            .collect::<Vec<_>>();
        let iters = (0..config.parallelism.get())
            // NOTE: All [`ClosestPeersIter`] share the same set of peers at
            // initialization. The [`ClosestDisjointPeersIter.contacted_peers`]
            // mapping ensures that a successful response from a peer is only
            // ever passed to a single [`ClosestPeersIter`]. See
            // [`ClosestDisjointPeersIter::on_success`] for details.
            .map(|_| ClosestPeersIter::with_config(config.clone(), target.clone(), peers.clone()))
            .collect::<Vec<_>>();

        let iters_len = iters.len();

        ClosestDisjointPeersIter {
            target: target.into(),
            iters,
            iter_order: (0..iters_len)
                .map(IteratorIndex as fn(usize) -> IteratorIndex)
                .cycle(),
            contacted_peers: HashMap::new(),
        }
    }

    /// Callback for informing the iterator about a failed request to a peer.
    ///
    /// If the iterator is currently waiting for a result from `peer`,
    /// the iterator state is updated and `true` is returned. In that
    /// case, after calling this function, `next` should eventually be
    /// called again to obtain the new state of the iterator.
    ///
    /// If the iterator is finished, it is not currently waiting for a
    /// result from `peer`, or a result for `peer` has already been reported,
    /// calling this function has no effect and `false` is returned.
    pub(crate) fn on_failure(&mut self, peer: &PeerId) -> bool {
        let mut updated = false;

        if let Some(PeerState {
            initiated_by,
            response,
        }) = self.contacted_peers.get_mut(peer)
        {
            updated = self.iters[*initiated_by].on_failure(peer);

            if updated {
                *response = ResponseState::Failed;
            }

            for (i, iter) in &mut self.iters.iter_mut().enumerate() {
                if IteratorIndex(i) != *initiated_by {
                    // This iterator never triggered an actual request to the
                    // given peer - thus ignore the returned boolean.
                    iter.on_failure(peer);
                }
            }
        }

        updated
    }

    /// Callback for delivering the result of a successful request to a peer.
    ///
    /// Delivering results of requests back to the iterator allows the iterator
    /// to make progress. The iterator is said to make progress either when the
    /// given `closer_peers` contain a peer closer to the target than any peer
    /// seen so far, or when the iterator did not yet accumulate `num_results`
    /// closest peers and `closer_peers` contains a new peer, regardless of its
    /// distance to the target.
    ///
    /// If the iterator is currently waiting for a result from `peer`,
    /// the iterator state is updated and `true` is returned. In that
    /// case, after calling this function, `next` should eventually be
    /// called again to obtain the new state of the iterator.
    ///
    /// If the iterator is finished, it is not currently waiting for a
    /// result from `peer`, or a result for `peer` has already been reported,
    /// calling this function has no effect and `false` is returned.
    pub(crate) fn on_success<I>(&mut self, peer: &PeerId, closer_peers: I) -> bool
    where
        I: IntoIterator<Item = PeerId>,
    {
        let mut updated = false;

        if let Some(PeerState {
            initiated_by,
            response,
        }) = self.contacted_peers.get_mut(peer)
        {
            // Pass the new `closer_peers` to the iterator that first yielded
            // the peer.
            updated = self.iters[*initiated_by].on_success(peer, closer_peers);

            if updated {
                // Mark the response as succeeded for future iterators yielding
                // this peer. There is no need to keep the `closer_peers`
                // around, given that they are only passed to the first
                // iterator.
                *response = ResponseState::Succeeded;
            }

            for (i, iter) in &mut self.iters.iter_mut().enumerate() {
                if IteratorIndex(i) != *initiated_by {
                    // Only report the success to all remaining not-first
                    // iterators. Do not pass the `closer_peers` in order to
                    // uphold the S/Kademlia disjoint paths guarantee.
                    //
                    // This iterator never triggered an actual request to the
                    // given peer - thus ignore the returned boolean.
                    iter.on_success(peer, std::iter::empty());
                }
            }
        }

        updated
    }

    pub(crate) fn next(&mut self, now: Instant) -> PeersIterState<'_> {
        let mut state = None;

        // Ensure querying each iterator at most once.
        for _ in 0..self.iters.len() {
            let i = self.iter_order.next().expect("Cycle never ends.");
            let iter = &mut self.iters[i];

            loop {
                match iter.next(now) {
                    PeersIterState::Waiting(None) => {
                        match state {
                            Some(PeersIterState::Waiting(Some(_))) => {
                                // [`ClosestDisjointPeersIter::next`] returns immediately once a
                                // [`ClosestPeersIter`] yielded a peer. Thus this state is
                                // unreachable.
                                unreachable!();
                            }
                            Some(PeersIterState::Waiting(None)) => {}
                            Some(PeersIterState::WaitingAtCapacity) => {
                                // At least one ClosestPeersIter is no longer at capacity, thus the
                                // composite ClosestDisjointPeersIter is no longer at capacity.
                                state = Some(PeersIterState::Waiting(None))
                            }
                            Some(PeersIterState::Finished) => {
                                // `state` is never set to `Finished`.
                                unreachable!();
                            }
                            None => state = Some(PeersIterState::Waiting(None)),
                        };

                        break;
                    }
                    PeersIterState::Waiting(Some(peer)) => {
                        match self.contacted_peers.get_mut(&*peer) {
                            Some(PeerState { response, .. }) => {
                                // Another iterator already contacted this peer.
                                let peer = peer.into_owned();

                                match response {
                                    // The iterator will be notified later whether the given node
                                    // was successfully contacted or not. See
                                    // [`ClosestDisjointPeersIter::on_success`] for details.
                                    ResponseState::Waiting => {}
                                    ResponseState::Succeeded => {
                                        // Given that iterator was not the first to contact the peer
                                        // it will not be made aware of the closer peers discovered
                                        // to uphold the S/Kademlia disjoint paths guarantee. See
                                        // [`ClosestDisjointPeersIter::on_success`] for details.
                                        iter.on_success(&peer, std::iter::empty());
                                    }
                                    ResponseState::Failed => {
                                        iter.on_failure(&peer);
                                    }
                                }
                            }
                            None => {
                                // The iterator is the first to contact this peer.
                                self.contacted_peers
                                    .insert(peer.clone().into_owned(), PeerState::new(i));
                                return PeersIterState::Waiting(Some(Cow::Owned(
                                    peer.into_owned(),
                                )));
                            }
                        }
                    }
                    PeersIterState::WaitingAtCapacity => {
                        match state {
                            Some(PeersIterState::Waiting(Some(_))) => {
                                // [`ClosestDisjointPeersIter::next`] returns immediately once a
                                // [`ClosestPeersIter`] yielded a peer. Thus this state is
                                // unreachable.
                                unreachable!();
                            }
                            Some(PeersIterState::Waiting(None)) => {}
                            Some(PeersIterState::WaitingAtCapacity) => {}
                            Some(PeersIterState::Finished) => {
                                // `state` is never set to `Finished`.
                                unreachable!();
                            }
                            None => state = Some(PeersIterState::WaitingAtCapacity),
                        };

                        break;
                    }
                    PeersIterState::Finished => break,
                }
            }
        }

        state.unwrap_or(PeersIterState::Finished)
    }

    /// Finishes all paths containing one of the given peers.
    ///
    /// See [`crate::query::Query::try_finish`] for details.
    pub(crate) fn finish_paths<'a, I>(&mut self, peers: I) -> bool
    where
        I: IntoIterator<Item = &'a PeerId>,
    {
        for peer in peers {
            if let Some(PeerState { initiated_by, .. }) = self.contacted_peers.get_mut(peer) {
                self.iters[*initiated_by].finish();
            }
        }

        self.is_finished()
    }

    /// Immediately transitions the iterator to [`PeersIterState::Finished`].
    pub(crate) fn finish(&mut self) {
        for iter in &mut self.iters {
            iter.finish();
        }
    }

    /// Checks whether the iterator has finished.
    pub(crate) fn is_finished(&self) -> bool {
        self.iters.iter().all(|i| i.is_finished())
    }

    /// Note: In the case of no adversarial peers or connectivity issues along
    ///       any path, all paths return the same result, deduplicated through
    ///       the `ResultIter`, thus overall `into_result` returns
    ///       `num_results`. In the case of adversarial peers or connectivity
    ///       issues `ClosestDisjointPeersIter` tries to return the
    ///       `num_results` closest benign peers, but as it can not
    ///       differentiate benign from faulty paths it as well returns faulty
    ///       peers and thus overall returns more than `num_results` peers.
    pub(crate) fn into_result(self) -> impl Iterator<Item = PeerId> {
        let result_per_path = self
            .iters
            .into_iter()
            .map(|iter| iter.into_result().map(Key::from));

        ResultIter::new(self.target, result_per_path).map(Key::into_preimage)
    }
}

/// Index into the [`ClosestDisjointPeersIter`] `iters` vector.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct IteratorIndex(usize);

impl Index<IteratorIndex> for Vec<ClosestPeersIter> {
    type Output = ClosestPeersIter;

    fn index(&self, index: IteratorIndex) -> &Self::Output {
        &self[index.0]
    }
}

impl IndexMut<IteratorIndex> for Vec<ClosestPeersIter> {
    fn index_mut(&mut self, index: IteratorIndex) -> &mut Self::Output {
        &mut self[index.0]
    }
}

/// State tracking the iterator that yielded (i.e. tried to contact) a peer. See
/// [`ClosestDisjointPeersIter::on_success`] for details.
#[derive(Debug, PartialEq, Eq)]
struct PeerState {
    /// First iterator to yield the peer. Will be notified both of the outcome
    /// (success/failure) as well as the closer peers.
    initiated_by: IteratorIndex,
    /// Keeping track of the response state. In case other iterators later on
    /// yield the same peer, they can be notified of the response outcome.
    response: ResponseState,
}

impl PeerState {
    fn new(initiated_by: IteratorIndex) -> Self {
        PeerState {
            initiated_by,
            response: ResponseState::Waiting,
        }
    }
}

#[derive(Debug, PartialEq, Eq)]
enum ResponseState {
    Waiting,
    Succeeded,
    Failed,
}

/// Iterator combining the result of multiple [`ClosestPeersIter`] into a single
/// deduplicated ordered iterator.
//
// Note: This operates under the assumption that `I` is ordered.
#[derive(Clone, Debug)]
struct ResultIter<I>
where
    I: Iterator<Item = Key<PeerId>>,
{
    target: KeyBytes,
    iters: Vec<Peekable<I>>,
}

impl<I: Iterator<Item = Key<PeerId>>> ResultIter<I> {
    fn new(target: KeyBytes, iters: impl Iterator<Item = I>) -> Self {
        ResultIter {
            target,
            iters: iters.map(Iterator::peekable).collect(),
        }
    }
}

impl<I: Iterator<Item = Key<PeerId>>> Iterator for ResultIter<I> {
    type Item = I::Item;

    fn next(&mut self) -> Option<Self::Item> {
        let target = &self.target;

        self.iters
            .iter_mut()
            // Find the iterator with the next closest peer.
            .fold(Option::<&mut Peekable<_>>::None, |iter_a, iter_b| {
                let Some(iter_a) = iter_a else {
                    return Some(iter_b);
                };

                match (iter_a.peek(), iter_b.peek()) {
                    (Some(next_a), Some(next_b)) => {
                        if next_a == next_b {
                            // Remove from one for deduplication.
                            iter_b.next();
                            return Some(iter_a);
                        }

                        if target.distance(next_a) < target.distance(next_b) {
                            Some(iter_a)
                        } else {
                            Some(iter_b)
                        }
                    }
                    (Some(_), None) => Some(iter_a),
                    (None, Some(_)) => Some(iter_b),
                    (None, None) => None,
                }
            })
            // Pop off the next closest peer from that iterator.
            .and_then(Iterator::next)
    }
}

