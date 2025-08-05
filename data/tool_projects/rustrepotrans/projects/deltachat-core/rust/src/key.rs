//! Cryptographic key module.

use std::collections::BTreeMap;
use std::fmt;
use std::io::Cursor;

use anyhow::{ensure, Context as _, Result};
use base64::Engine as _;
use deltachat_contact_tools::EmailAddress;
use num_traits::FromPrimitive;
use pgp::composed::Deserializable;
pub use pgp::composed::{SignedPublicKey, SignedSecretKey};
use pgp::ser::Serialize;
use pgp::types::{KeyTrait, SecretKeyTrait};
use tokio::runtime::Handle;

use crate::config::Config;
use crate::constants::KeyGenType;
use crate::context::Context;
use crate::log::LogExt;
use crate::pgp::KeyPair;
use crate::tools::{self, time_elapsed};

/// Convenience trait for working with keys.
///
/// This trait is implemented for rPGP's [SignedPublicKey] and
/// [SignedSecretKey] types and makes working with them a little
/// easier in the deltachat world.
pub(crate) trait DcKey: Serialize + Deserializable + KeyTrait + Clone {
    /// Create a key from some bytes.
    fn from_slice(bytes: &[u8]) -> Result<Self> {
        Ok(<Self as Deserializable>::from_bytes(Cursor::new(bytes))?)
    }

    /// Create a key from a base64 string.
    fn from_base64(data: &str) -> Result<Self> {
        // strip newlines and other whitespace
        let cleaned: String = data.split_whitespace().collect();
        let bytes = base64::engine::general_purpose::STANDARD.decode(cleaned.as_bytes())?;
        Self::from_slice(&bytes)
    }

    /// Create a key from an ASCII-armored string.
    ///
    /// Returns the key and a map of any headers which might have been set in
    /// the ASCII-armored representation.
    fn from_asc(data: &str) -> Result<(Self, BTreeMap<String, String>)> {
        let bytes = data.as_bytes();
        Self::from_armor_single(Cursor::new(bytes)).context("rPGP error")
    }

    /// Serialise the key as bytes.
    fn to_bytes(&self) -> Vec<u8> {
        // Not using Serialize::to_bytes() to make clear *why* it is
        // safe to ignore this error.
        // Because we write to a Vec<u8> the io::Write impls never
        // fail and we can hide this error.
        let mut buf = Vec::new();
        self.to_writer(&mut buf).unwrap();
        buf
    }

    /// Serialise the key to a base64 string.
    fn to_base64(&self) -> String {
        base64::engine::general_purpose::STANDARD.encode(DcKey::to_bytes(self))
    }

    /// Serialise the key to ASCII-armored representation.
    ///
    /// Each header line must be terminated by `\r\n`.  Only allows setting one
    /// header as a simplification since that's the only way it's used so far.
    // Since .to_armored_string() are actual methods on SignedPublicKey and
    // SignedSecretKey we can not generically implement this.
    fn to_asc(&self, header: Option<(&str, &str)>) -> String;

    /// The fingerprint for the key.
    fn fingerprint(&self) -> Fingerprint {
        Fingerprint::new(KeyTrait::fingerprint(self))
    }
}

pub(crate) async fn load_self_public_key(context: &Context) -> Result<SignedPublicKey> {
    let public_key = context
        .sql
        .query_row_optional(
            "SELECT public_key
             FROM keypairs
             WHERE id=(SELECT value FROM config WHERE keyname='key_id')",
            (),
            |row| {
                let bytes: Vec<u8> = row.get(0)?;
                Ok(bytes)
            },
        )
        .await?;
    match public_key {
        Some(bytes) => SignedPublicKey::from_slice(&bytes),
        None => {
            let keypair = generate_keypair(context).await?;
            Ok(keypair.public)
        }
    }
}

/// Returns our own public keyring.
pub(crate) async fn load_self_public_keyring(context: &Context) -> Result<Vec<SignedPublicKey>> {
    let keys = context
        .sql
        .query_map(
            r#"SELECT public_key
               FROM keypairs
               ORDER BY id=(SELECT value FROM config WHERE keyname='key_id') DESC"#,
            (),
            |row| row.get::<_, Vec<u8>>(0),
            |keys| keys.collect::<Result<Vec<_>, _>>().map_err(Into::into),
        )
        .await?
        .into_iter()
        .filter_map(|bytes| SignedPublicKey::from_slice(&bytes).log_err(context).ok())
        .collect();
    Ok(keys)
}

pub(crate) async fn load_self_secret_key(context: &Context) -> Result<SignedSecretKey> {
    let private_key = context
        .sql
        .query_row_optional(
            "SELECT private_key
             FROM keypairs
             WHERE id=(SELECT value FROM config WHERE keyname='key_id')",
            (),
            |row| {
                let bytes: Vec<u8> = row.get(0)?;
                Ok(bytes)
            },
        )
        .await?;
    match private_key {
        Some(bytes) => SignedSecretKey::from_slice(&bytes),
        None => {
            let keypair = generate_keypair(context).await?;
            Ok(keypair.secret)
        }
    }
}

