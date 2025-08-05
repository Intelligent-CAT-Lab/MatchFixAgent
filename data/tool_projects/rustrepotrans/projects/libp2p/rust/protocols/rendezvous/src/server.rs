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

use crate::codec::{Cookie, ErrorCode, Message, Namespace, NewRegistration, Registration, Ttl};
use crate::{MAX_TTL, MIN_TTL};
use bimap::BiMap;
use futures::future::BoxFuture;
use futures::stream::FuturesUnordered;
use futures::{FutureExt, StreamExt};
use libp2p_core::transport::PortUse;
use libp2p_core::{Endpoint, Multiaddr};
use libp2p_identity::PeerId;
use libp2p_request_response::ProtocolSupport;
use libp2p_swarm::behaviour::FromSwarm;
use libp2p_swarm::{
    ConnectionDenied, ConnectionId, NetworkBehaviour, THandler, THandlerInEvent, THandlerOutEvent,
    ToSwarm,
};
use std::collections::{HashMap, HashSet};
use std::iter;
use std::task::{ready, Context, Poll};
use std::time::Duration;

pub struct Behaviour {
    inner: libp2p_request_response::Behaviour<crate::codec::Codec>,

    registrations: Registrations,
}

pub struct Config {
    min_ttl: Ttl,
    max_ttl: Ttl,
}

impl Config {
    pub fn with_min_ttl(mut self, min_ttl: Ttl) -> Self {
        self.min_ttl = min_ttl;
        self
    }

    pub fn with_max_ttl(mut self, max_ttl: Ttl) -> Self {
        self.max_ttl = max_ttl;
        self
    }
}

impl Default for Config {
    fn default() -> Self {
        Self {
            min_ttl: MIN_TTL,
            max_ttl: MAX_TTL,
        }
    }
}

impl Behaviour {
    /// Create a new instance of the rendezvous [`NetworkBehaviour`].
    pub fn new(config: Config) -> Self {
        Self {
            inner: libp2p_request_response::Behaviour::with_codec(
                crate::codec::Codec::default(),
                iter::once((crate::PROTOCOL_IDENT, ProtocolSupport::Inbound)),
                libp2p_request_response::Config::default(),
            ),

            registrations: Registrations::with_config(config),
        }
    }
}

#[derive(Debug)]
#[allow(clippy::large_enum_variant)]
pub enum Event {
    /// We successfully served a discover request from a peer.
    DiscoverServed {
        enquirer: PeerId,
        registrations: Vec<Registration>,
    },
    /// We failed to serve a discover request for a peer.
    DiscoverNotServed { enquirer: PeerId, error: ErrorCode },
    /// A peer successfully registered with us.
    PeerRegistered {
        peer: PeerId,
        registration: Registration,
    },
    /// We declined a registration from a peer.
    PeerNotRegistered {
        peer: PeerId,
        namespace: Namespace,
        error: ErrorCode,
    },
    /// A peer successfully unregistered with us.
    PeerUnregistered { peer: PeerId, namespace: Namespace },
    /// A registration from a peer expired.
    RegistrationExpired(Registration),
}

impl NetworkBehaviour for Behaviour {
    type ConnectionHandler = <libp2p_request_response::Behaviour<
        crate::codec::Codec,
    > as NetworkBehaviour>::ConnectionHandler;

    type ToSwarm = Event;

    fn handle_established_inbound_connection(
        &mut self,
        connection_id: ConnectionId,
        peer: PeerId,
        local_addr: &Multiaddr,
        remote_addr: &Multiaddr,
    ) -> Result<THandler<Self>, ConnectionDenied> {
        self.inner.handle_established_inbound_connection(
            connection_id,
            peer,
            local_addr,
            remote_addr,
        )
    }

    fn handle_established_outbound_connection(
        &mut self,
        connection_id: ConnectionId,
        peer: PeerId,
        addr: &Multiaddr,
        role_override: Endpoint,
        port_use: PortUse,
    ) -> Result<THandler<Self>, ConnectionDenied> {
        self.inner.handle_established_outbound_connection(
            connection_id,
            peer,
            addr,
            role_override,
            port_use,
        )
    }

    fn on_connection_handler_event(
        &mut self,
        peer_id: PeerId,
        connection: ConnectionId,
        event: THandlerOutEvent<Self>,
    ) {
        self.inner
            .on_connection_handler_event(peer_id, connection, event);
    }

