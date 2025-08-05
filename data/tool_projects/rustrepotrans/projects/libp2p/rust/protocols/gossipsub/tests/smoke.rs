// Copyright 2019 Parity Technologies (UK) Ltd.
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

use async_std::prelude::FutureExt;
use futures::stream::{FuturesUnordered, SelectAll};
use futures::StreamExt;
use libp2p_gossipsub as gossipsub;
use libp2p_gossipsub::{MessageAuthenticity, ValidationMode};
use libp2p_swarm::Swarm;
use libp2p_swarm_test::SwarmExt as _;
use quickcheck::{QuickCheck, TestResult};
use rand::{seq::SliceRandom, SeedableRng};
use std::{task::Poll, time::Duration};
use tracing_subscriber::EnvFilter;
struct Graph {
    nodes: SelectAll<Swarm<gossipsub::Behaviour>>,
}

impl Graph {
    async fn new_connected(num_nodes: usize, seed: u64) -> Graph {
        if num_nodes == 0 {
            panic!("expecting at least one node");
        }

        let mut rng = rand::rngs::StdRng::seed_from_u64(seed);

        let mut not_connected_nodes = (0..num_nodes)
            .map(|_| build_node())
            .collect::<FuturesUnordered<_>>()
            .collect::<Vec<_>>()
            .await;

        let mut connected_nodes = vec![not_connected_nodes.pop().unwrap()];

        for mut next in not_connected_nodes {
            let connected = connected_nodes
                .choose_mut(&mut rng)
                .expect("at least one connected node");

            next.connect(connected).await;

            connected_nodes.push(next);
        }

        Graph {
            nodes: SelectAll::from_iter(connected_nodes),
        }
    }

    /// Polls the graph and passes each event into the provided FnMut until the closure returns
    /// `true`.
    ///
    /// Returns [`true`] on success and [`false`] on timeout.
    async fn wait_for<F: FnMut(&gossipsub::Event) -> bool>(&mut self, mut f: F) -> bool {
        let condition = async {
            loop {
                if let Ok(ev) = self
                    .nodes
                    .select_next_some()
                    .await
                    .try_into_behaviour_event()
                {
                    if f(&ev) {
                        break;
                    }
                }
            }
        };

        match condition.timeout(Duration::from_secs(10)).await {
            Ok(()) => true,
            Err(_) => false,
        }
    }

    /// Polls the graph until Poll::Pending is obtained, completing the underlying polls.
    async fn drain_events(&mut self) {
        let fut = futures::future::poll_fn(|cx| loop {
            match self.nodes.poll_next_unpin(cx) {
                Poll::Ready(_) => {}
                Poll::Pending => return Poll::Ready(()),
            }
        });
        fut.timeout(Duration::from_secs(10)).await.unwrap();
    }
}

async fn build_node() -> Swarm<gossipsub::Behaviour> {
    // NOTE: The graph of created nodes can be disconnected from the mesh point of view as nodes
    // can reach their d_lo value and not add other nodes to their mesh. To speed up this test, we
    // reduce the default values of the heartbeat, so that all nodes will receive gossip in a
    // timely fashion.

    let mut swarm = Swarm::new_ephemeral(|identity| {
        let peer_id = identity.public().to_peer_id();

        let config = gossipsub::ConfigBuilder::default()
            .heartbeat_initial_delay(Duration::from_millis(100))
            .heartbeat_interval(Duration::from_millis(200))
            .history_length(10)
            .history_gossip(10)
            .validation_mode(ValidationMode::Permissive)
            .build()
            .unwrap();
        gossipsub::Behaviour::new(MessageAuthenticity::Author(peer_id), config).unwrap()
    });
    swarm.listen().with_memory_addr_external().await;

    swarm
}

