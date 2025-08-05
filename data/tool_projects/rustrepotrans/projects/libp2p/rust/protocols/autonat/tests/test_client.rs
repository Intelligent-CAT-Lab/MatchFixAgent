// Copyright 2021 Protocol Labs.
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

use async_std::task::JoinHandle;
use libp2p_autonat::{
    Behaviour, Config, Event, NatStatus, OutboundProbeError, OutboundProbeEvent, ResponseError,
};
use libp2p_core::Multiaddr;
use libp2p_identity::PeerId;
use libp2p_swarm::{Swarm, SwarmEvent};
use libp2p_swarm_test::SwarmExt as _;
use std::time::Duration;

const MAX_CONFIDENCE: usize = 3;
const TEST_RETRY_INTERVAL: Duration = Duration::from_secs(1);
const TEST_REFRESH_INTERVAL: Duration = Duration::from_secs(2);

async fn new_server_swarm() -> (PeerId, Multiaddr, JoinHandle<()>) {
    let mut swarm = Swarm::new_ephemeral(|key| {
        Behaviour::new(
            key.public().to_peer_id(),
            Config {
                boot_delay: Duration::from_secs(60),
                throttle_clients_peer_max: usize::MAX,
                only_global_ips: false,
                ..Default::default()
            },
        )
    });

    let (_, multiaddr) = swarm.listen().await;
    let peer_id = *swarm.local_peer_id();

    let task = async_std::task::spawn(swarm.loop_on_next());

    (peer_id, multiaddr, task)
}
