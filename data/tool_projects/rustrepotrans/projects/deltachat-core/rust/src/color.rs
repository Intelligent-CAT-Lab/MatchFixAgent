//! Implementation of Consistent Color Generation.
//!
//! Consistent Color Generation is defined in XEP-0392.
//!
//! Color Vision Deficiency correction is not implemented as Delta Chat does not offer
//! corresponding settings.
use hsluv::hsluv_to_rgb;
use sha1::{Digest, Sha1};

/// Converts an identifier to Hue angle.
fn str_to_angle(s: &str) -> f64 {
    let bytes = s.as_bytes();
    let result = Sha1::digest(bytes);
    let checksum: u16 = result.first().map_or(0, |&x| u16::from(x))
        + 256 * result.get(1).map_or(0, |&x| u16::from(x));
    f64::from(checksum) / 65536.0 * 360.0
}

/// Converts RGB tuple to a 24-bit number.
///
/// Returns a 24-bit number with 8 least significant bits corresponding to the blue color and 8
/// most significant bits corresponding to the red color.
fn rgb_to_u32((r, g, b): (f64, f64, f64)) -> u32 {
    let r = ((r * 256.0) as u32).min(255);
    let g = ((g * 256.0) as u32).min(255);
    let b = ((b * 256.0) as u32).min(255);
    65536 * r + 256 * g + b
}

/// Converts an identifier to RGB color.
///
/// Saturation is set to maximum (100.0) to make colors distinguishable, and lightness is set to
/// half (50.0) to make colors suitable both for light and dark theme.
pub fn str_to_color(s: &str) -> u32 {
    rgb_to_u32(hsluv_to_rgb((str_to_angle(s), 100.0, 50.0)))
}

/// Returns color as a "#RRGGBB" `String` where R, G, B are hex digits.
pub fn color_int_to_hex_string(color: u32) -> String {
    format!("{color:#08x}").replace("0x", "#")
}
