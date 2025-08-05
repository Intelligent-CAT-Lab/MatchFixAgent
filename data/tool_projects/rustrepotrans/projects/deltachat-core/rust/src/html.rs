//! # Get message as HTML.
//!
//! Use `Message.has_html()` to check if the UI shall render a
//! corresponding button and `MsgId.get_html()` to get the full message.
//!
//! Even when the original mime-message is not HTML,
//! `MsgId.get_html()` will return HTML -
//! this allows nice quoting, handling linebreaks properly etc.

use anyhow::{Context as _, Result};
use base64::Engine as _;
use lettre_email::mime::Mime;
use lettre_email::PartBuilder;
use mailparse::ParsedContentType;

use crate::context::Context;
use crate::headerdef::{HeaderDef, HeaderDefMap};
use crate::message::{self, Message, MsgId};
use crate::mimeparser::parse_message_id;
use crate::param::Param::SendHtml;
use crate::plaintext::PlainText;

impl Message {
    /// Check if the message can be retrieved as HTML.
    /// Typically, this is the case, when the mime structure of a Message is modified,
    /// meaning that some text is cut or the original message
    /// is in HTML and `simplify()` may hide some maybe important information.
    /// The corresponding ffi-function is `dc_msg_has_html()`.
    /// To get the HTML-code of the message, use `MsgId.get_html()`.
    pub fn has_html(&self) -> bool {
        self.mime_modified
    }

    /// Set HTML-part part of a message that is about to be sent.
    /// The HTML-part is written to the database before sending and
    /// used as the `text/html` part in the MIME-structure.
    ///
    /// Received HTML parts are handled differently,
    /// they are saved together with the whole MIME-structure
    /// in `mime_headers` and the HTML-part is extracted using `MsgId::get_html()`.
    /// (To underline this asynchronicity, we are using the wording "SendHtml")
    pub fn set_html(&mut self, html: Option<String>) {
        if let Some(html) = html {
            self.param.set(SendHtml, html);
            self.mime_modified = true;
        } else {
            self.param.remove(SendHtml);
            self.mime_modified = false;
        }
    }
}

/// Type defining a rough mime-type.
/// This is mainly useful on iterating
/// to decide whether a mime-part has subtypes.
enum MimeMultipartType {
    Multiple,
    Single,
    Message,
}

/// Function takes a content type from a ParsedMail structure
/// and checks and returns the rough mime-type.
fn get_mime_multipart_type(ctype: &ParsedContentType) -> MimeMultipartType {
    let mimetype = ctype.mimetype.to_lowercase();
    if mimetype.starts_with("multipart") && ctype.params.contains_key("boundary") {
        MimeMultipartType::Multiple
    } else if mimetype == "message/rfc822" {
        MimeMultipartType::Message
    } else {
        MimeMultipartType::Single
    }
}

/// HtmlMsgParser converts a mime-message to HTML.
#[derive(Debug)]
struct HtmlMsgParser {
    pub html: String,
    pub plain: Option<PlainText>,
}

impl HtmlMsgParser {
    /// Function takes a raw mime-message string,
    /// searches for the main-text part
    /// and returns that as parser.html
    pub async fn from_bytes(context: &Context, rawmime: &[u8]) -> Result<Self> {
        let mut parser = HtmlMsgParser {
            html: "".to_string(),
            plain: None,
        };

        let parsedmail = mailparse::parse_mail(rawmime)?;

        parser.collect_texts_recursive(&parsedmail).await?;

        if parser.html.is_empty() {
            if let Some(plain) = &parser.plain {
                parser.html = plain.to_html();
            }
        } else {
            parser.cid_to_data_recursive(context, &parsedmail).await?;
        }

        Ok(parser)
    }

