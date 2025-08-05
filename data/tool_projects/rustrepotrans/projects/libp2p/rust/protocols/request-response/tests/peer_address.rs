use libp2p_core::ConnectedPoint;
use libp2p_request_response as request_response;
use libp2p_request_response::ProtocolSupport;
use libp2p_swarm::{StreamProtocol, Swarm, SwarmEvent};
use libp2p_swarm_test::SwarmExt;
use serde::{Deserialize, Serialize};
use std::iter;
use tracing_subscriber::EnvFilter;

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
struct Ping(Vec<u8>);
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
struct Pong(Vec<u8>);
