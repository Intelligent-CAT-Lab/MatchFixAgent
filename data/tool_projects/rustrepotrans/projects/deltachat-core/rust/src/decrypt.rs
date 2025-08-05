//! End-to-end decryption support.

use std::collections::HashSet;
use std::str::FromStr;

use anyhow::Result;
use deltachat_contact_tools::addr_cmp;
use mailparse::ParsedMail;

use crate::aheader::Aheader;
use crate::authres::handle_authres;
use crate::authres::{self, DkimResults};
use crate::context::Context;
use crate::headerdef::{HeaderDef, HeaderDefMap};
use crate::key::{DcKey, Fingerprint, SignedPublicKey, SignedSecretKey};
use crate::peerstate::Peerstate;
use crate::pgp;

/// Tries to decrypt a message, but only if it is structured as an Autocrypt message.
///
/// If successful and the message is encrypted, returns decrypted body and a set of valid
/// signature fingerprints.
///
/// If the message is wrongly signed, HashSet will be empty.
pub fn try_decrypt(
    mail: &ParsedMail<'_>,
    private_keyring: &[SignedSecretKey],
    public_keyring_for_validate: &[SignedPublicKey],
) -> Result<Option<(Vec<u8>, HashSet<Fingerprint>)>> {
    let Some(encrypted_data_part) = get_encrypted_mime(mail) else {
        return Ok(None);
    };

    decrypt_part(
        encrypted_data_part,
        private_keyring,
        public_keyring_for_validate,
    )
}

pub(crate) async fn prepare_decryption(
    context: &Context,
    mail: &ParsedMail<'_>,
    from: &str,
    message_time: i64,
) -> Result<DecryptionInfo> {
    if mail.headers.get_header(HeaderDef::ListPost).is_some() {
        if mail.headers.get_header(HeaderDef::Autocrypt).is_some() {
            info!(
                context,
                "Ignoring autocrypt header since this is a mailing list message. \
                NOTE: For privacy reasons, the mailing list software should remove Autocrypt headers."
            );
        }
        return Ok(DecryptionInfo {
            from: from.to_string(),
            autocrypt_header: None,
            peerstate: None,
            message_time,
            dkim_results: DkimResults { dkim_passed: false },
        });
    }

    let autocrypt_header = if context.is_self_addr(from).await? {
        None
    } else if let Some(aheader_value) = mail.headers.get_header_value(HeaderDef::Autocrypt) {
        match Aheader::from_str(&aheader_value) {
            Ok(header) if addr_cmp(&header.addr, from) => Some(header),
            Ok(header) => {
                warn!(
                    context,
                    "Autocrypt header address {:?} is not {:?}.", header.addr, from
                );
                None
            }
            Err(err) => {
                warn!(context, "Failed to parse Autocrypt header: {:#}.", err);
                None
            }
        }
    } else {
        None
    };

    let dkim_results = handle_authres(context, mail, from).await?;
    let allow_aeap = get_encrypted_mime(mail).is_some();
    let peerstate = get_autocrypt_peerstate(
        context,
        from,
        autocrypt_header.as_ref(),
        message_time,
        allow_aeap,
    )
    .await?;

    Ok(DecryptionInfo {
        from: from.to_string(),
        autocrypt_header,
        peerstate,
        message_time,
        dkim_results,
    })
}

#[derive(Debug)]
pub struct DecryptionInfo {
    /// The From address. This is the address from the unnencrypted, outer
    /// From header.
    pub from: String,
    pub autocrypt_header: Option<Aheader>,
    /// The peerstate that will be used to validate the signatures
    pub peerstate: Option<Peerstate>,
    /// The timestamp when the message was sent.
    /// If this is older than the peerstate's last_seen, this probably
    /// means out-of-order message arrival, We don't modify the
    /// peerstate in this case.
    pub message_time: i64,
    pub(crate) dkim_results: authres::DkimResults,
}

