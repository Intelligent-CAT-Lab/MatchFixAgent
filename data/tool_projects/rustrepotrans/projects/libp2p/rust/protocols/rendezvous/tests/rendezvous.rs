// Copyright 2021 COMIT Network.
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

use futures::stream::FuturesUnordered;
use futures::StreamExt;
use libp2p_core::multiaddr::Protocol;
use libp2p_core::Multiaddr;
use libp2p_identity as identity;
use libp2p_rendezvous as rendezvous;
use libp2p_rendezvous::client::RegisterError;
use libp2p_swarm::{DialError, Swarm, SwarmEvent};
use libp2p_swarm_test::SwarmExt;
use std::time::Duration;
use tracing_subscriber::EnvFilter;

// test if charlie can operate as client and server simultaneously

async fn new_server_with_connected_clients<const N: usize>(
    config: rendezvous::server::Config,
) -> (
    [Swarm<rendezvous::client::Behaviour>; N],
    Swarm<rendezvous::server::Behaviour>,
) {
    let mut server = new_server(config).await;

    let mut clients: [Swarm<_>; N] = match (0usize..N)
        .map(|_| new_client())
        .collect::<FuturesUnordered<_>>()
        .collect::<Vec<_>>()
        .await
        .try_into()
    {
        Ok(clients) => clients,
        Err(_) => panic!("Vec is of size N"),
    };

    for client in &mut clients {
        client.connect(&mut server).await;
    }

    (clients, server)
}

async fn new_client() -> Swarm<rendezvous::client::Behaviour> {
    let mut client = Swarm::new_ephemeral(rendezvous::client::Behaviour::new);
    client.listen().with_memory_addr_external().await; // we need to listen otherwise we don't have addresses to register

    client
}

async fn new_server(config: rendezvous::server::Config) -> Swarm<rendezvous::server::Behaviour> {
    let mut server = Swarm::new_ephemeral(|_| rendezvous::server::Behaviour::new(config));

    server.listen().with_memory_addr_external().await;

    server
}

async fn new_combined_node() -> Swarm<Combined> {
    let mut node = Swarm::new_ephemeral(|identity| Combined {
        client: rendezvous::client::Behaviour::new(identity),
        server: rendezvous::server::Behaviour::new(rendezvous::server::Config::default()),
    });
    node.listen().with_memory_addr_external().await;

    node
}

async fn new_impersonating_client() -> Swarm<rendezvous::client::Behaviour> {
    // In reality, if Eve were to try and fake someones identity, she would obviously only know the public key.
    // Due to the type-safe API of the `Rendezvous` behaviour and `PeerRecord`, we actually cannot construct a bad `PeerRecord` (i.e. one that is claims to be someone else).
    // As such, the best we can do is hand eve a completely different keypair from what she is using to authenticate her connection.
    let someone_else = identity::Keypair::generate_ed25519();
    let mut eve = Swarm::new_ephemeral(move |_| rendezvous::client::Behaviour::new(someone_else));
    eve.listen().with_memory_addr_external().await;

    eve
}

#[derive(libp2p_swarm::NetworkBehaviour)]
#[behaviour(prelude = "libp2p_swarm::derive_prelude")]
struct Combined {
    client: rendezvous::client::Behaviour,
    server: rendezvous::server::Behaviour,
}
