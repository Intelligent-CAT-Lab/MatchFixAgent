use std::io;

use futures::{AsyncReadExt as _, AsyncWriteExt as _, StreamExt as _};
use libp2p_identity::PeerId;
use libp2p_stream as stream;
use libp2p_swarm::{StreamProtocol, Swarm};
use libp2p_swarm_test::SwarmExt as _;
use stream::OpenStreamError;
use tracing::level_filters::LevelFilter;
use tracing_subscriber::EnvFilter;

const PROTOCOL: StreamProtocol = StreamProtocol::new("/test");