    /// Function iterates over all mime-parts
    /// and searches for text/plain and text/html parts and saves the
    /// first one found.
    /// in the corresponding structure fields.
    ///
    /// Usually, there is at most one plain-text and one HTML-text part,
    /// multiple plain-text parts might be used for mailinglist-footers,
    /// therefore we use the first one.
    async fn collect_texts_recursive<'a>(
        &'a mut self,
        mail: &'a mailparse::ParsedMail<'a>,
    ) -> Result<()> {
        match get_mime_multipart_type(&mail.ctype) {
            MimeMultipartType::Multiple => {
                for cur_data in &mail.subparts {
                    Box::pin(self.collect_texts_recursive(cur_data)).await?
                }
                Ok(())
            }
            MimeMultipartType::Message => {
                let raw = mail.get_body_raw()?;
                if raw.is_empty() {
                    return Ok(());
                }
                let mail = mailparse::parse_mail(&raw).context("failed to parse mail")?;
                Box::pin(self.collect_texts_recursive(&mail)).await
            }
            MimeMultipartType::Single => {
                let mimetype = mail.ctype.mimetype.parse::<Mime>()?;
                if mimetype == mime::TEXT_HTML {
                    if self.html.is_empty() {
                        if let Ok(decoded_data) = mail.get_body() {
                            self.html = decoded_data;
                        }
                    }
                } else if mimetype == mime::TEXT_PLAIN && self.plain.is_none() {
                    if let Ok(decoded_data) = mail.get_body() {
                        self.plain = Some(PlainText {
                            text: decoded_data,
                            flowed: if let Some(format) = mail.ctype.params.get("format") {
                                format.as_str().to_ascii_lowercase() == "flowed"
                            } else {
                                false
                            },
                            delsp: if let Some(delsp) = mail.ctype.params.get("delsp") {
                                delsp.as_str().to_ascii_lowercase() == "yes"
                            } else {
                                false
                            },
                        });
                    }
                }
                Ok(())
            }
        }
    }

    /// Replace cid:-protocol by the data:-protocol where appropriate.
    /// This allows the final html-file to be self-contained.
    async fn cid_to_data_recursive<'a>(
        &'a mut self,
        context: &'a Context,
        mail: &'a mailparse::ParsedMail<'a>,
    ) -> Result<()> {
        match get_mime_multipart_type(&mail.ctype) {
            MimeMultipartType::Multiple => {
                for cur_data in &mail.subparts {
                    Box::pin(self.cid_to_data_recursive(context, cur_data)).await?;
                }
                Ok(())
            }
            MimeMultipartType::Message => {
                let raw = mail.get_body_raw()?;
                if raw.is_empty() {
                    return Ok(());
                }
                let mail = mailparse::parse_mail(&raw).context("failed to parse mail")?;
                Box::pin(self.cid_to_data_recursive(context, &mail)).await
            }
            MimeMultipartType::Single => {
                let mimetype = mail.ctype.mimetype.parse::<Mime>()?;
                if mimetype.type_() == mime::IMAGE {
                    if let Some(cid) = mail.headers.get_header_value(HeaderDef::ContentId) {
                        if let Ok(cid) = parse_message_id(&cid) {
                            if let Ok(replacement) = mimepart_to_data_url(mail) {
                                let re_string = format!(
                                    "(<img[^>]*src[^>]*=[^>]*)(cid:{})([^>]*>)",
                                    regex::escape(&cid)
                                );
                                match regex::Regex::new(&re_string) {
                                    Ok(re) => {
                                        self.html = re
                                            .replace_all(
                                                &self.html,
                                                format!("${{1}}{replacement}${{3}}").as_str(),
                                            )
                                            .as_ref()
                                            .to_string()
                                    }
                                    Err(e) => warn!(
                                        context,
                                        "Cannot create regex for cid: {} throws {}", re_string, e
                                    ),
                                }
                            }
                        }
                    }
                }
                Ok(())
            }
        }
    }
}

/// Convert a mime part to a data: url as defined in [RFC 2397](https://tools.ietf.org/html/rfc2397).
fn mimepart_to_data_url(mail: &mailparse::ParsedMail<'_>) -> Result<String> {
    let data = mail.get_body_raw()?;
    let data = base64::engine::general_purpose::STANDARD.encode(data);
    Ok(format!("data:{};base64,{}", mail.ctype.mimetype, data))
}

impl MsgId {
    /// Get HTML by database message id.
    /// This requires `mime_headers` field to be set for the message;
    /// this is the case at least when `Message.has_html()` returns true
    /// (we do not save raw mime unconditionally in the database to save space).
    /// The corresponding ffi-function is `dc_get_msg_html()`.
    pub async fn get_html(self, context: &Context) -> Result<Option<String>> {
        let rawmime = message::get_mime_headers(context, self).await?;

        if !rawmime.is_empty() {
            match HtmlMsgParser::from_bytes(context, &rawmime).await {
                Err(err) => {
                    warn!(context, "get_html: parser error: {:#}", err);
                    Ok(None)
                }
                Ok(parser) => Ok(Some(parser.html)),
            }
        } else {
            warn!(context, "get_html: no mime for {}", self);
            Ok(None)
        }
    }
}

/// Wraps HTML text into a new text/html mimepart structure.
///
/// Used on forwarding messages to avoid leaking the original mime structure
/// and also to avoid sending too much, maybe large data.
pub fn new_html_mimepart(html: String) -> PartBuilder {
    PartBuilder::new()
        .content_type(&"text/html; charset=utf-8".parse::<mime::Mime>().unwrap())
        .body(html)
}
