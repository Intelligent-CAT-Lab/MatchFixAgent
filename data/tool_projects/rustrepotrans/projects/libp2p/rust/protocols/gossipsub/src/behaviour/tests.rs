// Copyright 2020 Sigma Prime Pty Ltd.
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

// Collection of tests for the gossipsub network behaviour

use super::*;
use crate::subscription_filter::WhitelistSubscriptionFilter;
use crate::{config::ConfigBuilder, types::Rpc, IdentTopic as Topic};
use async_std::net::Ipv4Addr;
use byteorder::{BigEndian, ByteOrder};
use libp2p_core::ConnectedPoint;
use rand::Rng;
use std::thread::sleep;

#[derive(Default, Debug)]
struct InjectNodes<D, F>
// TODO: remove trait bound Default when this issue is fixed:
//  https://github.com/colin-kiegel/rust-derive-builder/issues/93
where
    D: DataTransform + Default + Clone + Send + 'static,
    F: TopicSubscriptionFilter + Clone + Default + Send + 'static,
{
    peer_no: usize,
    topics: Vec<String>,
    to_subscribe: bool,
    gs_config: Config,
    explicit: usize,
    outbound: usize,
    scoring: Option<(PeerScoreParams, PeerScoreThresholds)>,
    data_transform: D,
    subscription_filter: F,
}

impl<D, F> InjectNodes<D, F>
where
    D: DataTransform + Default + Clone + Send + 'static,
    F: TopicSubscriptionFilter + Clone + Default + Send + 'static,
{
    pub(crate) fn create_network(self) -> (Behaviour<D, F>, Vec<PeerId>, Vec<TopicHash>) {
        let keypair = libp2p_identity::Keypair::generate_ed25519();
        // create a gossipsub struct
        let mut gs: Behaviour<D, F> = Behaviour::new_with_subscription_filter_and_transform(
            MessageAuthenticity::Signed(keypair),
            self.gs_config,
            None,
            self.subscription_filter,
            self.data_transform,
        )
        .unwrap();

        if let Some((scoring_params, scoring_thresholds)) = self.scoring {
            gs.with_peer_score(scoring_params, scoring_thresholds)
                .unwrap();
        }

        let mut topic_hashes = vec![];

        // subscribe to the topics
        for t in self.topics {
            let topic = Topic::new(t);
            gs.subscribe(&topic).unwrap();
            topic_hashes.push(topic.hash().clone());
        }

        // build and connect peer_no random peers
        let mut peers = vec![];

        let empty = vec![];
        for i in 0..self.peer_no {
            peers.push(add_peer(
                &mut gs,
                if self.to_subscribe {
                    &topic_hashes
                } else {
                    &empty
                },
                i < self.outbound,
                i < self.explicit,
            ));
        }

        (gs, peers, topic_hashes)
    }

    fn peer_no(mut self, peer_no: usize) -> Self {
        self.peer_no = peer_no;
        self
    }

    fn topics(mut self, topics: Vec<String>) -> Self {
        self.topics = topics;
        self
    }

    #[allow(clippy::wrong_self_convention)]
    fn to_subscribe(mut self, to_subscribe: bool) -> Self {
        self.to_subscribe = to_subscribe;
        self
    }

    fn gs_config(mut self, gs_config: Config) -> Self {
        self.gs_config = gs_config;
        self
    }

    fn explicit(mut self, explicit: usize) -> Self {
        self.explicit = explicit;
        self
    }

    fn outbound(mut self, outbound: usize) -> Self {
        self.outbound = outbound;
        self
    }

    fn scoring(mut self, scoring: Option<(PeerScoreParams, PeerScoreThresholds)>) -> Self {
        self.scoring = scoring;
        self
    }

    fn subscription_filter(mut self, subscription_filter: F) -> Self {
        self.subscription_filter = subscription_filter;
        self
    }
}

fn inject_nodes<D, F>() -> InjectNodes<D, F>
where
    D: DataTransform + Default + Clone + Send + 'static,
    F: TopicSubscriptionFilter + Clone + Default + Send + 'static,
{
    InjectNodes::default()
}

fn inject_nodes1() -> InjectNodes<IdentityTransform, AllowAllSubscriptionFilter> {
    InjectNodes::<IdentityTransform, AllowAllSubscriptionFilter>::default()
}

// helper functions for testing

