//! Variable server parameters lists

use crate::provider::{Protocol, Socket};

/// Set of variable parameters to try during configuration.
///
/// Can be loaded from offline provider database, online configuration
/// or derived from user entered parameters.
#[derive(Debug, Clone, PartialEq)]
pub(crate) struct ServerParams {
    /// Protocol, such as IMAP or SMTP.
    pub protocol: Protocol,

    /// Server hostname, empty if unknown.
    pub hostname: String,

    /// Server port, zero if unknown.
    pub port: u16,

    /// Socket security, such as TLS or STARTTLS, Socket::Automatic if unknown.
    pub socket: Socket,

    /// Username, empty if unknown.
    pub username: String,

    /// Whether TLS certificates should be strictly checked or not, `None` for automatic.
    pub strict_tls: Option<bool>,
}

impl ServerParams {
    fn expand_usernames(self, addr: &str) -> Vec<ServerParams> {
        let mut res = Vec::new();

        if self.username.is_empty() {
            res.push(Self {
                username: addr.to_string(),
                ..self.clone()
            });

            if let Some(at) = addr.find('@') {
                res.push(Self {
                    username: addr.split_at(at).0.to_string(),
                    ..self
                });
            }
        } else {
            res.push(self)
        }
        res
    }

    fn expand_hostnames(self, param_domain: &str) -> Vec<ServerParams> {
        if self.hostname.is_empty() {
            vec![
                // Try "imap.ex.org"/"smtp.ex.org" and "mail.ex.org" first because if a server exists
                // under this address, it's likely the correct one.
                Self {
                    hostname: match self.protocol {
                        Protocol::Imap => "imap.".to_string() + param_domain,
                        Protocol::Smtp => "smtp.".to_string() + param_domain,
                    },
                    ..self.clone()
                },
                Self {
                    hostname: "mail.".to_string() + param_domain,
                    ..self.clone()
                },
                // Try "ex.org" last because if it's wrong and the server is configured to
                // not answer at all, configuration may be stuck for several minutes.
                Self {
                    hostname: param_domain.to_string(),
                    ..self
                },
            ]
        } else {
            vec![self]
        }
    }

    fn expand_ports(mut self) -> Vec<ServerParams> {
        // Try to infer port from socket security.
        if self.port == 0 {
            self.port = match self.socket {
                Socket::Ssl => match self.protocol {
                    Protocol::Imap => 993,
                    Protocol::Smtp => 465,
                },
                Socket::Starttls | Socket::Plain => match self.protocol {
                    Protocol::Imap => 143,
                    Protocol::Smtp => 587,
                },
                Socket::Automatic => 0,
            }
        }

        if self.port == 0 {
            // Neither port nor security is set.
            //
            // Try common secure combinations.

            vec![
                // Try TLS
                Self {
                    socket: Socket::Ssl,
                    port: match self.protocol {
                        Protocol::Imap => 993,
                        Protocol::Smtp => 465,
                    },
                    ..self.clone()
                },
                // Try STARTTLS
                Self {
                    socket: Socket::Starttls,
                    port: match self.protocol {
                        Protocol::Imap => 143,
                        Protocol::Smtp => 587,
                    },
                    ..self
                },
            ]
        } else if self.socket == Socket::Automatic {
            vec![
                // Try TLS over user-provided port.
                Self {
                    socket: Socket::Ssl,
                    ..self.clone()
                },
                // Try STARTTLS over user-provided port.
                Self {
                    socket: Socket::Starttls,
                    ..self
                },
            ]
        } else {
            vec![self]
        }
    }

    fn expand_strict_tls(self) -> Vec<ServerParams> {
        vec![Self {
            // Strict if not set by the user or provider database.
            strict_tls: Some(self.strict_tls.unwrap_or(true)),
            ..self
        }]
    }
}

/// Expands vector of `ServerParams`, replacing placeholders with
/// variants to try.
pub(crate) fn expand_param_vector(
    v: Vec<ServerParams>,
    addr: &str,
    domain: &str,
) -> Vec<ServerParams> {
    v.into_iter()
        // The order of expansion is important.
        //
        // Ports are expanded the last, so they are changed the first.  Username is only changed if
        // default value (address with domain) didn't work for all available hosts and ports.
        .flat_map(|params| params.expand_strict_tls().into_iter())
        .flat_map(|params| params.expand_usernames(addr).into_iter())
        .flat_map(|params| params.expand_hostnames(domain).into_iter())
        .flat_map(|params| params.expand_ports().into_iter())
        .collect()
}
