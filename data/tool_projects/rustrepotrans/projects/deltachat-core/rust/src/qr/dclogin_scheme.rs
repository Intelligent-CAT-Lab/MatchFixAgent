use std::collections::HashMap;

use anyhow::{bail, Context as _, Result};

use deltachat_contact_tools::may_be_valid_addr;
use num_traits::cast::ToPrimitive;

use super::{Qr, DCLOGIN_SCHEME};
use crate::config::Config;
use crate::context::Context;
use crate::login_param::CertificateChecks;
use crate::provider::Socket;

/// Options for `dclogin:` scheme.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum LoginOptions {
    /// Unsupported version.
    UnsuportedVersion(u32),

    /// Version 1.
    V1 {
        /// IMAP server password.
        ///
        /// Used for SMTP if separate SMTP password is not provided.
        mail_pw: String,

        /// IMAP host.
        imap_host: Option<String>,

        /// IMAP port.
        imap_port: Option<u16>,

        /// IMAP username.
        imap_username: Option<String>,

        /// IMAP password.
        imap_password: Option<String>,

        /// IMAP socket security.
        imap_security: Option<Socket>,

        /// IMAP certificate checks.
        imap_certificate_checks: Option<CertificateChecks>,

        /// SMTP host.
        smtp_host: Option<String>,

        /// SMTP port.
        smtp_port: Option<u16>,

        /// SMTP username.
        smtp_username: Option<String>,

        /// SMTP password.
        smtp_password: Option<String>,

        /// SMTP socket security.
        smtp_security: Option<Socket>,

        /// SMTP certificate checks.
        smtp_certificate_checks: Option<CertificateChecks>,
    },
}

/// scheme: `dclogin://user@host/?p=password&v=1[&options]`
/// read more about the scheme at <https://github.com/deltachat/interface/blob/master/uri-schemes.md#DCLOGIN>
pub(super) fn decode_login(qr: &str) -> Result<Qr> {
    let url = url::Url::parse(qr).with_context(|| format!("Malformed url: {qr:?}"))?;

    let url_without_scheme = qr
        .get(DCLOGIN_SCHEME.len()..)
        .context("invalid DCLOGIN payload E1")?;
    let payload = url_without_scheme
        .strip_prefix("//")
        .unwrap_or(url_without_scheme);

    let addr = payload
        .split(|c| c == '?' || c == '/')
        .next()
        .context("invalid DCLOGIN payload E3")?;

    if url.scheme().eq_ignore_ascii_case("dclogin") {
        let options = url.query_pairs();
        if options.count() == 0 {
            bail!("invalid DCLOGIN payload E4")
        }
        // load options into hashmap
        let parameter_map: HashMap<String, String> = options
            .map(|(key, value)| (key.into_owned(), value.into_owned()))
            .collect();

        // check if username is there
        if !may_be_valid_addr(addr) {
            bail!("invalid DCLOGIN payload: invalid username E5");
        }

        // apply to result struct
        let options: LoginOptions = match parameter_map.get("v").map(|i| i.parse::<u32>()) {
            Some(Ok(1)) => LoginOptions::V1 {
                mail_pw: parameter_map
                    .get("p")
                    .map(|s| s.to_owned())
                    .context("password missing")?,
                imap_host: parameter_map.get("ih").map(|s| s.to_owned()),
                imap_port: parse_port(parameter_map.get("ip"))
                    .context("could not parse imap port")?,
                imap_username: parameter_map.get("iu").map(|s| s.to_owned()),
                imap_password: parameter_map.get("ipw").map(|s| s.to_owned()),
                imap_security: parse_socket_security(parameter_map.get("is"))?,
                imap_certificate_checks: parse_certificate_checks(parameter_map.get("ic"))?,
                smtp_host: parameter_map.get("sh").map(|s| s.to_owned()),
                smtp_port: parse_port(parameter_map.get("sp"))
                    .context("could not parse smtp port")?,
                smtp_username: parameter_map.get("su").map(|s| s.to_owned()),
                smtp_password: parameter_map.get("spw").map(|s| s.to_owned()),
                smtp_security: parse_socket_security(parameter_map.get("ss"))?,
                smtp_certificate_checks: parse_certificate_checks(parameter_map.get("sc"))?,
            },
            Some(Ok(v)) => LoginOptions::UnsuportedVersion(v),
            Some(Err(_)) => bail!("version could not be parsed as number E6"),
            None => bail!("invalid DCLOGIN payload: version missing E7"),
        };

        Ok(Qr::Login {
            address: addr.to_owned(),
            options,
        })
    } else {
        bail!("Bad scheme for account URL: {:?}.", payload);
    }
}