fn add_peer<D, F>(
    gs: &mut Behaviour<D, F>,
    topic_hashes: &[TopicHash],
    outbound: bool,
    explicit: bool,
) -> PeerId
where
    D: DataTransform + Default + Clone + Send + 'static,
    F: TopicSubscriptionFilter + Clone + Default + Send + 'static,
{
    add_peer_with_addr(gs, topic_hashes, outbound, explicit, Multiaddr::empty())
}

fn add_peer_with_addr<D, F>(
    gs: &mut Behaviour<D, F>,
    topic_hashes: &[TopicHash],
    outbound: bool,
    explicit: bool,
    address: Multiaddr,
) -> PeerId
where
    D: DataTransform + Default + Clone + Send + 'static,
    F: TopicSubscriptionFilter + Clone + Default + Send + 'static,
{
    add_peer_with_addr_and_kind(
        gs,
        topic_hashes,
        outbound,
        explicit,
        address,
        Some(PeerKind::Gossipsubv1_1),
    )
}

fn add_peer_with_addr_and_kind<D, F>(
    gs: &mut Behaviour<D, F>,
    topic_hashes: &[TopicHash],
    outbound: bool,
    explicit: bool,
    address: Multiaddr,
    kind: Option<PeerKind>,
) -> PeerId
where
    D: DataTransform + Default + Clone + Send + 'static,
    F: TopicSubscriptionFilter + Clone + Default + Send + 'static,
{
    let peer = PeerId::random();
    let endpoint = if outbound {
        ConnectedPoint::Dialer {
            address,
            role_override: Endpoint::Dialer,
            port_use: PortUse::Reuse,
        }
    } else {
        ConnectedPoint::Listener {
            local_addr: Multiaddr::empty(),
            send_back_addr: address,
        }
    };

    gs.on_swarm_event(FromSwarm::ConnectionEstablished(ConnectionEstablished {
        peer_id: peer,
        connection_id: ConnectionId::new_unchecked(0),
        endpoint: &endpoint,
        failed_addresses: &[],
        other_established: 0, // first connection
    }));
    if let Some(kind) = kind {
        gs.on_connection_handler_event(
            peer,
            ConnectionId::new_unchecked(0),
            HandlerEvent::PeerKind(kind),
        );
    }
    if explicit {
        gs.add_explicit_peer(&peer);
    }
    if !topic_hashes.is_empty() {
        gs.handle_received_subscriptions(
            &topic_hashes
                .iter()
                .cloned()
                .map(|t| Subscription {
                    action: SubscriptionAction::Subscribe,
                    topic_hash: t,
                })
                .collect::<Vec<_>>(),
            &peer,
        );
    }
    peer
}

fn disconnect_peer<D, F>(gs: &mut Behaviour<D, F>, peer_id: &PeerId)
where
    D: DataTransform + Default + Clone + Send + 'static,
    F: TopicSubscriptionFilter + Clone + Default + Send + 'static,
{
    if let Some(peer_connections) = gs.connected_peers.get(peer_id) {
        let fake_endpoint = ConnectedPoint::Dialer {
            address: Multiaddr::empty(),
            role_override: Endpoint::Dialer,
            port_use: PortUse::Reuse,
        }; // this is not relevant
           // peer_connections.connections should never be empty.

        let mut active_connections = peer_connections.connections.len();
        for connection_id in peer_connections.connections.clone() {
            active_connections = active_connections.checked_sub(1).unwrap();

            gs.on_swarm_event(FromSwarm::ConnectionClosed(ConnectionClosed {
                peer_id: *peer_id,
                connection_id,
                endpoint: &fake_endpoint,
                remaining_established: active_connections,
                cause: None,
            }));
        }
    }
}

