//! # format=flowed support.
//!
//! Format=flowed is defined in
//! [RFC 3676](https://tools.ietf.org/html/rfc3676).
//!
//! Older [RFC 2646](https://tools.ietf.org/html/rfc2646) is used
//! during formatting, i.e., DelSp parameter introduced in RFC 3676
//! is assumed to be set to "no".
//!
//! For received messages, DelSp parameter is honoured.

/// Wraps line to 72 characters using format=flowed soft breaks.
///
/// 72 characters is the limit recommended by RFC 3676.
///
/// The function breaks line only after SP and before non-whitespace
/// characters. It also does not insert breaks before ">" to avoid the
/// need to do space stuffing (see RFC 3676) for quotes.
///
/// If there are long words, line may still exceed the limits on line
/// length. However, this should be rare and should not result in
/// immediate mail rejection: SMTP (RFC 2821) limit is 998 characters,
/// and Spam Assassin limit is 78 characters.
fn format_line_flowed(line: &str, prefix: &str) -> String {
    let mut result = String::new();
    let mut buffer = prefix.to_string();
    let mut after_space = prefix.ends_with(' ');

    for c in line.chars() {
        if c == ' ' {
            if buffer.is_empty() {
                // Space stuffing, see RFC 3676
                buffer.push(' ');
            }
            buffer.push(c);
            after_space = true;
        } else if c == '>' {
            if buffer.is_empty() {
                // Space stuffing, see RFC 3676
                buffer.push(' ');
            }
            buffer.push(c);
            after_space = false;
        } else {
            if after_space && buffer.len() >= 72 && !c.is_whitespace() {
                // Flush the buffer and insert soft break (SP CRLF).
                result += &buffer;
                result += "\r\n";
                buffer = prefix.to_string();
            }
            buffer.push(c);
            after_space = false;
        }
    }
    result + &buffer
}

/// Returns text formatted according to RFC 3676 (format=flowed).
///
/// This function accepts text separated by LF, but returns text
/// separated by CRLF.
///
/// RFC 2646 technique is used to insert soft line breaks, so DelSp
/// SHOULD be set to "no" when sending.
pub fn format_flowed(text: &str) -> String {
    let mut result = String::new();

    for line in text.split('\n') {
        if !result.is_empty() {
            result += "\r\n";
        }

        let line = line.trim_end();
        let quote_depth = line.chars().take_while(|&c| c == '>').count();
        let (prefix, mut line) = line.split_at(quote_depth);

        let mut prefix = prefix.to_string();

        if quote_depth > 0 {
            if let Some(s) = line.strip_prefix(' ') {
                line = s;
                prefix += " ";
            }
        }

        result += &format_line_flowed(line, &prefix);
    }

    result
}

/// Same as format_flowed(), but adds "> " prefix to each line.
pub fn format_flowed_quote(text: &str) -> String {
    let mut result = String::new();

    for line in text.split('\n') {
        if !result.is_empty() {
            result += "\n";
        }
        result += "> ";
        result += line;
    }

    format_flowed(&result)
}

/// Joins lines in format=flowed text.
///
/// Lines must be separated by single LF.
///
/// Signature separator line is not processed here, it is assumed to
/// be stripped beforehand.
pub fn unformat_flowed(text: &str, delsp: bool) -> String {
    let mut result = String::new();
    let mut skip_newline = true;

    for line in text.split('\n') {
        let line = if !result.is_empty() && skip_newline {
            line.trim_start_matches('>')
        } else {
            line
        };

        // Revert space-stuffing
        let line = line.strip_prefix(' ').unwrap_or(line);

        if !skip_newline {
            result.push('\n');
        }

        if let Some(line) = line.strip_suffix(' ') {
            // Flowed line
            result += line;
            if !delsp {
                result.push(' ');
            }
            skip_newline = true;
        } else {
            // Fixed line
            result += line;
            skip_newline = false;
        }
    }
    result
}

