//! Parsing and handling of the Authentication-Results header.
//! See the comment on [`handle_authres`] for more.

use std::borrow::Cow;
use std::collections::BTreeSet;
use std::fmt;

use anyhow::Result;
use deltachat_contact_tools::EmailAddress;
use mailparse::MailHeaderMap;
use mailparse::ParsedMail;
use once_cell::sync::Lazy;

use crate::config::Config;
use crate::context::Context;
use crate::headerdef::HeaderDef;

/// `authres` is short for the Authentication-Results header, defined in
/// <https://datatracker.ietf.org/doc/html/rfc8601>, which contains info
/// about whether DKIM and SPF passed.
///
/// To mitigate From forgery, we remember for each sending domain whether it is known
/// to have valid DKIM. If an email from such a domain comes with invalid DKIM,
/// we don't allow changing the autocrypt key.
///
/// See <https://github.com/deltachat/deltachat-core-rust/issues/3507>.
pub(crate) async fn handle_authres(
    context: &Context,
    mail: &ParsedMail<'_>,
    from: &str,
) -> Result<DkimResults> {
    let from_domain = match EmailAddress::new(from) {
        Ok(email) => email.domain,
        Err(e) => {
            return Err(anyhow::format_err!("invalid email {}: {:#}", from, e));
        }
    };

    let authres = parse_authres_headers(&mail.get_headers(), &from_domain);
    update_authservid_candidates(context, &authres).await?;
    compute_dkim_results(context, authres).await
}

#[derive(Debug)]
pub(crate) struct DkimResults {
    /// Whether DKIM passed for this particular e-mail.
    pub dkim_passed: bool,
}

impl fmt::Display for DkimResults {
    fn fmt(&self, fmt: &mut fmt::Formatter) -> fmt::Result {
        write!(fmt, "DKIM Results: Passed={}", self.dkim_passed)?;
        Ok(())
    }
}

type AuthservId = String;

#[derive(Debug, PartialEq)]
enum DkimResult {
    /// The header explicitly said that DKIM passed
    Passed,
    /// The header explicitly said that DKIM failed
    Failed,
    /// The header didn't say anything about DKIM; this might mean that it wasn't
    /// checked, but it might also mean that it failed. This is because some providers
    /// (e.g. ik.me, mail.ru, posteo.de) don't add `dkim=none` to their
    /// Authentication-Results if there was no DKIM.
    Nothing,
}

type ParsedAuthresHeaders = Vec<(AuthservId, DkimResult)>;

fn parse_authres_headers(
    headers: &mailparse::headers::Headers<'_>,
    from_domain: &str,
) -> ParsedAuthresHeaders {
    let mut res = Vec::new();
    for header_value in headers.get_all_values(HeaderDef::AuthenticationResults.into()) {
        let header_value = remove_comments(&header_value);

        if let Some(mut authserv_id) = header_value.split(';').next() {
            if authserv_id.contains(char::is_whitespace) || authserv_id.is_empty() {
                // Outlook violates the RFC by not adding an authserv-id at all, which we notice
                // because there is whitespace in the first identifier before the ';'.
                // Authentication-Results-parsing still works securely because they remove incoming
                // Authentication-Results headers.
                // We just use an arbitrary authserv-id, it will work for Outlook, and in general,
                // with providers not implementing the RFC correctly, someone can trick us
                // into thinking that an incoming email is DKIM-correct, anyway.
                // The most important thing here is that we have some valid `authserv_id`.
                authserv_id = "invalidAuthservId";
            }
            let dkim_passed = parse_one_authres_header(&header_value, from_domain);
            res.push((authserv_id.to_string(), dkim_passed));
        }
    }

    res
}

/// The headers can contain comments that look like this:
/// ```text
/// Authentication-Results: (this is a comment) gmx.net; (another; comment) dkim=pass;
/// ```
fn remove_comments(header: &str) -> Cow<'_, str> {
    // In Pomsky, this is:
    //     "(" Codepoint* lazy ")"
    // See https://playground.pomsky-lang.org/?text=%22(%22%20Codepoint*%20lazy%20%22)%22
    static RE: Lazy<regex::Regex> = Lazy::new(|| regex::Regex::new(r"\([\s\S]*?\)").unwrap());

    RE.replace_all(header, " ")
}