// Converts a protobuf message into a gossipsub message for reading the Gossipsub event queue.
fn proto_to_message(rpc: &proto::RPC) -> Rpc {
    // Store valid messages.
    let mut messages = Vec::with_capacity(rpc.publish.len());
    let rpc = rpc.clone();
    for message in rpc.publish.into_iter() {
        messages.push(RawMessage {
            source: message.from.map(|x| PeerId::from_bytes(&x).unwrap()),
            data: message.data.unwrap_or_default(),
            sequence_number: message.seqno.map(|x| BigEndian::read_u64(&x)), // don't inform the application
            topic: TopicHash::from_raw(message.topic),
            signature: message.signature, // don't inform the application
            key: None,
            validated: false,
        });
    }
    let mut control_msgs = Vec::new();
    if let Some(rpc_control) = rpc.control {
        // Collect the gossipsub control messages
        let ihave_msgs: Vec<ControlAction> = rpc_control
            .ihave
            .into_iter()
            .map(|ihave| ControlAction::IHave {
                topic_hash: TopicHash::from_raw(ihave.topic_id.unwrap_or_default()),
                message_ids: ihave
                    .message_ids
                    .into_iter()
                    .map(MessageId::from)
                    .collect::<Vec<_>>(),
            })
            .collect();

        let iwant_msgs: Vec<ControlAction> = rpc_control
            .iwant
            .into_iter()
            .map(|iwant| ControlAction::IWant {
                message_ids: iwant
                    .message_ids
                    .into_iter()
                    .map(MessageId::from)
                    .collect::<Vec<_>>(),
            })
            .collect();

        let graft_msgs: Vec<ControlAction> = rpc_control
            .graft
            .into_iter()
            .map(|graft| ControlAction::Graft {
                topic_hash: TopicHash::from_raw(graft.topic_id.unwrap_or_default()),
            })
            .collect();

        let mut prune_msgs = Vec::new();

        for prune in rpc_control.prune {
            // filter out invalid peers
            let peers = prune
                .peers
                .into_iter()
                .filter_map(|info| {
                    info.peer_id
                        .and_then(|id| PeerId::from_bytes(&id).ok())
                        .map(|peer_id|
                            //TODO signedPeerRecord, see https://github.com/libp2p/specs/pull/217
                            PeerInfo {
                                peer_id: Some(peer_id),
                            })
                })
                .collect::<Vec<PeerInfo>>();

            let topic_hash = TopicHash::from_raw(prune.topic_id.unwrap_or_default());
            prune_msgs.push(ControlAction::Prune {
                topic_hash,
                peers,
                backoff: prune.backoff,
            });
        }

        control_msgs.extend(ihave_msgs);
        control_msgs.extend(iwant_msgs);
        control_msgs.extend(graft_msgs);
        control_msgs.extend(prune_msgs);
    }

    Rpc {
        messages,
        subscriptions: rpc
            .subscriptions
            .into_iter()
            .map(|sub| Subscription {
                action: if Some(true) == sub.subscribe {
                    SubscriptionAction::Subscribe
                } else {
                    SubscriptionAction::Unsubscribe
                },
                topic_hash: TopicHash::from_raw(sub.topic_id.unwrap_or_default()),
            })
            .collect(),
        control_msgs,
    }
}

/// Test local node publish to subscribed topic

/// Test local node publish to unsubscribed topic

/// Tests that the correct message is sent when a peer asks for a message in our cache.

/// Tests that messages are sent correctly depending on the shifting of the message cache.

fn count_control_msgs<D: DataTransform, F: TopicSubscriptionFilter>(
    gs: &Behaviour<D, F>,
    mut filter: impl FnMut(&PeerId, &ControlAction) -> bool,
) -> usize {
    gs.control_pool
        .iter()
        .map(|(peer_id, actions)| actions.iter().filter(|m| filter(peer_id, m)).count())
        .sum::<usize>()
        + gs.events
            .iter()
            .filter(|e| match e {
                ToSwarm::NotifyHandler {
                    peer_id,
                    event: HandlerIn::Message(RpcOut::Control(action)),
                    ..
                } => filter(peer_id, action),
                _ => false,
            })
            .count()
}

fn flush_events<D: DataTransform, F: TopicSubscriptionFilter>(gs: &mut Behaviour<D, F>) {
    gs.control_pool.clear();
    gs.events.clear();
}

// Tests the mesh maintenance addition

// Tests the mesh maintenance subtraction

///Note that in this test also without a penalty the px would be ignored because of the
/// acceptPXThreshold, but the spec still explicitly states the rule that px from negative
/// peers should get ignored, therefore we test it here.

fn random_message(seq: &mut u64, topics: &[TopicHash]) -> RawMessage {
    let mut rng = rand::thread_rng();
    *seq += 1;
    RawMessage {
        source: Some(PeerId::random()),
        data: (0..rng.gen_range(10..30)).map(|_| rng.gen()).collect(),
        sequence_number: Some(*seq),
        topic: topics[rng.gen_range(0..topics.len())].clone(),
        signature: None,
        key: None,
        validated: true,
    }
}

// Some very basic test of public api methods.

