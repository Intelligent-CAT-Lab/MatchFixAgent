// Copyright 2019 Parity Technologies (UK) Ltd.
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

use futures::prelude::*;
use libp2p_core::transport::{MemoryTransport, Transport};
use libp2p_core::upgrade;
use libp2p_core::upgrade::{InboundConnectionUpgrade, OutboundConnectionUpgrade};
use libp2p_identity as identity;
use libp2p_noise as noise;
use quickcheck::*;
use std::io;
use tracing_subscriber::EnvFilter;

#[allow(dead_code)]
fn core_upgrade_compat() {
    // Tests API compatibility with the libp2p-core upgrade API,
    // i.e. if it compiles, the "test" is considered a success.
    let id_keys = identity::Keypair::generate_ed25519();
    let noise = noise::Config::new(&id_keys).unwrap();
    let _ = MemoryTransport::default()
        .upgrade(upgrade::Version::V1)
        .authenticate(noise);
}

#[derive(Debug, Clone, PartialEq, Eq)]
struct Message(Vec<u8>);

impl Arbitrary for Message {
    fn arbitrary(g: &mut Gen) -> Self {
        let s = g.gen_range(1..128 * 1024);
        let mut v = vec![0; s];
        for b in &mut v {
            *b = u8::arbitrary(g);
        }
        Message(v)
    }
}
