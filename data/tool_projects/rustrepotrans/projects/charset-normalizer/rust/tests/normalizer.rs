use assert_cmd::Command;
use predicates::prelude::*;
use std::ffi::OsString;
use std::fs;
use std::path::PathBuf;

fn get_sample_path(sample_name: &str) -> OsString {
    let mut path = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    path.push(format!("src/tests/data/samples/{}", sample_name));
    path.as_os_str().to_os_string()
}

