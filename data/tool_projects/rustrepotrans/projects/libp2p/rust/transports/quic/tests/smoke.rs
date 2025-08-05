#![cfg(any(feature = "async-std", feature = "tokio"))]

use futures::channel::{mpsc, oneshot};
use futures::future::BoxFuture;
use futures::future::{poll_fn, Either};
use futures::stream::StreamExt;
use futures::{future, AsyncReadExt, AsyncWriteExt, FutureExt, SinkExt};
use futures_timer::Delay;
use libp2p_core::muxing::{StreamMuxerBox, StreamMuxerExt, SubstreamBox};
use libp2p_core::transport::{Boxed, DialOpts, OrTransport, PortUse, TransportEvent};
use libp2p_core::transport::{ListenerId, TransportError};
use libp2p_core::Endpoint;
use libp2p_core::{multiaddr::Protocol, upgrade, Multiaddr, Transport};
use libp2p_identity::PeerId;
use libp2p_noise as noise;
use libp2p_quic as quic;
use libp2p_tcp as tcp;
use libp2p_yamux as yamux;
use quic::Provider;
use rand::RngCore;
use std::future::Future;
use std::io;
use std::num::NonZeroU8;
use std::task::Poll;
use std::time::Duration;
use std::{
    pin::Pin,
    sync::{Arc, Mutex},
};
use tracing_subscriber::EnvFilter;

#[cfg(feature = "tokio")]

#[cfg(feature = "async-std")]

#[cfg(feature = "tokio")]

#[cfg(feature = "async-std")]

/// Tests that a [`Transport::dial`] wakes up the task previously polling [`Transport::poll`].
///
/// See https://github.com/libp2p/rust-libp2p/pull/3306 for context.
#[cfg(feature = "async-std")]

#[cfg(feature = "async-std")]

#[cfg(feature = "async-std")]
fn new_tcp_quic_transport() -> (PeerId, Boxed<(PeerId, StreamMuxerBox)>) {
    let keypair = generate_tls_keypair();
    let peer_id = keypair.public().to_peer_id();
    let mut config = quic::Config::new(&keypair);
    config.handshake_timeout = Duration::from_secs(1);

    let quic_transport = quic::async_std::Transport::new(config);
    let tcp_transport = tcp::async_io::Transport::new(tcp::Config::default())
        .upgrade(upgrade::Version::V1)
        .authenticate(noise::Config::new(&keypair).unwrap())
        .multiplex(yamux::Config::default());

    let transport = OrTransport::new(quic_transport, tcp_transport)
        .map(|either_output, _| match either_output {
            Either::Left((peer_id, muxer)) => (peer_id, StreamMuxerBox::new(muxer)),
            Either::Right((peer_id, muxer)) => (peer_id, StreamMuxerBox::new(muxer)),
        })
        .boxed();

    (peer_id, transport)
}

#[cfg(feature = "async-std")]

// Note: This test should likely be ported to the muxer compliance test suite.
#[cfg(feature = "async-std")]

// Note: This test should likely be ported to the muxer compliance test suite.
#[cfg(feature = "tokio")]

#[cfg(feature = "tokio")]

#[cfg(feature = "async-std")]

#[cfg(feature = "async-std")]

#[cfg(feature = "async-std")]

/// - A listens on 0.0.0.0:0
/// - B listens on 127.0.0.1:0
/// - A dials B
/// - Source port of A at B is the A's listen port
#[cfg(feature = "tokio")]

async fn smoke<P: Provider>() {
    let _ = tracing_subscriber::fmt()
        .with_env_filter(EnvFilter::from_default_env())
        .try_init();

    let (a_peer_id, mut a_transport) = create_default_transport::<P>();
    let (b_peer_id, mut b_transport) = create_default_transport::<P>();

    let addr = start_listening(&mut a_transport, "/ip4/127.0.0.1/udp/0/quic-v1").await;
    let ((a_connected, _, _), (b_connected, _)) =
        connect(&mut a_transport, &mut b_transport, addr).await;

    assert_eq!(a_connected, b_peer_id);
    assert_eq!(b_connected, a_peer_id);
}

