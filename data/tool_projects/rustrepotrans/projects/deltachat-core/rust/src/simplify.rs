//! # Simplify incoming plaintext.

/// Protects lines starting with `--` against being treated as a footer.
/// for that, we insert a ZERO WIDTH SPACE (ZWSP, 0x200B);
/// this should be invisible on most systems and there is no need to unescape it again
/// (which won't be done by non-deltas anyway).
///
/// This escapes a bit more than actually needed by delta (e.g. also lines as "-- footer"),
/// but for non-delta-compatibility, that seems to be better.
/// (to be only compatible with delta, only "[\r\n|\n]-- {0,2}[\r\n|\n]" needs to be replaced)
pub fn escape_message_footer_marks(text: &str) -> String {
    if let Some(text) = text.strip_prefix("--") {
        "-\u{200B}-".to_string() + &text.replace("\n--", "\n-\u{200B}-")
    } else {
        text.replace("\n--", "\n-\u{200B}-")
    }
}

/// Remove standard (RFC 3676, §4.3) footer if it is found.
/// Returns `(lines, footer_lines)` tuple;
/// `footer_lines` is set to `Some` if the footer was actually removed from `lines`
/// (which is equal to the input array otherwise).
#[allow(clippy::indexing_slicing)]
fn remove_message_footer<'a>(lines: &'a [&str]) -> (&'a [&'a str], Option<&'a [&'a str]>) {
    let mut nearly_standard_footer = None;
    for (ix, &line) in lines.iter().enumerate() {
        match line {
            // some providers encode `-- ` to `-- =20` which results in `--  `
            "-- " | "--  " => return (&lines[..ix], lines.get(ix + 1..)),
            // some providers encode `-- ` to `=2D-` which results in only `--`;
            // use that only when no other footer is found
            // and if the line before is empty and the line after is not empty
            "--" => {
                if (ix == 0 || lines[ix - 1].is_empty())
                    && ix != lines.len() - 1
                    && !lines[ix + 1].is_empty()
                {
                    nearly_standard_footer = Some(ix);
                }
            }
            _ => (),
        }
    }
    if let Some(ix) = nearly_standard_footer {
        return (&lines[..ix], lines.get(ix + 1..));
    }
    (lines, None)
}

/// Remove nonstandard footer and a boolean indicating whether such footer was removed.
/// Returns `(lines, is_footer_removed)` tuple;
/// `is_footer_removed` is set to `true` if the footer was actually removed from `lines`
/// (which is equal to the input array otherwise).
#[allow(clippy::indexing_slicing)]
fn remove_nonstandard_footer<'a>(lines: &'a [&str]) -> (&'a [&'a str], bool) {
    for (ix, &line) in lines.iter().enumerate() {
        if line == "--"
            || line.starts_with("---")
            || line.starts_with("_____")
            || line.starts_with("=====")
            || line.starts_with("*****")
            || line.starts_with("~~~~~")
        {
            return (&lines[..ix], true);
        }
    }
    (lines, false)
}

/// Remove footers if any.
/// This also makes all newlines "\n", but why not.
pub(crate) fn remove_footers(msg: &str) -> String {
    let lines = split_lines(msg);
    let lines = remove_message_footer(&lines).0;
    let lines = remove_nonstandard_footer(lines).0;
    lines.join("\n")
}

pub(crate) fn split_lines(buf: &str) -> Vec<&str> {
    buf.split('\n').collect()
}

/// Simplified text and some additional information gained from the input.
#[derive(Debug, Default, PartialEq, Eq)]
pub(crate) struct SimplifiedText {
    /// The text itself.
    pub text: String,

    /// True if the message is forwarded.
    pub is_forwarded: bool,

    /// True if nonstandard footer was removed
    /// or if the message contains quotes other than `top_quote`.
    pub is_cut: bool,

    /// Top quote, if any.
    pub top_quote: Option<String>,

    /// Footer, if any.
    pub footer: Option<String>,
}

pub(crate) fn simplify_quote(quote: &str) -> (String, bool) {
    let quote_lines = split_lines(quote);
    let (quote_lines, quote_footer_lines) = remove_message_footer(&quote_lines);
    let is_cut = quote_footer_lines.is_some();

    (render_message(quote_lines, false), is_cut)
}

/// Simplify message text for chat display.
/// Remove quotes, signatures, trailing empty lines etc.
pub(crate) fn simplify(mut input: String, is_chat_message: bool) -> SimplifiedText {
    let mut is_cut = false;

    input.retain(|c| c != '\r');
    let lines = split_lines(&input);
    let (lines, is_forwarded) = skip_forward_header(&lines);

    let (lines, mut top_quote) = remove_top_quote(lines);
    let original_lines = &lines;
    let (lines, footer_lines) = remove_message_footer(lines);
    let footer = footer_lines.map(|footer_lines| render_message(footer_lines, false));

    let text = if is_chat_message {
        render_message(lines, false)
    } else {
        let (lines, has_nonstandard_footer) = remove_nonstandard_footer(lines);
        let (lines, mut bottom_quote) = remove_bottom_quote(lines);

        if top_quote.is_none() && bottom_quote.is_some() {
            std::mem::swap(&mut top_quote, &mut bottom_quote);
        }

        if lines.iter().all(|it| it.trim().is_empty()) {
            render_message(original_lines, false)
        } else {
            is_cut = is_cut || has_nonstandard_footer || bottom_quote.is_some();
            render_message(lines, has_nonstandard_footer || bottom_quote.is_some())
        }
    };

    if !is_chat_message {
        top_quote = top_quote.map(|quote| {
            let (quote, quote_cut) = simplify_quote(&quote);
            is_cut |= quote_cut;
            quote
        });
    }

    SimplifiedText {
        text,
        is_forwarded,
        is_cut,
        top_quote,
        footer,
    }
}