/// Returns a reference to the encrypted payload of a message.
fn get_encrypted_mime<'a, 'b>(mail: &'a ParsedMail<'b>) -> Option<&'a ParsedMail<'b>> {
    get_autocrypt_mime(mail)
        .or_else(|| get_mixed_up_mime(mail))
        .or_else(|| get_attachment_mime(mail))
}

/// Returns a reference to the encrypted payload of a ["Mixed
/// Up"][pgpmime-message-mangling] message.
///
/// According to [RFC 3156] encrypted messages should have
/// `multipart/encrypted` MIME type and two parts, but Microsoft
/// Exchange and ProtonMail IMAP/SMTP Bridge are known to mangle this
/// structure by changing the type to `multipart/mixed` and prepending
/// an empty part at the start.
///
/// ProtonMail IMAP/SMTP Bridge prepends a part literally saying
/// "Empty Message", so we don't check its contents at all, checking
/// only for `text/plain` type.
///
/// Returns `None` if the message is not a "Mixed Up" message.
///
/// [RFC 3156]: https://www.rfc-editor.org/info/rfc3156
/// [pgpmime-message-mangling]: https://tools.ietf.org/id/draft-dkg-openpgp-pgpmime-message-mangling-00.html
fn get_mixed_up_mime<'a, 'b>(mail: &'a ParsedMail<'b>) -> Option<&'a ParsedMail<'b>> {
    if mail.ctype.mimetype != "multipart/mixed" {
        return None;
    }
    if let [first_part, second_part, third_part] = &mail.subparts[..] {
        if first_part.ctype.mimetype == "text/plain"
            && second_part.ctype.mimetype == "application/pgp-encrypted"
            && third_part.ctype.mimetype == "application/octet-stream"
        {
            Some(third_part)
        } else {
            None
        }
    } else {
        None
    }
}

/// Returns a reference to the encrypted payload of a message turned into attachment.
///
/// Google Workspace has an option "Append footer" which appends standard footer defined
/// by administrator to all outgoing messages. However, there is no plain text part in
/// encrypted messages sent by Delta Chat, so Google Workspace turns the message into
/// multipart/mixed MIME, where the first part is an empty plaintext part with a footer
/// and the second part is the original encrypted message.
fn get_attachment_mime<'a, 'b>(mail: &'a ParsedMail<'b>) -> Option<&'a ParsedMail<'b>> {
    if mail.ctype.mimetype != "multipart/mixed" {
        return None;
    }
    if let [first_part, second_part] = &mail.subparts[..] {
        if first_part.ctype.mimetype == "text/plain"
            && second_part.ctype.mimetype == "multipart/encrypted"
        {
            get_autocrypt_mime(second_part)
        } else {
            None
        }
    } else {
        None
    }
}

/// Returns a reference to the encrypted payload of a valid PGP/MIME message.
///
/// Returns `None` if the message is not a valid PGP/MIME message.
fn get_autocrypt_mime<'a, 'b>(mail: &'a ParsedMail<'b>) -> Option<&'a ParsedMail<'b>> {
    if mail.ctype.mimetype != "multipart/encrypted" {
        return None;
    }
    if let [first_part, second_part] = &mail.subparts[..] {
        if first_part.ctype.mimetype == "application/pgp-encrypted"
            && second_part.ctype.mimetype == "application/octet-stream"
        {
            Some(second_part)
        } else {
            None
        }
    } else {
        None
    }
}

/// Returns Ok(None) if nothing encrypted was found.
fn decrypt_part(
    mail: &ParsedMail<'_>,
    private_keyring: &[SignedSecretKey],
    public_keyring_for_validate: &[SignedPublicKey],
) -> Result<Option<(Vec<u8>, HashSet<Fingerprint>)>> {
    let data = mail.get_body_raw()?;

    if has_decrypted_pgp_armor(&data) {
        let (plain, ret_valid_signatures) =
            pgp::pk_decrypt(data, private_keyring, public_keyring_for_validate)?;
        return Ok(Some((plain, ret_valid_signatures)));
    }

    Ok(None)
}

