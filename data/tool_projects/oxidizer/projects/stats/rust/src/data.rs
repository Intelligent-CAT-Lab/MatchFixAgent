#![allow(unused_imports)]
use anyhow::Context;
use anyhow::Error;
use anyhow::Result;
use anyhow::anyhow;

//Translated from: github.com/montanaflynn/stats.Float64Data
#[derive(derive_more::From, derive_more::Into)]
#[derive(Default)]#[derive(Clone)]pub struct Float64Data(pub Vec<f64>);


//Translated from: (github.com/montanaflynn/stats.Float64Data).Get
impl Float64Data {
    pub fn get(&self, i: usize) -> f64 {
        self.0[i]
    }
}

//Translated from: (github.com/montanaflynn/stats.Float64Data).Len
impl Float64Data {
    pub fn len(&self) -> usize {
        self.0.len()
    }
}
use crate::sum::sum;
//Translated from: (github.com/montanaflynn/stats.Float64Data).Sum
impl Float64Data {
    pub fn sum(&self) -> Result<f64, Error> {
        sum(self.clone())
    }
}