async fn build_streams<P: Provider + Spawn>() -> (SubstreamBox, SubstreamBox) {
    let (_, mut a_transport) = create_default_transport::<P>();
    let (_, mut b_transport) = create_default_transport::<P>();

    let addr = start_listening(&mut a_transport, "/ip4/127.0.0.1/udp/0/quic-v1").await;
    let ((_, _, mut conn_a), (_, mut conn_b)) =
        connect(&mut a_transport, &mut b_transport, addr).await;
    let (stream_a_tx, stream_a_rx) = oneshot::channel();
    let (stream_b_tx, stream_b_rx) = oneshot::channel();

    P::spawn(async move {
        let mut stream_a_tx = Some(stream_a_tx);
        let mut stream_b_tx = Some(stream_b_tx);
        poll_fn::<(), _>(move |cx| {
            let _ = a_transport.poll_next_unpin(cx);
            let _ = conn_a.poll_unpin(cx);
            let _ = b_transport.poll_next_unpin(cx);
            let _ = conn_b.poll_unpin(cx);
            if stream_a_tx.is_some() {
                if let Poll::Ready(stream) = conn_a.poll_outbound_unpin(cx) {
                    let tx = stream_a_tx.take().unwrap();
                    tx.send(stream.unwrap()).unwrap();
                }
            }
            if stream_b_tx.is_some() {
                if let Poll::Ready(stream) = conn_b.poll_inbound_unpin(cx) {
                    let tx = stream_b_tx.take().unwrap();
                    tx.send(stream.unwrap()).unwrap();
                }
            }
            Poll::Pending
        })
        .await
    });
    let mut stream_a = stream_a_rx.map(Result::unwrap).await;

    // Send dummy byte to notify the peer of the new stream.
    let send_buf = [0];
    stream_a.write_all(&send_buf).await.unwrap();

    let mut stream_b = stream_b_rx.map(Result::unwrap).await;
    let mut recv_buf = [1];

    assert_eq!(stream_b.read(&mut recv_buf).await.unwrap(), 1);
    assert_eq!(send_buf, recv_buf);

    (stream_a, stream_b)
}

#[macro_export]
macro_rules! swap_protocol {
    ($addr:expr, $From:ident => $To:ident) => {
        $addr
            .into_iter()
            .map(|p| match p {
                Protocol::$From => Protocol::$To,
                _ => p,
            })
            .collect::<Multiaddr>()
    };
}

fn generate_tls_keypair() -> libp2p_identity::Keypair {
    libp2p_identity::Keypair::generate_ed25519()
}

fn create_default_transport<P: Provider>() -> (PeerId, Boxed<(PeerId, StreamMuxerBox)>) {
    create_transport::<P>(|_| {})
}

fn create_transport<P: Provider>(
    with_config: impl Fn(&mut quic::Config),
) -> (PeerId, Boxed<(PeerId, StreamMuxerBox)>) {
    let keypair = generate_tls_keypair();
    let peer_id = keypair.public().to_peer_id();
    let mut config = quic::Config::new(&keypair);
    with_config(&mut config);
    let transport = quic::GenTransport::<P>::new(config)
        .map(|(p, c), _| (p, StreamMuxerBox::new(c)))
        .boxed();

    (peer_id, transport)
}

async fn start_listening(transport: &mut Boxed<(PeerId, StreamMuxerBox)>, addr: &str) -> Multiaddr {
    transport
        .listen_on(ListenerId::next(), addr.parse().unwrap())
        .unwrap();
    match transport.next().await {
        Some(TransportEvent::NewAddress { listen_addr, .. }) => listen_addr,
        e => panic!("{e:?}"),
    }
}

