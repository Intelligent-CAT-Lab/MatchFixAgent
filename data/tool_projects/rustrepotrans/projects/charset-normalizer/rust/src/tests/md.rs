use crate::md::structs::{MessDetectorChar, MessDetectorCharFlags};
use crate::md::*;
use crate::utils::{decode, get_large_test_datasets};
use encoding::DecoderTrap;
use ordered_float::OrderedFloat;
use std::fs::File;
use std::io::Read;