/// Parses a single Authentication-Results header, like:
///
/// ```text
/// Authentication-Results:  gmx.net; dkim=pass header.i=@slack.com
/// ```
fn parse_one_authres_header(header_value: &str, from_domain: &str) -> DkimResult {
    if let Some((before_dkim_part, dkim_to_end)) = header_value.split_once("dkim=") {
        // Check that the character right before `dkim=` is a space or a tab
        // so that we wouldn't e.g. mistake `notdkim=pass` for `dkim=pass`
        if before_dkim_part.ends_with(' ') || before_dkim_part.ends_with('\t') {
            let dkim_part = dkim_to_end.split(';').next().unwrap_or_default();
            let dkim_parts: Vec<_> = dkim_part.split_whitespace().collect();
            if let Some(&"pass") = dkim_parts.first() {
                // DKIM headers contain a header.d or header.i field
                // that says which domain signed. We have to check ourselves
                // that this is the same domain as in the From header.
                let header_d: &str = &format!("header.d={}", &from_domain);
                let header_i: &str = &format!("header.i=@{}", &from_domain);

                if dkim_parts.contains(&header_d) || dkim_parts.contains(&header_i) {
                    // We have found a `dkim=pass` header!
                    return DkimResult::Passed;
                }
            } else {
                // dkim=fail, dkim=none, ...
                return DkimResult::Failed;
            }
        }
    }

    DkimResult::Nothing
}

/// ## About authserv-ids
///
/// After having checked DKIM, our email server adds an Authentication-Results header.
///
/// Now, an attacker could just add an Authentication-Results header that says dkim=pass
/// in order to make us think that DKIM was correct in their From-forged email.
///
/// In order to prevent this, each email server adds its authserv-id to the
/// Authentication-Results header, e.g. Testrun's authserv-id is `testrun.org`, Gmail's
/// is `mx.google.com`. When Testrun gets a mail delivered from outside, it will then
/// remove any Authentication-Results headers whose authserv-id is also `testrun.org`.
///
/// We need to somehow find out the authserv-id(s) of our email server, so that
/// we can use the Authentication-Results with the right authserv-id.
///
/// ## What this function does
///
/// When receiving an email, this function is called and updates the candidates for
/// our server's authserv-id, i.e. what we think our server's authserv-id is.
///
/// Usually, every incoming email has Authentication-Results  with our server's
/// authserv-id, so, the intersection of the existing authserv-ids and the incoming
/// authserv-ids for our server's authserv-id is a good guess for our server's
/// authserv-id. When this intersection is empty, we assume that the authserv-id has
/// changed and start over with the new authserv-ids.
///
/// See [`handle_authres`].
async fn update_authservid_candidates(
    context: &Context,
    authres: &ParsedAuthresHeaders,
) -> Result<()> {
    let mut new_ids: BTreeSet<&str> = authres
        .iter()
        .map(|(authserv_id, _dkim_passed)| authserv_id.as_str())
        .collect();
    if new_ids.is_empty() {
        // The incoming message doesn't contain any authentication results, maybe it's a
        // self-sent or a mailer-daemon message
        return Ok(());
    }

    let old_config = context.get_config(Config::AuthservIdCandidates).await?;
    let old_ids = parse_authservid_candidates_config(&old_config);
    let intersection: BTreeSet<&str> = old_ids.intersection(&new_ids).copied().collect();
    if !intersection.is_empty() {
        new_ids = intersection;
    }
    // If there were no AuthservIdCandidates previously, just start with
    // the ones from the incoming email

    if old_ids != new_ids {
        let new_config = new_ids.into_iter().collect::<Vec<_>>().join(" ");
        context
            .set_config_internal(Config::AuthservIdCandidates, Some(&new_config))
            .await?;
    }
    Ok(())
}

/// Use the parsed authres and the authservid candidates to compute whether DKIM passed
/// and whether a keychange should be allowed.
///
/// We track in the `sending_domains` table whether we get positive Authentication-Results
/// for mails from a contact (meaning that their provider properly authenticates against
/// our provider).
///
/// Once a contact is known to come with positive Authentication-Resutls (dkim: pass),
/// we don't accept Autocrypt key changes if they come with negative Authentication-Results.
async fn compute_dkim_results(
    context: &Context,
    mut authres: ParsedAuthresHeaders,
) -> Result<DkimResults> {
    let mut dkim_passed = false;

    let ids_config = context.get_config(Config::AuthservIdCandidates).await?;
    let ids = parse_authservid_candidates_config(&ids_config);

    // Remove all foreign authentication results
    authres.retain(|(authserv_id, _dkim_passed)| ids.contains(authserv_id.as_str()));

    if authres.is_empty() {
        // If the authentication results are empty, then our provider doesn't add them
        // and an attacker could just add their own Authentication-Results, making us
        // think that DKIM passed. So, in this case, we can as well assume that DKIM passed.
        dkim_passed = true;
    } else {
        for (_authserv_id, current_dkim_passed) in authres {
            match current_dkim_passed {
                DkimResult::Passed => {
                    dkim_passed = true;
                    break;
                }
                DkimResult::Failed => {
                    dkim_passed = false;
                    break;
                }
                DkimResult::Nothing => {
                    // Continue looking for an Authentication-Results header
                }
            }
        }
    }

    Ok(DkimResults { dkim_passed })
}

fn parse_authservid_candidates_config(config: &Option<String>) -> BTreeSet<&str> {
    config
        .as_deref()
        .map(|c| c.split_whitespace().collect())
        .unwrap_or_default()
}

