//! End-to-end encryption support.

use anyhow::{format_err, Context as _, Result};
use num_traits::FromPrimitive;

use crate::aheader::{Aheader, EncryptPreference};
use crate::config::Config;
use crate::context::Context;
use crate::key::{load_self_public_key, load_self_secret_key, SignedPublicKey};
use crate::peerstate::Peerstate;
use crate::pgp;

#[derive(Debug)]
pub struct EncryptHelper {
    pub prefer_encrypt: EncryptPreference,
    pub addr: String,
    pub public_key: SignedPublicKey,
}

impl EncryptHelper {
    pub async fn new(context: &Context) -> Result<EncryptHelper> {
        let prefer_encrypt =
            EncryptPreference::from_i32(context.get_config_int(Config::E2eeEnabled).await?)
                .unwrap_or_default();
        let addr = context.get_primary_self_addr().await?;
        let public_key = load_self_public_key(context).await?;

        Ok(EncryptHelper {
            prefer_encrypt,
            addr,
            public_key,
        })
    }

    pub fn get_aheader(&self) -> Aheader {
        let pk = self.public_key.clone();
        let addr = self.addr.to_string();
        Aheader::new(addr, pk, self.prefer_encrypt)
    }

    /// Determines if we can and should encrypt.
    ///
    /// For encryption to be enabled, `e2ee_guaranteed` should be true, or strictly more than a half
    /// of peerstates should prefer encryption. Own preference is counted equally to peer
    /// preferences, even if message copy is not sent to self.
    ///
    /// `e2ee_guaranteed` should be set to true for replies to encrypted messages (as required by
    /// Autocrypt Level 1, version 1.1) and for messages sent in protected groups.
    ///
    /// Returns an error if `e2ee_guaranteed` is true, but one or more keys are missing.
    pub fn should_encrypt(
        &self,
        context: &Context,
        e2ee_guaranteed: bool,
        peerstates: &[(Option<Peerstate>, String)],
    ) -> Result<bool> {
        let mut prefer_encrypt_count = if self.prefer_encrypt == EncryptPreference::Mutual {
            1
        } else {
            0
        };
        for (peerstate, addr) in peerstates {
            match peerstate {
                Some(peerstate) => {
                    let prefer_encrypt = peerstate.prefer_encrypt;
                    info!(context, "Peerstate for {addr:?} is {prefer_encrypt}.");
                    match peerstate.prefer_encrypt {
                        EncryptPreference::NoPreference | EncryptPreference::Reset => {}
                        EncryptPreference::Mutual => prefer_encrypt_count += 1,
                    };
                }
                None => {
                    let msg = format!("Peerstate for {addr:?} missing, cannot encrypt");
                    if e2ee_guaranteed {
                        return Err(format_err!("{msg}"));
                    } else {
                        info!(context, "{msg}.");
                        return Ok(false);
                    }
                }
            }
        }

        // Count number of recipients, including self.
        // This does not depend on whether we send a copy to self or not.
        let recipients_count = peerstates.len() + 1;

        Ok(e2ee_guaranteed || 2 * prefer_encrypt_count > recipients_count)
    }

    /// Tries to encrypt the passed in `mail`.
    pub async fn encrypt(
        self,
        context: &Context,
        verified: bool,
        mail_to_encrypt: lettre_email::PartBuilder,
        peerstates: Vec<(Option<Peerstate>, String)>,
        compress: bool,
    ) -> Result<String> {
        let mut keyring: Vec<SignedPublicKey> = Vec::new();

        let mut verifier_addresses: Vec<&str> = Vec::new();

        for (peerstate, addr) in peerstates
            .iter()
            .filter_map(|(state, addr)| state.clone().map(|s| (s, addr)))
        {
            let key = peerstate
                .take_key(verified)
                .with_context(|| format!("proper enc-key for {addr} missing, cannot encrypt"))?;
            keyring.push(key);
            verifier_addresses.push(addr);
        }

        // Encrypt to self.
        keyring.push(self.public_key.clone());

        // Encrypt to secondary verified keys
        // if we also encrypt to the introducer ("verifier") of the key.
        if verified {
            for (peerstate, _addr) in &peerstates {
                if let Some(peerstate) = peerstate {
                    if let (Some(key), Some(verifier)) = (
                        peerstate.secondary_verified_key.as_ref(),
                        peerstate.secondary_verifier.as_deref(),
                    ) {
                        if verifier_addresses.contains(&verifier) {
                            keyring.push(key.clone());
                        }
                    }
                }
            }
        }

        let sign_key = load_self_secret_key(context).await?;

        let raw_message = mail_to_encrypt.build().as_string().into_bytes();

        let ctext = pgp::pk_encrypt(&raw_message, keyring, Some(sign_key), compress).await?;

        Ok(ctext)
    }

    /// Signs the passed-in `mail` using the private key from `context`.
    /// Returns the payload and the signature.
    pub async fn sign(
        self,
        context: &Context,
        mail: lettre_email::PartBuilder,
    ) -> Result<(lettre_email::MimeMessage, String)> {
        let sign_key = load_self_secret_key(context).await?;
        let mime_message = mail.build();
        let signature = pgp::pk_calc_signature(mime_message.as_string().as_bytes(), &sign_key)?;
        Ok((mime_message, signature))
    }
}

/// Ensures a private key exists for the configured user.
///
/// Normally the private key is generated when the first message is
/// sent but in a few locations there are no such guarantees,
/// e.g. when exporting keys, and calling this function ensures a
/// private key will be present.
// TODO, remove this once deltachat::key::Key no longer exists.
pub async fn ensure_secret_key_exists(context: &Context) -> Result<()> {
    load_self_public_key(context).await?;
    Ok(())
}

