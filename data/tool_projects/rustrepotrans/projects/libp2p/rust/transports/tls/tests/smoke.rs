use futures::{future, StreamExt};
use libp2p_core::multiaddr::Protocol;
use libp2p_core::transport::MemoryTransport;
use libp2p_core::upgrade::Version;
use libp2p_core::Transport;
use libp2p_swarm::{dummy, Config, Swarm, SwarmEvent};
use std::time::Duration;

fn make_swarm() -> Swarm<dummy::Behaviour> {
    let identity = libp2p_identity::Keypair::generate_ed25519();

    let transport = MemoryTransport::default()
        .upgrade(Version::V1)
        .authenticate(libp2p_tls::Config::new(&identity).unwrap())
        .multiplex(libp2p_yamux::Config::default())
        .boxed();

    Swarm::new(
        transport,
        dummy::Behaviour,
        identity.public().to_peer_id(),
        Config::with_tokio_executor().with_idle_connection_timeout(Duration::from_secs(60)),
    )
}