fn prop<P: Provider + BlockOn + Spawn>(
    number_listeners: NonZeroU8,
    number_streams: NonZeroU8,
) -> quickcheck::TestResult {
    const BUFFER_SIZE: usize = 4096 * 10;

    let number_listeners = u8::from(number_listeners) as usize;
    let number_streams = u8::from(number_streams) as usize;

    if number_listeners > 10 || number_streams > 10 {
        return quickcheck::TestResult::discard();
    }

    let (listeners_tx, mut listeners_rx) = mpsc::channel(number_listeners);

    tracing::info!(
        stream_count=%number_streams,
        connection_count=%number_listeners,
        "Creating streams on connections"
    );

    // Spawn the listener nodes.
    for _ in 0..number_listeners {
        P::spawn({
            let mut listeners_tx = listeners_tx.clone();

            async move {
                let (peer_id, mut listener) = create_default_transport::<P>();
                let addr = start_listening(&mut listener, "/ip4/127.0.0.1/udp/0/quic-v1").await;

                listeners_tx.send((peer_id, addr)).await.unwrap();

                loop {
                    if let TransportEvent::Incoming { upgrade, .. } =
                        listener.select_next_some().await
                    {
                        let (_, connection) = upgrade.await.unwrap();

                        P::spawn(answer_inbound_streams::<P, BUFFER_SIZE>(connection));
                    }
                }
            }
        })
    }

    let (completed_streams_tx, completed_streams_rx) =
        mpsc::channel(number_streams * number_listeners);

    // For each listener node start `number_streams` requests.
    P::spawn(async move {
        let (_, mut dialer) = create_default_transport::<P>();

        while let Some((_, listener_addr)) = listeners_rx.next().await {
            let (_, connection) = dial(&mut dialer, listener_addr.clone()).await.unwrap();

            P::spawn(open_outbound_streams::<P, BUFFER_SIZE>(
                connection,
                number_streams,
                completed_streams_tx.clone(),
            ))
        }

        // Drive the dialer.
        loop {
            dialer.next().await;
        }
    });

    let completed_streams = number_streams * number_listeners;

    // Wait for all streams to complete.
    P::block_on(
        completed_streams_rx
            .take(completed_streams)
            .collect::<Vec<_>>(),
        Duration::from_secs(30),
    );

    quickcheck::TestResult::passed()
}

async fn answer_inbound_streams<P: Provider + Spawn, const BUFFER_SIZE: usize>(
    mut connection: StreamMuxerBox,
) {
    loop {
        let Ok(mut inbound_stream) = future::poll_fn(|cx| {
            let _ = connection.poll_unpin(cx)?;
            connection.poll_inbound_unpin(cx)
        })
        .await
        else {
            return;
        };

        P::spawn(async move {
            // FIXME: Need to write _some_ data before we can read on both sides.
            // Do a ping-pong exchange.
            {
                let mut pong = [0u8; 4];
                inbound_stream.write_all(b"PING").await.unwrap();
                inbound_stream.flush().await.unwrap();
                inbound_stream.read_exact(&mut pong).await.unwrap();
                assert_eq!(&pong, b"PONG");
            }

            let mut data = vec![0; BUFFER_SIZE];

            inbound_stream.read_exact(&mut data).await.unwrap();
            inbound_stream.write_all(&data).await.unwrap();
            inbound_stream.close().await.unwrap();
        });
    }
}

