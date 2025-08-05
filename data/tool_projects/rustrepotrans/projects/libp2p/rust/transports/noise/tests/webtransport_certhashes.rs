use libp2p_core::upgrade::{InboundConnectionUpgrade, OutboundConnectionUpgrade};
use libp2p_identity as identity;
use libp2p_noise as noise;
use multihash::Multihash;
use std::collections::HashSet;

const SHA_256_MH: u64 = 0x12;

fn certhashes() -> (Multihash<64>, Multihash<64>, Multihash<64>) {
    (
        Multihash::wrap(SHA_256_MH, b"1").unwrap(),
        Multihash::wrap(SHA_256_MH, b"2").unwrap(),
        Multihash::wrap(SHA_256_MH, b"3").unwrap(),
    )
}

// `valid_certhases` must be a strict subset of `server_certhashes`.
fn handshake_with_certhashes(
    valid_certhases: impl Into<Option<Vec<Multihash<64>>>>,
    server_certhashes: impl Into<Option<Vec<Multihash<64>>>>,
) -> Result<(), noise::Error> {
    let valid_certhases = valid_certhases.into();
    let server_certhashes = server_certhashes.into();

    let client_id = identity::Keypair::generate_ed25519();
    let server_id = identity::Keypair::generate_ed25519();

    let (client, server) = futures_ringbuf::Endpoint::pair(100, 100);

    futures::executor::block_on(async move {
        let mut client_config = noise::Config::new(&client_id)?;
        let mut server_config = noise::Config::new(&server_id)?;

        if let Some(valid_certhases) = valid_certhases {
            client_config =
                client_config.with_webtransport_certhashes(valid_certhases.into_iter().collect());
        }

        if let Some(server_certhashes) = server_certhashes {
            server_config =
                server_config.with_webtransport_certhashes(server_certhashes.into_iter().collect());
        }

        let ((reported_client_id, mut _server_session), (reported_server_id, mut _client_session)) =
            futures::future::try_join(
                server_config.upgrade_inbound(server, ""),
                client_config.upgrade_outbound(client, ""),
            )
            .await?;

        assert_eq!(reported_client_id, client_id.public().to_peer_id());
        assert_eq!(reported_server_id, server_id.public().to_peer_id());

        Ok(())
    })
}