    #[tracing::instrument(level = "trace", name = "NetworkBehaviour::poll", skip(self, cx))]
    fn poll(
        &mut self,
        cx: &mut Context<'_>,
    ) -> Poll<ToSwarm<Self::ToSwarm, THandlerInEvent<Self>>> {
        if let Poll::Ready(ExpiredRegistration(registration)) = self.registrations.poll(cx) {
            return Poll::Ready(ToSwarm::GenerateEvent(Event::RegistrationExpired(
                registration,
            )));
        }

        loop {
            if let Poll::Ready(to_swarm) = self.inner.poll(cx) {
                match to_swarm {
                    ToSwarm::GenerateEvent(libp2p_request_response::Event::Message {
                        peer: peer_id,
                        message:
                            libp2p_request_response::Message::Request {
                                request, channel, ..
                            },
                    }) => {
                        if let Some((event, response)) =
                            handle_request(peer_id, request, &mut self.registrations)
                        {
                            if let Some(resp) = response {
                                self.inner
                                    .send_response(channel, resp)
                                    .expect("Send response");
                            }

                            return Poll::Ready(ToSwarm::GenerateEvent(event));
                        }

                        continue;
                    }
                    ToSwarm::GenerateEvent(libp2p_request_response::Event::InboundFailure {
                        peer,
                        request_id,
                        error,
                    }) => {
                        tracing::warn!(
                            %peer,
                            request=%request_id,
                            "Inbound request with peer failed: {error}"
                        );

                        continue;
                    }
                    ToSwarm::GenerateEvent(libp2p_request_response::Event::ResponseSent {
                        ..
                    })
                    | ToSwarm::GenerateEvent(libp2p_request_response::Event::Message {
                        peer: _,
                        message: libp2p_request_response::Message::Response { .. },
                    })
                    | ToSwarm::GenerateEvent(libp2p_request_response::Event::OutboundFailure {
                        ..
                    }) => {
                        continue;
                    }
                    other => {
                        let new_to_swarm = other
                            .map_out(|_| unreachable!("we manually map `GenerateEvent` variants"));

                        return Poll::Ready(new_to_swarm);
                    }
                };
            }

            return Poll::Pending;
        }
    }

    fn on_swarm_event(&mut self, event: FromSwarm) {
        self.inner.on_swarm_event(event);
    }
}

fn handle_request(
    peer_id: PeerId,
    message: Message,
    registrations: &mut Registrations,
) -> Option<(Event, Option<Message>)> {
    match message {
        Message::Register(registration) => {
            if registration.record.peer_id() != peer_id {
                let error = ErrorCode::NotAuthorized;

                let event = Event::PeerNotRegistered {
                    peer: peer_id,
                    namespace: registration.namespace,
                    error,
                };

                return Some((event, Some(Message::RegisterResponse(Err(error)))));
            }

            let namespace = registration.namespace.clone();

            match registrations.add(registration) {
                Ok(registration) => {
                    let response = Message::RegisterResponse(Ok(registration.ttl));

                    let event = Event::PeerRegistered {
                        peer: peer_id,
                        registration,
                    };

                    Some((event, Some(response)))
                }
                Err(TtlOutOfRange::TooLong { .. }) | Err(TtlOutOfRange::TooShort { .. }) => {
                    let error = ErrorCode::InvalidTtl;

                    let response = Message::RegisterResponse(Err(error));

                    let event = Event::PeerNotRegistered {
                        peer: peer_id,
                        namespace,
                        error,
                    };

                    Some((event, Some(response)))
                }
            }
        }
        Message::Unregister(namespace) => {
            registrations.remove(namespace.clone(), peer_id);

            let event = Event::PeerUnregistered {
                peer: peer_id,
                namespace,
            };

            Some((event, None))
        }
        Message::Discover {
            namespace,
            cookie,
            limit,
        } => match registrations.get(namespace, cookie, limit) {
            Ok((registrations, cookie)) => {
                let discovered = registrations.cloned().collect::<Vec<_>>();

                let response = Message::DiscoverResponse(Ok((discovered.clone(), cookie)));

                let event = Event::DiscoverServed {
                    enquirer: peer_id,
                    registrations: discovered,
                };

                Some((event, Some(response)))
            }
            Err(_) => {
                let error = ErrorCode::InvalidCookie;

                let response = Message::DiscoverResponse(Err(error));

                let event = Event::DiscoverNotServed {
                    enquirer: peer_id,
                    error,
                };

                Some((event, Some(response)))
            }
        },
        Message::RegisterResponse(_) => None,
        Message::DiscoverResponse(_) => None,
    }
}

#[derive(Debug, Eq, PartialEq, Hash, Copy, Clone)]
struct RegistrationId(u64);

impl RegistrationId {
    fn new() -> Self {
        Self(rand::random())
    }
}

#[derive(Debug, PartialEq)]
struct ExpiredRegistration(Registration);

pub struct Registrations {
    registrations_for_peer: BiMap<(PeerId, Namespace), RegistrationId>,
    registrations: HashMap<RegistrationId, Registration>,
    cookies: HashMap<Cookie, HashSet<RegistrationId>>,
    min_ttl: Ttl,
    max_ttl: Ttl,
    next_expiry: FuturesUnordered<BoxFuture<'static, RegistrationId>>,
}

#[derive(Debug, thiserror::Error)]
pub enum TtlOutOfRange {
    #[error("Requested TTL ({requested}s) is too long; max {bound}s")]
    TooLong { bound: Ttl, requested: Ttl },
    #[error("Requested TTL ({requested}s) is too short; min {bound}s")]
    TooShort { bound: Ttl, requested: Ttl },
}