pub(crate) async fn load_self_secret_keyring(context: &Context) -> Result<Vec<SignedSecretKey>> {
    let keys = context
        .sql
        .query_map(
            r#"SELECT private_key
               FROM keypairs
               ORDER BY id=(SELECT value FROM config WHERE keyname='key_id') DESC"#,
            (),
            |row| row.get::<_, Vec<u8>>(0),
            |keys| keys.collect::<Result<Vec<_>, _>>().map_err(Into::into),
        )
        .await?
        .into_iter()
        .filter_map(|bytes| SignedSecretKey::from_slice(&bytes).log_err(context).ok())
        .collect();
    Ok(keys)
}

impl DcKey for SignedPublicKey {
    fn to_asc(&self, header: Option<(&str, &str)>) -> String {
        // Not using .to_armored_string() to make clear *why* it is
        // safe to ignore this error.
        // Because we write to a Vec<u8> the io::Write impls never
        // fail and we can hide this error.
        let headers = header.map(|(key, value)| {
            let mut m = BTreeMap::new();
            m.insert(key.to_string(), value.to_string());
            m
        });
        let mut buf = Vec::new();
        self.to_armored_writer(&mut buf, headers.as_ref())
            .unwrap_or_default();
        std::string::String::from_utf8(buf).unwrap_or_default()
    }
}

impl DcKey for SignedSecretKey {
    fn to_asc(&self, header: Option<(&str, &str)>) -> String {
        // Not using .to_armored_string() to make clear *why* it is
        // safe to do these unwraps.
        // Because we write to a Vec<u8> the io::Write impls never
        // fail and we can hide this error.  The string is always ASCII.
        let headers = header.map(|(key, value)| {
            let mut m = BTreeMap::new();
            m.insert(key.to_string(), value.to_string());
            m
        });
        let mut buf = Vec::new();
        self.to_armored_writer(&mut buf, headers.as_ref())
            .unwrap_or_default();
        std::string::String::from_utf8(buf).unwrap_or_default()
    }
}

/// Deltachat extension trait for secret keys.
///
/// Provides some convenience wrappers only applicable to [SignedSecretKey].
pub(crate) trait DcSecretKey {
    /// Create a public key from a private one.
    fn split_public_key(&self) -> Result<SignedPublicKey>;
}

impl DcSecretKey for SignedSecretKey {
    fn split_public_key(&self) -> Result<SignedPublicKey> {
        self.verify()?;
        let unsigned_pubkey = SecretKeyTrait::public_key(self);
        let signed_pubkey = unsigned_pubkey.sign(self, || "".into())?;
        Ok(signed_pubkey)
    }
}

async fn generate_keypair(context: &Context) -> Result<KeyPair> {
    let addr = context.get_primary_self_addr().await?;
    let addr = EmailAddress::new(&addr)?;
    let _guard = context.generating_key_mutex.lock().await;

    // Check if the key appeared while we were waiting on the lock.
    match load_keypair(context, &addr).await? {
        Some(key_pair) => Ok(key_pair),
        None => {
            let start = tools::Time::now();
            let keytype = KeyGenType::from_i32(context.get_config_int(Config::KeyGenType).await?)
                .unwrap_or_default();
            info!(context, "Generating keypair with type {}", keytype);
            let keypair = Handle::current()
                .spawn_blocking(move || crate::pgp::create_keypair(addr, keytype))
                .await??;

            store_self_keypair(context, &keypair, KeyPairUse::Default).await?;
            info!(
                context,
                "Keypair generated in {:.3}s.",
                time_elapsed(&start).as_secs(),
            );
            Ok(keypair)
        }
    }
}

pub(crate) async fn load_keypair(
    context: &Context,
    addr: &EmailAddress,
) -> Result<Option<KeyPair>> {
    let res = context
        .sql
        .query_row_optional(
            "SELECT public_key, private_key
             FROM keypairs
             WHERE id=(SELECT value FROM config WHERE keyname='key_id')",
            (),
            |row| {
                let pub_bytes: Vec<u8> = row.get(0)?;
                let sec_bytes: Vec<u8> = row.get(1)?;
                Ok((pub_bytes, sec_bytes))
            },
        )
        .await?;

    Ok(if let Some((pub_bytes, sec_bytes)) = res {
        Some(KeyPair {
            addr: addr.clone(),
            public: SignedPublicKey::from_slice(&pub_bytes)?,
            secret: SignedSecretKey::from_slice(&sec_bytes)?,
        })
    } else {
        None
    })
}