fn parse_port(port: Option<&String>) -> core::result::Result<Option<u16>, std::num::ParseIntError> {
    match port {
        Some(p) => Ok(Some(p.parse::<u16>()?)),
        None => Ok(None),
    }
}

fn parse_socket_security(security: Option<&String>) -> Result<Option<Socket>> {
    Ok(match security.map(|s| s.as_str()) {
        Some("ssl") => Some(Socket::Ssl),
        Some("starttls") => Some(Socket::Starttls),
        Some("default") => Some(Socket::Automatic),
        Some("plain") => Some(Socket::Plain),
        Some(other) => bail!("Unknown security level: {}", other),
        None => None,
    })
}

fn parse_certificate_checks(
    certificate_checks: Option<&String>,
) -> Result<Option<CertificateChecks>> {
    Ok(match certificate_checks.map(|s| s.as_str()) {
        Some("0") => Some(CertificateChecks::Automatic),
        Some("1") => Some(CertificateChecks::Strict),
        Some("3") => Some(CertificateChecks::AcceptInvalidCertificates),
        Some(other) => bail!("Unknown certificatecheck level: {}", other),
        None => None,
    })
}

pub(crate) async fn configure_from_login_qr(
    context: &Context,
    address: &str,
    options: LoginOptions,
) -> Result<()> {
    context
        .set_config_internal(Config::Addr, Some(address))
        .await?;

    match options {
        LoginOptions::V1 {
            mail_pw,
            imap_host,
            imap_port,
            imap_username,
            imap_password,
            imap_security,
            imap_certificate_checks,
            smtp_host,
            smtp_port,
            smtp_username,
            smtp_password,
            smtp_security,
            smtp_certificate_checks,
        } => {
            context
                .set_config_internal(Config::MailPw, Some(&mail_pw))
                .await?;
            if let Some(value) = imap_host {
                context
                    .set_config_internal(Config::MailServer, Some(&value))
                    .await?;
            }
            if let Some(value) = imap_port {
                context
                    .set_config_internal(Config::MailPort, Some(&value.to_string()))
                    .await?;
            }
            if let Some(value) = imap_username {
                context
                    .set_config_internal(Config::MailUser, Some(&value))
                    .await?;
            }
            if let Some(value) = imap_password {
                context
                    .set_config_internal(Config::MailPw, Some(&value))
                    .await?;
            }
            if let Some(value) = imap_security {
                let code = value
                    .to_u8()
                    .context("could not convert imap security value to number")?;
                context
                    .set_config_internal(Config::MailSecurity, Some(&code.to_string()))
                    .await?;
            }
            if let Some(value) = imap_certificate_checks {
                let code = value
                    .to_u32()
                    .context("could not convert imap certificate checks value to number")?;
                context
                    .set_config_internal(Config::ImapCertificateChecks, Some(&code.to_string()))
                    .await?;
            }
            if let Some(value) = smtp_host {
                context
                    .set_config_internal(Config::SendServer, Some(&value))
                    .await?;
            }
            if let Some(value) = smtp_port {
                context
                    .set_config_internal(Config::SendPort, Some(&value.to_string()))
                    .await?;
            }
            if let Some(value) = smtp_username {
                context
                    .set_config_internal(Config::SendUser, Some(&value))
                    .await?;
            }
            if let Some(value) = smtp_password {
                context
                    .set_config_internal(Config::SendPw, Some(&value))
                    .await?;
            }
            if let Some(value) = smtp_security {
                let code = value
                    .to_u8()
                    .context("could not convert smtp security value to number")?;
                context
                    .set_config_internal(Config::SendSecurity, Some(&code.to_string()))
                    .await?;
            }
            if let Some(value) = smtp_certificate_checks {
                let code = value
                    .to_u32()
                    .context("could not convert smtp certificate checks value to number")?;
                context
                    .set_config_internal(Config::SmtpCertificateChecks, Some(&code.to_string()))
                    .await?;
            }
            Ok(())
        }
        _ => bail!(
            "DeltaChat does not understand this QR Code yet, please update the app and try again."
        ),
    }
}

