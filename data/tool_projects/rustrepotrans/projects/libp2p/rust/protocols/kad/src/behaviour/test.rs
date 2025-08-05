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

#![cfg(test)]

use super::*;

use crate::record::{store::MemoryStore, Key};
use crate::{K_VALUE, PROTOCOL_NAME, SHA_256_MH};
use futures::{executor::block_on, future::poll_fn, prelude::*};
use futures_timer::Delay;
use libp2p_core::{
    multiaddr::{multiaddr, Protocol},
    multihash::Multihash,
    transport::MemoryTransport,
    upgrade, Transport,
};
use libp2p_identity as identity;
use libp2p_noise as noise;
use libp2p_swarm::{self as swarm, Swarm, SwarmEvent};
use libp2p_yamux as yamux;
use quickcheck::*;
use rand::{random, rngs::StdRng, thread_rng, Rng, SeedableRng};

type TestSwarm = Swarm<Behaviour<MemoryStore>>;

fn build_node() -> (Multiaddr, TestSwarm) {
    build_node_with_config(Default::default())
}

fn build_node_with_config(cfg: Config) -> (Multiaddr, TestSwarm) {
    let local_key = identity::Keypair::generate_ed25519();
    let local_public_key = local_key.public();
    let transport = MemoryTransport::default()
        .upgrade(upgrade::Version::V1)
        .authenticate(noise::Config::new(&local_key).unwrap())
        .multiplex(yamux::Config::default())
        .boxed();

    let local_id = local_public_key.to_peer_id();
    let store = MemoryStore::new(local_id);
    let behaviour = Behaviour::with_config(local_id, store, cfg);

    let mut swarm = Swarm::new(
        transport,
        behaviour,
        local_id,
        swarm::Config::with_async_std_executor()
            .with_idle_connection_timeout(Duration::from_secs(5)),
    );

    let address: Multiaddr = Protocol::Memory(random::<u64>()).into();
    swarm.listen_on(address.clone()).unwrap();
    swarm.add_external_address(address.clone());

    (address, swarm)
}

/// Builds swarms, each listening on a port. Does *not* connect the nodes together.
fn build_nodes(num: usize) -> Vec<(Multiaddr, TestSwarm)> {
    build_nodes_with_config(num, Default::default())
}

/// Builds swarms, each listening on a port. Does *not* connect the nodes together.
fn build_nodes_with_config(num: usize, cfg: Config) -> Vec<(Multiaddr, TestSwarm)> {
    (0..num)
        .map(|_| build_node_with_config(cfg.clone()))
        .collect()
}

fn build_connected_nodes(total: usize, step: usize) -> Vec<(Multiaddr, TestSwarm)> {
    build_connected_nodes_with_config(total, step, Default::default())
}

fn build_connected_nodes_with_config(
    total: usize,
    step: usize,
    cfg: Config,
) -> Vec<(Multiaddr, TestSwarm)> {
    let mut swarms = build_nodes_with_config(total, cfg);
    let swarm_ids: Vec<_> = swarms
        .iter()
        .map(|(addr, swarm)| (addr.clone(), *swarm.local_peer_id()))
        .collect();

    let mut i = 0;
    for (j, (addr, peer_id)) in swarm_ids.iter().enumerate().skip(1) {
        if i < swarm_ids.len() {
            swarms[i]
                .1
                .behaviour_mut()
                .add_address(peer_id, addr.clone());
        }
        if j % step == 0 {
            i += step;
        }
    }

    swarms
}

fn build_fully_connected_nodes_with_config(
    total: usize,
    cfg: Config,
) -> Vec<(Multiaddr, TestSwarm)> {
    let mut swarms = build_nodes_with_config(total, cfg);
    let swarm_addr_and_peer_id: Vec<_> = swarms
        .iter()
        .map(|(addr, swarm)| (addr.clone(), *swarm.local_peer_id()))
        .collect();

    for (_addr, swarm) in swarms.iter_mut() {
        for (addr, peer) in &swarm_addr_and_peer_id {
            swarm.behaviour_mut().add_address(peer, addr.clone());
        }
    }

    swarms
}

fn random_multihash() -> Multihash<64> {
    Multihash::wrap(SHA_256_MH, &thread_rng().gen::<[u8; 32]>()).unwrap()
}

#[derive(Clone, Debug)]
struct Seed([u8; 32]);

impl Arbitrary for Seed {
    fn arbitrary(g: &mut Gen) -> Seed {
        let seed = core::array::from_fn(|_| u8::arbitrary(g));
        Seed(seed)
    }
}
