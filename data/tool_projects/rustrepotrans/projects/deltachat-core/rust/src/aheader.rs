//! # Autocrypt header module.
//!
//! Parse and create [Autocrypt-headers](https://autocrypt.org/en/latest/level1.html#the-autocrypt-header).

use std::collections::BTreeMap;
use std::fmt;
use std::str::FromStr;

use anyhow::{bail, Context as _, Error, Result};

use crate::key::{DcKey, SignedPublicKey};

/// Possible values for encryption preference
#[derive(PartialEq, Eq, Debug, Default, Clone, Copy, FromPrimitive, ToPrimitive)]
#[repr(u8)]
pub enum EncryptPreference {
    #[default]
    NoPreference = 0,
    Mutual = 1,
    Reset = 20,
}

impl fmt::Display for EncryptPreference {
    fn fmt(&self, fmt: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            EncryptPreference::Mutual => write!(fmt, "mutual"),
            EncryptPreference::NoPreference => write!(fmt, "nopreference"),
            EncryptPreference::Reset => write!(fmt, "reset"),
        }
    }
}

impl FromStr for EncryptPreference {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self> {
        match s {
            "mutual" => Ok(EncryptPreference::Mutual),
            "nopreference" => Ok(EncryptPreference::NoPreference),
            _ => bail!("Cannot parse encryption preference {}", s),
        }
    }
}

/// Autocrypt header
#[derive(Debug)]
pub struct Aheader {
    pub addr: String,
    pub public_key: SignedPublicKey,
    pub prefer_encrypt: EncryptPreference,
}

impl Aheader {
    /// Creates new autocrypt header
    pub fn new(
        addr: String,
        public_key: SignedPublicKey,
        prefer_encrypt: EncryptPreference,
    ) -> Self {
        Aheader {
            addr,
            public_key,
            prefer_encrypt,
        }
    }
}

impl fmt::Display for Aheader {
    fn fmt(&self, fmt: &mut fmt::Formatter) -> fmt::Result {
        write!(fmt, "addr={};", self.addr.to_lowercase())?;
        if self.prefer_encrypt == EncryptPreference::Mutual {
            write!(fmt, " prefer-encrypt=mutual;")?;
        }

        // adds a whitespace every 78 characters, this allows
        // email crate to wrap the lines according to RFC 5322
        // (which may insert a linebreak before every whitespace)
        let keydata = self.public_key.to_base64().chars().enumerate().fold(
            String::new(),
            |mut res, (i, c)| {
                if i % 78 == 78 - "keydata=".len() {
                    res.push(' ')
                }
                res.push(c);
                res
            },
        );
        write!(fmt, " keydata={keydata}")
    }
}

impl FromStr for Aheader {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self> {
        let mut attributes: BTreeMap<String, String> = s
            .split(';')
            .filter_map(|a| {
                let attribute: Vec<&str> = a.trim().splitn(2, '=').collect();
                match &attribute[..] {
                    [key, value] => Some((key.trim().to_string(), value.trim().to_string())),
                    _ => None,
                }
            })
            .collect();

        let addr = match attributes.remove("addr") {
            Some(addr) => addr,
            None => bail!("Autocrypt header has no addr"),
        };
        let public_key: SignedPublicKey = attributes
            .remove("keydata")
            .context("keydata attribute is not found")
            .and_then(|raw| {
                SignedPublicKey::from_base64(&raw).context("autocrypt key cannot be decoded")
            })
            .and_then(|key| {
                key.verify()
                    .and(Ok(key))
                    .context("autocrypt key cannot be verified")
            })?;

        let prefer_encrypt = attributes
            .remove("prefer-encrypt")
            .and_then(|raw| raw.parse().ok())
            .unwrap_or_default();

        // Autocrypt-Level0: unknown attributes starting with an underscore can be safely ignored
        // Autocrypt-Level0: unknown attribute, treat the header as invalid
        if attributes.keys().any(|k| !k.starts_with('_')) {
            bail!("Unknown Autocrypt attribute found");
        }

        Ok(Aheader {
            addr,
            public_key,
            prefer_encrypt,
        })
    }
}
