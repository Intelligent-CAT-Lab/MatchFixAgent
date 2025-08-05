use libp2p_autonat::v2::client::{self, Config};
use libp2p_autonat::v2::server;
use libp2p_core::transport::TransportError;
use libp2p_core::Multiaddr;
use libp2p_swarm::{
    DialError, FromSwarm, NetworkBehaviour, NewExternalAddrCandidate, Swarm, SwarmEvent,
};
use libp2p_swarm_test::SwarmExt;
use rand_core::OsRng;
use std::sync::Arc;
use std::time::Duration;
use tokio::sync::oneshot;
use tracing_subscriber::EnvFilter;

async fn new_server() -> Swarm<CombinedServer> {
    let mut node = Swarm::new_ephemeral(|identity| CombinedServer {
        autonat: libp2p_autonat::v2::server::Behaviour::default(),
        identify: libp2p_identify::Behaviour::new(libp2p_identify::Config::new(
            "/libp2p-test/1.0.0".into(),
            identity.public().clone(),
        )),
    });
    node.listen().with_tcp_addr_external().await;

    node
}

async fn new_client() -> Swarm<CombinedClient> {
    let mut node = Swarm::new_ephemeral(|identity| CombinedClient {
        autonat: libp2p_autonat::v2::client::Behaviour::new(
            OsRng,
            Config::default().with_probe_interval(Duration::from_millis(100)),
        ),
        identify: libp2p_identify::Behaviour::new(libp2p_identify::Config::new(
            "/libp2p-test/1.0.0".into(),
            identity.public().clone(),
        )),
    });
    node.listen().with_tcp_addr_external().await;
    node
}

#[derive(libp2p_swarm::NetworkBehaviour)]
#[behaviour(prelude = "libp2p_swarm::derive_prelude")]
struct CombinedServer {
    autonat: libp2p_autonat::v2::server::Behaviour,
    identify: libp2p_identify::Behaviour,
}

#[derive(libp2p_swarm::NetworkBehaviour)]
#[behaviour(prelude = "libp2p_swarm::derive_prelude")]
struct CombinedClient {
    autonat: libp2p_autonat::v2::client::Behaviour,
    identify: libp2p_identify::Behaviour,
}

async fn new_dummy() -> Swarm<libp2p_identify::Behaviour> {
    let mut node = Swarm::new_ephemeral(|identity| {
        libp2p_identify::Behaviour::new(libp2p_identify::Config::new(
            "/libp2p-test/1.0.0".into(),
            identity.public().clone(),
        ))
    });
    node.listen().with_tcp_addr_external().await;
    node
}

async fn start_and_connect() -> (Swarm<CombinedServer>, Swarm<CombinedClient>) {
    let mut alice = new_server().await;
    let mut bob = new_client().await;

    bob.connect(&mut alice).await;
    (alice, bob)
}

async fn bootstrap() -> (Swarm<CombinedServer>, Swarm<CombinedClient>) {
    let (mut alice, mut bob) = start_and_connect().await;

    let cor_server_peer = *alice.local_peer_id();
    let cor_client_peer = *bob.local_peer_id();

    let alice_task = async {
        let _ = alice
            .wait(|event| match event {
                SwarmEvent::NewExternalAddrCandidate { .. } => Some(()),
                _ => None,
            })
            .await;

        let (dialed_peer_id, dialed_connection_id) = alice
            .wait(|event| match event {
                SwarmEvent::Dialing {
                    peer_id,
                    connection_id,
                    ..
                } => peer_id.map(|peer_id| (peer_id, connection_id)),
                _ => None,
            })
            .await;

        let _ = alice
            .wait(|event| match event {
                SwarmEvent::ConnectionEstablished {
                    peer_id,
                    connection_id,
                    ..
                } if peer_id == dialed_peer_id
                    && peer_id == cor_client_peer
                    && connection_id == dialed_connection_id =>
                {
                    Some(())
                }
                _ => None,
            })
            .await;

        alice
            .wait(|event| match event {
                SwarmEvent::Behaviour(CombinedServerEvent::Autonat(_)) => Some(()),
                _ => None,
            })
            .await;
    };

    let bob_task = async {
        bob.wait(|event| match event {
            SwarmEvent::NewExternalAddrCandidate { address } => Some(address),
            _ => None,
        })
        .await;
        let incoming_conn_id = bob
            .wait(|event| match event {
                SwarmEvent::IncomingConnection { connection_id, .. } => Some(connection_id),
                _ => None,
            })
            .await;

        let _ = bob
            .wait(|event| match event {
                SwarmEvent::ConnectionEstablished {
                    connection_id,
                    peer_id,
                    ..
                } if incoming_conn_id == connection_id && peer_id == cor_server_peer => Some(()),
                _ => None,
            })
            .await;

        bob.wait(|event| match event {
            SwarmEvent::Behaviour(CombinedClientEvent::Autonat(_)) => Some(()),
            _ => None,
        })
        .await;
    };

    tokio::join!(alice_task, bob_task);
    (alice, bob)
}