/// Skips "forwarded message" header.
/// Returns message body lines and a boolean indicating whether
/// a message is forwarded or not.
fn skip_forward_header<'a>(lines: &'a [&str]) -> (&'a [&'a str], bool) {
    match lines {
        ["---------- Forwarded message ----------", first_line, "", rest @ ..]
            if first_line.starts_with("From: ") =>
        {
            (rest, true)
        }
        _ => (lines, false),
    }
}

#[allow(clippy::indexing_slicing)]
fn remove_bottom_quote<'a>(lines: &'a [&str]) -> (&'a [&'a str], Option<String>) {
    let mut first_quoted_line = lines.len();
    let mut last_quoted_line = None;
    for (l, line) in lines.iter().enumerate().rev() {
        if is_plain_quote(line) {
            if last_quoted_line.is_none() {
                first_quoted_line = l + 1;
            }
            last_quoted_line = Some(l)
        } else if !is_empty_line(line) {
            break;
        }
    }
    if let Some(mut l_last) = last_quoted_line {
        let quoted_text = lines[l_last..first_quoted_line]
            .iter()
            .map(|s| {
                s.strip_prefix('>')
                    .map_or(*s, |u| u.strip_prefix(' ').unwrap_or(u))
            })
            .collect::<Vec<&str>>()
            .join("\n");
        if l_last > 1 && is_empty_line(lines[l_last - 1]) {
            l_last -= 1
        }
        if l_last > 1 {
            let line = lines[l_last - 1];
            if is_quoted_headline(line) {
                l_last -= 1
            }
        }
        (&lines[..l_last], Some(quoted_text))
    } else {
        (lines, None)
    }
}

#[allow(clippy::indexing_slicing)]
fn remove_top_quote<'a>(lines: &'a [&str]) -> (&'a [&'a str], Option<String>) {
    let mut first_quoted_line = 0;
    let mut last_quoted_line = None;
    let mut has_quoted_headline = false;
    for (l, line) in lines.iter().enumerate() {
        if is_plain_quote(line) {
            if last_quoted_line.is_none() {
                first_quoted_line = l;
            }
            last_quoted_line = Some(l)
        } else if is_quoted_headline(line) && !has_quoted_headline && last_quoted_line.is_none() {
            has_quoted_headline = true
        } else {
            /* non-quoting line found */
            break;
        }
    }
    if let Some(last_quoted_line) = last_quoted_line {
        (
            &lines[last_quoted_line + 1..],
            Some(
                lines[first_quoted_line..last_quoted_line + 1]
                    .iter()
                    .map(|s| {
                        s.strip_prefix('>')
                            .map_or(*s, |u| u.strip_prefix(' ').unwrap_or(u))
                    })
                    .collect::<Vec<&str>>()
                    .join("\n"),
            ),
        )
    } else {
        (lines, None)
    }
}

fn render_message(lines: &[&str], is_cut_at_end: bool) -> String {
    let mut ret = String::new();
    /* we write empty lines only in case and non-empty line follows */
    let mut pending_linebreaks = 0;
    for line in lines {
        if is_empty_line(line) {
            pending_linebreaks += 1
        } else {
            if !ret.is_empty() {
                if pending_linebreaks > 2 {
                    pending_linebreaks = 2
                }
                while 0 != pending_linebreaks {
                    ret += "\n";
                    pending_linebreaks -= 1
                }
            }
            // the incoming message might contain invalid UTF8
            ret += line;
            pending_linebreaks = 1
        }
    }
    if is_cut_at_end && !ret.is_empty() {
        ret += " [...]";
    }
    // redo escaping done by escape_message_footer_marks()
    ret.replace('\u{200B}', "")
}

/// Returns true if the line contains only whitespace.
fn is_empty_line(buf: &str) -> bool {
    buf.chars().all(char::is_whitespace)
    // for some time, this checked for `char <= ' '`,
    // see discussion at: <https://github.com/deltachat/deltachat-core-rust/pull/402#discussion_r317062392>
    // and <https://github.com/deltachat/deltachat-core-rust/pull/2104/files#r538973613>
}

fn is_quoted_headline(buf: &str) -> bool {
    /* This function may be called for the line _directly_ before a quote.
    The function checks if the line contains sth. like "On 01.02.2016, xy@z wrote:" in various languages.
    - Currently, we simply check if the last character is a ':'.
    - Checking for the existence of an email address may fail (headlines may show the user's name instead of the address) */

    buf.len() <= 80 && buf.ends_with(':')
}

fn is_plain_quote(buf: &str) -> bool {
    buf.starts_with('>')
}