impl Default for Registrations {
    fn default() -> Self {
        Registrations::with_config(Config::default())
    }
}

impl Registrations {
    pub fn with_config(config: Config) -> Self {
        Self {
            registrations_for_peer: Default::default(),
            registrations: Default::default(),
            min_ttl: config.min_ttl,
            max_ttl: config.max_ttl,
            cookies: Default::default(),
            next_expiry: FuturesUnordered::from_iter(vec![futures::future::pending().boxed()]),
        }
    }

    pub fn add(
        &mut self,
        new_registration: NewRegistration,
    ) -> Result<Registration, TtlOutOfRange> {
        let ttl = new_registration.effective_ttl();
        if ttl > self.max_ttl {
            return Err(TtlOutOfRange::TooLong {
                bound: self.max_ttl,
                requested: ttl,
            });
        }
        if ttl < self.min_ttl {
            return Err(TtlOutOfRange::TooShort {
                bound: self.min_ttl,
                requested: ttl,
            });
        }

        let namespace = new_registration.namespace;
        let registration_id = RegistrationId::new();

        if let Some(old_registration) = self
            .registrations_for_peer
            .get_by_left(&(new_registration.record.peer_id(), namespace.clone()))
        {
            self.registrations.remove(old_registration);
        }

        self.registrations_for_peer.insert(
            (new_registration.record.peer_id(), namespace.clone()),
            registration_id,
        );

        let registration = Registration {
            namespace,
            record: new_registration.record,
            ttl,
        };
        self.registrations
            .insert(registration_id, registration.clone());

        let next_expiry = futures_timer::Delay::new(Duration::from_secs(ttl))
            .map(move |_| registration_id)
            .boxed();

        self.next_expiry.push(next_expiry);

        Ok(registration)
    }

    pub fn remove(&mut self, namespace: Namespace, peer_id: PeerId) {
        let reggo_to_remove = self
            .registrations_for_peer
            .remove_by_left(&(peer_id, namespace));

        if let Some((_, reggo_to_remove)) = reggo_to_remove {
            self.registrations.remove(&reggo_to_remove);
        }
    }

    pub fn get(
        &mut self,
        discover_namespace: Option<Namespace>,
        cookie: Option<Cookie>,
        limit: Option<u64>,
    ) -> Result<(impl Iterator<Item = &Registration> + '_, Cookie), CookieNamespaceMismatch> {
        let cookie_namespace = cookie.as_ref().and_then(|cookie| cookie.namespace());

        match (discover_namespace.as_ref(), cookie_namespace) {
            // discover all namespace but cookie is specific to a namespace? => bad
            (None, Some(_)) => return Err(CookieNamespaceMismatch),
            // discover for a namespace but cookie is for a different namespace? => bad
            (Some(namespace), Some(cookie_namespace)) if namespace != cookie_namespace => {
                return Err(CookieNamespaceMismatch)
            }
            // every other combination is fine
            _ => {}
        }

        let mut reggos_of_last_discover = cookie
            .and_then(|cookie| self.cookies.get(&cookie))
            .cloned()
            .unwrap_or_default();

        let ids = self
            .registrations_for_peer
            .iter()
            .filter_map({
                |((_, namespace), registration_id)| {
                    if reggos_of_last_discover.contains(registration_id) {
                        return None;
                    }

                    match discover_namespace.as_ref() {
                        Some(discover_namespace) if discover_namespace == namespace => {
                            Some(registration_id)
                        }
                        Some(_) => None,
                        None => Some(registration_id),
                    }
                }
            })
            .take(limit.unwrap_or(u64::MAX) as usize)
            .cloned()
            .collect::<Vec<_>>();

        reggos_of_last_discover.extend(&ids);

        let new_cookie = discover_namespace
            .map(Cookie::for_namespace)
            .unwrap_or_else(Cookie::for_all_namespaces);
        self.cookies
            .insert(new_cookie.clone(), reggos_of_last_discover);

        let regs = &self.registrations;
        let registrations = ids
            .into_iter()
            .map(move |id| regs.get(&id).expect("bad internal data structure"));

        Ok((registrations, new_cookie))
    }

    fn poll(&mut self, cx: &mut Context<'_>) -> Poll<ExpiredRegistration> {
        loop {
            let expired_registration = ready!(self.next_expiry.poll_next_unpin(cx)).expect(
                "This stream should never finish because it is initialised with a pending future",
            );

            // clean up our cookies
            self.cookies.retain(|_, registrations| {
                registrations.remove(&expired_registration);

                // retain all cookies where there are still registrations left
                !registrations.is_empty()
            });

            self.registrations_for_peer
                .remove_by_right(&expired_registration);
            match self.registrations.remove(&expired_registration) {
                None => {
                    continue;
                }
                Some(registration) => {
                    return Poll::Ready(ExpiredRegistration(registration));
                }
            }
        }
    }
}

#[derive(Debug, thiserror::Error, Eq, PartialEq)]
#[error("The provided cookie is not valid for a DISCOVER request for the given namespace")]
pub struct CookieNamespaceMismatch;

