// Copyright 2018 Parity Technologies (UK) Ltd.
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

use crate::transport::{DialOpts, ListenerId, Transport, TransportError, TransportEvent};
use fnv::FnvHashMap;
use futures::{channel::mpsc, future::Ready, prelude::*, task::Context, task::Poll};
use multiaddr::{Multiaddr, Protocol};
use once_cell::sync::Lazy;
use parking_lot::Mutex;
use rw_stream_sink::RwStreamSink;
use std::{
    collections::{hash_map::Entry, VecDeque},
    error, fmt, io,
    num::NonZeroU64,
    pin::Pin,
};

static HUB: Lazy<Hub> = Lazy::new(|| Hub(Mutex::new(FnvHashMap::default())));

struct Hub(Mutex<FnvHashMap<NonZeroU64, ChannelSender>>);

/// A [`mpsc::Sender`] enabling a [`DialFuture`] to send a [`Channel`] and the
/// port of the dialer to a [`Listener`].
type ChannelSender = mpsc::Sender<(Channel<Vec<u8>>, NonZeroU64)>;

/// A [`mpsc::Receiver`] enabling a [`Listener`] to receive a [`Channel`] and
/// the port of the dialer from a [`DialFuture`].
type ChannelReceiver = mpsc::Receiver<(Channel<Vec<u8>>, NonZeroU64)>;

impl Hub {
    /// Registers the given port on the hub.
    ///
    /// Randomizes port when given port is `0`. Returns [`None`] when given port
    /// is already occupied.
    fn register_port(&self, port: u64) -> Option<(ChannelReceiver, NonZeroU64)> {
        let mut hub = self.0.lock();

        let port = if let Some(port) = NonZeroU64::new(port) {
            port
        } else {
            loop {
                let Some(port) = NonZeroU64::new(rand::random()) else {
                    continue;
                };
                if !hub.contains_key(&port) {
                    break port;
                }
            }
        };

        let (tx, rx) = mpsc::channel(2);
        match hub.entry(port) {
            Entry::Occupied(_) => return None,
            Entry::Vacant(e) => e.insert(tx),
        };

        Some((rx, port))
    }

    fn unregister_port(&self, port: &NonZeroU64) -> Option<ChannelSender> {
        self.0.lock().remove(port)
    }

    fn get(&self, port: &NonZeroU64) -> Option<ChannelSender> {
        self.0.lock().get(port).cloned()
    }
}

/// Transport that supports `/memory/N` multiaddresses.
#[derive(Default)]
pub struct MemoryTransport {
    listeners: VecDeque<Pin<Box<Listener>>>,
}

impl MemoryTransport {
    pub fn new() -> Self {
        Self::default()
    }
}

/// Connection to a `MemoryTransport` currently being opened.
pub struct DialFuture {
    /// Ephemeral source port.
    ///
    /// These ports mimic TCP ephemeral source ports but are not actually used
    /// by the memory transport due to the direct use of channels. They merely
    /// ensure that every connection has a unique address for each dialer, which
    /// is not at the same time a listen address (analogous to TCP).
    dial_port: NonZeroU64,
    sender: ChannelSender,
    channel_to_send: Option<Channel<Vec<u8>>>,
    channel_to_return: Option<Channel<Vec<u8>>>,
}

impl DialFuture {
    fn new(port: NonZeroU64) -> Option<Self> {
        let sender = HUB.get(&port)?;

        let (_dial_port_channel, dial_port) = HUB
            .register_port(0)
            .expect("there to be some random unoccupied port.");

        let (a_tx, a_rx) = mpsc::channel(4096);
        let (b_tx, b_rx) = mpsc::channel(4096);
        Some(DialFuture {
            dial_port,
            sender,
            channel_to_send: Some(RwStreamSink::new(Chan {
                incoming: a_rx,
                outgoing: b_tx,
                dial_port: None,
            })),
            channel_to_return: Some(RwStreamSink::new(Chan {
                incoming: b_rx,
                outgoing: a_tx,
                dial_port: Some(dial_port),
            })),
        })
    }
}

