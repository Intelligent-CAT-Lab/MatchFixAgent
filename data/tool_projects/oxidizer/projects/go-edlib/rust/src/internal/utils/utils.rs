#![allow(unused_imports)]
use anyhow::Context;
use anyhow::Error;
use anyhow::Result;
use anyhow::anyhow;

//Translated from: github.com/hbollon/go-edlib/internal/utils.Equal
pub fn equal(a: &[char], b: &[char]) -> Result<bool> {
    if a.len() != b.len() {
        return Ok(false);
    }

    for (i, v) in a.iter().enumerate() {
        if v != &b[i] {
            return Ok(false);
        }
    }

    Ok(true)
}

//Translated from: github.com/hbollon/go-edlib/internal/utils.Min
pub fn min(a: i32, b: i32) -> i32 {
    if b < a {
        b
    } else {
        a
    }
}

//Translated from: github.com/hbollon/go-edlib/internal/utils.Max
pub fn max(a: i32, b: i32) -> i32 {
    if b > a {
        b
    } else {
        a
    }
}
