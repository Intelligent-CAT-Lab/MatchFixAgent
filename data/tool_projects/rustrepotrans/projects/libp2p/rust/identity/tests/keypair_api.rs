use libp2p_identity::Keypair;

#[allow(dead_code)]
fn using_keypair(kp: Keypair) {
    let _ = kp.to_protobuf_encoding();
    let _ = kp.sign(&[]);
    let _ = kp.public();
    let _: Option<[u8; 32]> = kp.derive_secret(b"foobar");
}