impl Future for DialFuture {
    type Output = Result<Channel<Vec<u8>>, MemoryTransportError>;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        match self.sender.poll_ready(cx) {
            Poll::Pending => return Poll::Pending,
            Poll::Ready(Ok(())) => {}
            Poll::Ready(Err(_)) => return Poll::Ready(Err(MemoryTransportError::Unreachable)),
        }

        let channel_to_send = self
            .channel_to_send
            .take()
            .expect("Future should not be polled again once complete");
        let dial_port = self.dial_port;
        if self
            .sender
            .start_send((channel_to_send, dial_port))
            .is_err()
        {
            return Poll::Ready(Err(MemoryTransportError::Unreachable));
        }

        Poll::Ready(Ok(self
            .channel_to_return
            .take()
            .expect("Future should not be polled again once complete")))
    }
}

impl Transport for MemoryTransport {
    type Output = Channel<Vec<u8>>;
    type Error = MemoryTransportError;
    type ListenerUpgrade = Ready<Result<Self::Output, Self::Error>>;
    type Dial = DialFuture;

    fn listen_on(
        &mut self,
        id: ListenerId,
        addr: Multiaddr,
    ) -> Result<(), TransportError<Self::Error>> {
        let port =
            parse_memory_addr(&addr).map_err(|_| TransportError::MultiaddrNotSupported(addr))?;

        let (rx, port) = HUB
            .register_port(port)
            .ok_or(TransportError::Other(MemoryTransportError::Unreachable))?;

        let listener = Listener {
            id,
            port,
            addr: Protocol::Memory(port.get()).into(),
            receiver: rx,
            tell_listen_addr: true,
        };
        self.listeners.push_back(Box::pin(listener));

        Ok(())
    }

    fn remove_listener(&mut self, id: ListenerId) -> bool {
        if let Some(index) = self.listeners.iter().position(|listener| listener.id == id) {
            let listener = self.listeners.get_mut(index).unwrap();
            let val_in = HUB.unregister_port(&listener.port);
            debug_assert!(val_in.is_some());
            listener.receiver.close();
            true
        } else {
            false
        }
    }

    fn dial(
        &mut self,
        addr: Multiaddr,
        _opts: DialOpts,
    ) -> Result<DialFuture, TransportError<Self::Error>> {
        let port = if let Ok(port) = parse_memory_addr(&addr) {
            if let Some(port) = NonZeroU64::new(port) {
                port
            } else {
                return Err(TransportError::Other(MemoryTransportError::Unreachable));
            }
        } else {
            return Err(TransportError::MultiaddrNotSupported(addr));
        };

        DialFuture::new(port).ok_or(TransportError::Other(MemoryTransportError::Unreachable))
    }

    fn poll(
        mut self: Pin<&mut Self>,
        cx: &mut Context<'_>,
    ) -> Poll<TransportEvent<Self::ListenerUpgrade, Self::Error>>
    where
        Self: Sized,
    {
        let mut remaining = self.listeners.len();
        while let Some(mut listener) = self.listeners.pop_back() {
            if listener.tell_listen_addr {
                listener.tell_listen_addr = false;
                let listen_addr = listener.addr.clone();
                let listener_id = listener.id;
                self.listeners.push_front(listener);
                return Poll::Ready(TransportEvent::NewAddress {
                    listen_addr,
                    listener_id,
                });
            }

            let event = match Stream::poll_next(Pin::new(&mut listener.receiver), cx) {
                Poll::Pending => None,
                Poll::Ready(Some((channel, dial_port))) => Some(TransportEvent::Incoming {
                    listener_id: listener.id,
                    upgrade: future::ready(Ok(channel)),
                    local_addr: listener.addr.clone(),
                    send_back_addr: Protocol::Memory(dial_port.get()).into(),
                }),
                Poll::Ready(None) => {
                    // Listener was closed.
                    return Poll::Ready(TransportEvent::ListenerClosed {
                        listener_id: listener.id,
                        reason: Ok(()),
                    });
                }
            };

            self.listeners.push_front(listener);
            if let Some(event) = event {
                return Poll::Ready(event);
            } else {
                remaining -= 1;
                if remaining == 0 {
                    break;
                }
            }
        }
        Poll::Pending
    }
}