#[allow(clippy::indexing_slicing)]
fn has_decrypted_pgp_armor(input: &[u8]) -> bool {
    if let Some(index) = input.iter().position(|b| *b > b' ') {
        if input.len() - index > 26 {
            let start = index;
            let end = start + 27;

            return &input[start..end] == b"-----BEGIN PGP MESSAGE-----";
        }
    }

    false
}

/// Validates signatures of Multipart/Signed message part, as defined in RFC 1847.
///
/// Returns the signed part and the set of key
/// fingerprints for which there is a valid signature.
///
/// Returns None if the message is not Multipart/Signed or doesn't contain necessary parts.
pub(crate) fn validate_detached_signature<'a, 'b>(
    mail: &'a ParsedMail<'b>,
    public_keyring_for_validate: &[SignedPublicKey],
) -> Option<(&'a ParsedMail<'b>, HashSet<Fingerprint>)> {
    if mail.ctype.mimetype != "multipart/signed" {
        return None;
    }

    if let [first_part, second_part] = &mail.subparts[..] {
        // First part is the content, second part is the signature.
        let content = first_part.raw_bytes;
        let ret_valid_signatures = match second_part.get_body_raw() {
            Ok(signature) => pgp::pk_validate(content, &signature, public_keyring_for_validate)
                .unwrap_or_default(),
            Err(_) => Default::default(),
        };
        Some((first_part, ret_valid_signatures))
    } else {
        None
    }
}

/// Returns public keyring for `peerstate`.
pub(crate) fn keyring_from_peerstate(peerstate: Option<&Peerstate>) -> Vec<SignedPublicKey> {
    let mut public_keyring_for_validate = Vec::new();
    if let Some(peerstate) = peerstate {
        if let Some(key) = &peerstate.public_key {
            public_keyring_for_validate.push(key.clone());
        } else if let Some(key) = &peerstate.gossip_key {
            public_keyring_for_validate.push(key.clone());
        }
    }
    public_keyring_for_validate
}

/// Applies Autocrypt header to Autocrypt peer state and saves it into the database.
///
/// If we already know this fingerprint from another contact's peerstate, return that
/// peerstate in order to make AEAP work, but don't save it into the db yet.
///
/// Returns updated peerstate.
pub(crate) async fn get_autocrypt_peerstate(
    context: &Context,
    from: &str,
    autocrypt_header: Option<&Aheader>,
    message_time: i64,
    allow_aeap: bool,
) -> Result<Option<Peerstate>> {
    let allow_change = !context.is_self_addr(from).await?;
    let mut peerstate;

    // Apply Autocrypt header
    if let Some(header) = autocrypt_header {
        if allow_aeap {
            // If we know this fingerprint from another addr,
            // we may want to do a transition from this other addr
            // (and keep its peerstate)
            // For security reasons, for now, we only do a transition
            // if the fingerprint is verified.
            peerstate = Peerstate::from_verified_fingerprint_or_addr(
                context,
                &header.public_key.fingerprint(),
                from,
            )
            .await?;
        } else {
            peerstate = Peerstate::from_addr(context, from).await?;
        }

        if let Some(ref mut peerstate) = peerstate {
            if addr_cmp(&peerstate.addr, from) {
                if allow_change {
                    peerstate.apply_header(header, message_time);
                    peerstate.save_to_db(&context.sql).await?;
                } else {
                    info!(
                        context,
                        "Refusing to update existing peerstate of {}", &peerstate.addr
                    );
                }
            }
            // If `peerstate.addr` and `from` differ, this means that
            // someone is using the same key but a different addr, probably
            // because they made an AEAP transition.
            // But we don't know if that's legit until we checked the
            // signatures, so wait until then with writing anything
            // to the database.
        } else {
            let p = Peerstate::from_header(header, message_time);
            p.save_to_db(&context.sql).await?;
            peerstate = Some(p);
        }
    } else {
        peerstate = Peerstate::from_addr(context, from).await?;
    }

    Ok(peerstate)
}

