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

use libp2p_autonat::{
    Behaviour, Config, Event, InboundProbeError, InboundProbeEvent, ResponseError,
};
use libp2p_core::{multiaddr::Protocol, ConnectedPoint, Endpoint, Multiaddr};
use libp2p_identity::PeerId;
use libp2p_swarm::DialError;
use libp2p_swarm::{Swarm, SwarmEvent};
use libp2p_swarm_test::SwarmExt as _;
use std::{num::NonZeroU32, time::Duration};

async fn new_server_swarm(config: Option<Config>) -> (Swarm<Behaviour>, PeerId, Multiaddr) {
    let mut config = config.unwrap_or_else(|| Config {
        only_global_ips: false,
        ..Default::default()
    });
    // Don't do any outbound probes.
    config.boot_delay = Duration::from_secs(60);

    let mut server = Swarm::new_ephemeral(|key| Behaviour::new(key.public().to_peer_id(), config));
    let peer_id = *server.local_peer_id();
    let (_, addr) = server.listen().await;

    (server, peer_id, addr)
}

async fn new_client_swarm(server_id: PeerId, server_addr: Multiaddr) -> (Swarm<Behaviour>, PeerId) {
    let mut client = Swarm::new_ephemeral(|key| {
        Behaviour::new(
            key.public().to_peer_id(),
            Config {
                boot_delay: Duration::from_secs(1),
                retry_interval: Duration::from_secs(1),
                throttle_server_period: Duration::ZERO,
                only_global_ips: false,
                ..Default::default()
            },
        )
    });
    client
        .behaviour_mut()
        .add_server(server_id, Some(server_addr));
    let peer_id = *client.local_peer_id();

    (client, peer_id)
}