/// Error that can be produced from the `MemoryTransport`.
#[derive(Debug, Copy, Clone)]
pub enum MemoryTransportError {
    /// There's no listener on the given port.
    Unreachable,
    /// Tries to listen on a port that is already in use.
    AlreadyInUse,
}

impl fmt::Display for MemoryTransportError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match *self {
            MemoryTransportError::Unreachable => write!(f, "No listener on the given port."),
            MemoryTransportError::AlreadyInUse => write!(f, "Port already occupied."),
        }
    }
}

impl error::Error for MemoryTransportError {}

/// Listener for memory connections.
pub struct Listener {
    id: ListenerId,
    /// Port we're listening on.
    port: NonZeroU64,
    /// The address we are listening on.
    addr: Multiaddr,
    /// Receives incoming connections.
    receiver: ChannelReceiver,
    /// Generate [`TransportEvent::NewAddress`] to inform about our listen address.
    tell_listen_addr: bool,
}

/// If the address is `/memory/n`, returns the value of `n`.
fn parse_memory_addr(a: &Multiaddr) -> Result<u64, ()> {
    let mut protocols = a.iter();
    match protocols.next() {
        Some(Protocol::Memory(port)) => match protocols.next() {
            None | Some(Protocol::P2p(_)) => Ok(port),
            _ => Err(()),
        },
        _ => Err(()),
    }
}

/// A channel represents an established, in-memory, logical connection between two endpoints.
///
/// Implements `AsyncRead` and `AsyncWrite`.
pub type Channel<T> = RwStreamSink<Chan<T>>;

/// A channel represents an established, in-memory, logical connection between two endpoints.
///
/// Implements `Sink` and `Stream`.
pub struct Chan<T = Vec<u8>> {
    incoming: mpsc::Receiver<T>,
    outgoing: mpsc::Sender<T>,

    // Needed in [`Drop`] implementation of [`Chan`] to unregister the dialing
    // port with the global [`HUB`]. Is [`Some`] when [`Chan`] of dialer and
    // [`None`] when [`Chan`] of listener.
    //
    // Note: Listening port is unregistered in [`Drop`] implementation of
    // [`Listener`].
    dial_port: Option<NonZeroU64>,
}

impl<T> Unpin for Chan<T> {}

impl<T> Stream for Chan<T> {
    type Item = Result<T, io::Error>;

    fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {
        match Stream::poll_next(Pin::new(&mut self.incoming), cx) {
            Poll::Pending => Poll::Pending,
            Poll::Ready(None) => Poll::Ready(None),
            Poll::Ready(Some(v)) => Poll::Ready(Some(Ok(v))),
        }
    }
}

impl<T> Sink<T> for Chan<T> {
    type Error = io::Error;

    fn poll_ready(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Result<(), Self::Error>> {
        self.outgoing
            .poll_ready(cx)
            .map(|v| v.map_err(|_| io::ErrorKind::BrokenPipe.into()))
    }

    fn start_send(mut self: Pin<&mut Self>, item: T) -> Result<(), Self::Error> {
        self.outgoing
            .start_send(item)
            .map_err(|_| io::ErrorKind::BrokenPipe.into())
    }

    fn poll_flush(self: Pin<&mut Self>, _: &mut Context<'_>) -> Poll<Result<(), Self::Error>> {
        Poll::Ready(Ok(()))
    }

    fn poll_close(self: Pin<&mut Self>, _: &mut Context<'_>) -> Poll<Result<(), Self::Error>> {
        Poll::Ready(Ok(()))
    }
}

impl<T: AsRef<[u8]>> From<Chan<T>> for RwStreamSink<Chan<T>> {
    fn from(channel: Chan<T>) -> RwStreamSink<Chan<T>> {
        RwStreamSink::new(channel)
    }
}

impl<T> Drop for Chan<T> {
    fn drop(&mut self) {
        if let Some(port) = self.dial_port {
            let channel_sender = HUB.unregister_port(&port);
            debug_assert!(channel_sender.is_some());
        }
    }
}