/// Use of a key pair for encryption or decryption.
///
/// This is used by `store_self_keypair` to know what kind of key is
/// being saved.
#[derive(Debug, Clone, Eq, PartialEq)]
pub enum KeyPairUse {
    /// The default key used to encrypt new messages.
    Default,
    /// Only used to decrypt existing message.
    ReadOnly,
}

/// Store the keypair as an owned keypair for addr in the database.
///
/// This will save the keypair as keys for the given address.  The
/// "self" here refers to the fact that this DC instance owns the
/// keypair.  Usually `addr` will be [Config::ConfiguredAddr].
///
/// If either the public or private keys are already present in the
/// database, this entry will be removed first regardless of the
/// address associated with it.  Practically this means saving the
/// same key again overwrites it.
///
/// [Config::ConfiguredAddr]: crate::config::Config::ConfiguredAddr
pub(crate) async fn store_self_keypair(
    context: &Context,
    keypair: &KeyPair,
    default: KeyPairUse,
) -> Result<()> {
    let mut config_cache_lock = context.sql.config_cache.write().await;
    let new_key_id = context
        .sql
        .transaction(|transaction| {
            let public_key = DcKey::to_bytes(&keypair.public);
            let secret_key = DcKey::to_bytes(&keypair.secret);

            let is_default = match default {
                KeyPairUse::Default => true,
                KeyPairUse::ReadOnly => false,
            };

            // `addr` and `is_default` written for compatibility with older versions,
            // until new cores are rolled out everywhere.
            // otherwise "add second device" or "backup" may break.
            // moreover, this allows downgrades to the previous version.
            // writing of `addr` and `is_default` can be removed ~ 2024-08
            let addr = keypair.addr.to_string();
            transaction
                .execute(
                    "INSERT OR REPLACE INTO keypairs (public_key, private_key, addr, is_default)
                     VALUES (?,?,?,?)",
                    (&public_key, &secret_key, addr, is_default),
                )
                .context("Failed to insert keypair")?;

            if is_default {
                let new_key_id = transaction.last_insert_rowid();
                transaction.execute(
                    "INSERT OR REPLACE INTO config (keyname, value) VALUES ('key_id', ?)",
                    (new_key_id,),
                )?;
                Ok(Some(new_key_id))
            } else {
                Ok(None)
            }
        })
        .await?;

    if let Some(new_key_id) = new_key_id {
        // Update config cache if transaction succeeded and changed current default key.
        config_cache_lock.insert("key_id".to_string(), Some(new_key_id.to_string()));
    }

    Ok(())
}

/// Saves a keypair as the default keys.
///
/// This API is used for testing purposes
/// to avoid generating the key in tests.
/// Use import/export APIs instead.
pub async fn preconfigure_keypair(context: &Context, addr: &str, secret_data: &str) -> Result<()> {
    let addr = EmailAddress::new(addr)?;
    let secret = SignedSecretKey::from_asc(secret_data)?.0;
    let public = secret.split_public_key()?;
    let keypair = KeyPair {
        addr,
        public,
        secret,
    };
    store_self_keypair(context, &keypair, KeyPairUse::Default).await?;
    Ok(())
}

/// A key fingerprint
#[derive(Clone, Eq, PartialEq, Hash, serde::Serialize, serde::Deserialize)]
pub struct Fingerprint(Vec<u8>);

impl Fingerprint {
    /// Creates new 160-bit (20 bytes) fingerprint.
    pub fn new(v: Vec<u8>) -> Fingerprint {
        debug_assert_eq!(v.len(), 20);
        Fingerprint(v)
    }

    /// Make a hex string from the fingerprint.
    ///
    /// Use [std::fmt::Display] or [ToString::to_string] to get a
    /// human-readable formatted string.
    pub fn hex(&self) -> String {
        hex::encode_upper(&self.0)
    }
}

impl fmt::Debug for Fingerprint {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Fingerprint")
            .field("hex", &self.hex())
            .finish()
    }
}

/// Make a human-readable fingerprint.
impl fmt::Display for Fingerprint {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        // Split key into chunks of 4 with space and newline at 20 chars
        for (i, c) in self.hex().chars().enumerate() {
            if i > 0 && i % 20 == 0 {
                writeln!(f)?;
            } else if i > 0 && i % 4 == 0 {
                write!(f, " ")?;
            }
            write!(f, "{c}")?;
        }
        Ok(())
    }
}

/// Parse a human-readable or otherwise formatted fingerprint.
impl std::str::FromStr for Fingerprint {
    type Err = anyhow::Error;

    fn from_str(input: &str) -> Result<Self> {
        let hex_repr: String = input
            .to_uppercase()
            .chars()
            .filter(|&c| c.is_ascii_hexdigit())
            .collect();
        let v: Vec<u8> = hex::decode(&hex_repr)?;
        ensure!(v.len() == 20, "wrong fingerprint length: {}", hex_repr);
        let fp = Fingerprint::new(v);
        Ok(fp)
    }
}