async fn open_outbound_streams<P: Provider + Spawn, const BUFFER_SIZE: usize>(
    mut connection: StreamMuxerBox,
    number_streams: usize,
    completed_streams_tx: mpsc::Sender<()>,
) {
    for _ in 0..number_streams {
        let mut outbound_stream = future::poll_fn(|cx| {
            let _ = connection.poll_unpin(cx)?;

            connection.poll_outbound_unpin(cx)
        })
        .await
        .unwrap();

        P::spawn({
            let mut completed_streams_tx = completed_streams_tx.clone();

            async move {
                // FIXME: Need to write _some_ data before we can read on both sides.
                // Do a ping-pong exchange.
                {
                    let mut ping = [0u8; 4];
                    outbound_stream.write_all(b"PONG").await.unwrap();
                    outbound_stream.flush().await.unwrap();
                    outbound_stream.read_exact(&mut ping).await.unwrap();
                    assert_eq!(&ping, b"PING");
                }

                let mut data = vec![0; BUFFER_SIZE];
                rand::thread_rng().fill_bytes(&mut data);

                let mut received = Vec::new();

                outbound_stream.write_all(&data).await.unwrap();
                outbound_stream.flush().await.unwrap();
                outbound_stream.read_to_end(&mut received).await.unwrap();

                assert_eq!(received, data);

                completed_streams_tx.send(()).await.unwrap();
            }
        });
    }

    tracing::info!(
        stream_count=%number_streams,
        "Created streams"
    );

    while future::poll_fn(|cx| connection.poll_unpin(cx))
        .await
        .is_ok()
    {}
}

/// Helper function for driving two transports until they established a connection.
#[allow(unknown_lints, clippy::needless_pass_by_ref_mut)] // False positive.
async fn connect(
    listener: &mut Boxed<(PeerId, StreamMuxerBox)>,
    dialer: &mut Boxed<(PeerId, StreamMuxerBox)>,
    addr: Multiaddr,
) -> (
    (PeerId, Multiaddr, StreamMuxerBox),
    (PeerId, StreamMuxerBox),
) {
    future::join(
        async {
            let (upgrade, send_back_addr) =
                listener.select_next_some().await.into_incoming().unwrap();
            let (peer_id, connection) = upgrade.await.unwrap();

            (peer_id, send_back_addr, connection)
        },
        async { dial(dialer, addr).await.unwrap() },
    )
    .await
}

/// Helper function for dialling that also polls the `Transport`.
async fn dial(
    transport: &mut Boxed<(PeerId, StreamMuxerBox)>,
    addr: Multiaddr,
) -> io::Result<(PeerId, StreamMuxerBox)> {
    match future::select(
        transport
            .dial(
                addr,
                DialOpts {
                    role: Endpoint::Dialer,
                    port_use: PortUse::Reuse,
                },
            )
            .unwrap(),
        transport.next(),
    )
    .await
    {
        Either::Left((conn, _)) => conn,
        Either::Right((event, _)) => {
            panic!("Unexpected event: {event:?}")
        }
    }
}

trait BlockOn {
    fn block_on<R>(future: impl Future<Output = R> + Send, timeout: Duration) -> R;
}

#[cfg(feature = "async-std")]
impl BlockOn for libp2p_quic::async_std::Provider {
    fn block_on<R>(future: impl Future<Output = R> + Send, timeout: Duration) -> R {
        async_std::task::block_on(async_std::future::timeout(timeout, future)).unwrap()
    }
}

#[cfg(feature = "tokio")]
impl BlockOn for libp2p_quic::tokio::Provider {
    fn block_on<R>(future: impl Future<Output = R> + Send, timeout: Duration) -> R {
        tokio::runtime::Handle::current()
            .block_on(tokio::time::timeout(timeout, future))
            .unwrap()
    }
}

trait Spawn {
    /// Run the given future in the background until it ends.
    fn spawn(future: impl Future<Output = ()> + Send + 'static);
}

#[cfg(feature = "async-std")]
impl Spawn for libp2p_quic::async_std::Provider {
    fn spawn(future: impl Future<Output = ()> + Send + 'static) {
        async_std::task::spawn(future);
    }
}

#[cfg(feature = "tokio")]
impl Spawn for libp2p_quic::tokio::Provider {
    fn spawn(future: impl Future<Output = ()> + Send + 'static) {
        tokio::spawn(future);
    }
}
