// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

use super::TransformFunction;
use crate::spec::{Datum, PrimitiveLiteral};
use crate::{Error, ErrorKind, Result};
use arrow_arith::temporal::DatePart;
use arrow_arith::{arity::binary, temporal::date_part};
use arrow_array::{
    types::Date32Type, Array, ArrayRef, Date32Array, Int32Array, TimestampMicrosecondArray,
};
use arrow_schema::{DataType, TimeUnit};
use chrono::{DateTime, Datelike, Duration};
use std::sync::Arc;

/// Hour in one second.
const HOUR_PER_SECOND: f64 = 1.0_f64 / 3600.0_f64;
/// Year of unix epoch.
const UNIX_EPOCH_YEAR: i32 = 1970;
/// One second in micros.
const MICROS_PER_SECOND: i64 = 1_000_000;

/// Extract a date or timestamp year, as years from 1970
#[derive(Debug)]
pub struct Year;

impl Year {
    #[inline]
    fn timestamp_to_year(timestamp: i64) -> Result<i32> {
        Ok(DateTime::from_timestamp_micros(timestamp)
            .ok_or_else(|| {
                Error::new(
                    ErrorKind::DataInvalid,
                    "Fail to convert timestamp to date in year transform",
                )
            })?
            .year()
            - UNIX_EPOCH_YEAR)
    }
}

impl TransformFunction for Year {
    fn transform(&self, input: ArrayRef) -> Result<ArrayRef> {
        let array = date_part(&input, DatePart::Year)
            .map_err(|err| Error::new(ErrorKind::Unexpected, format!("{err}")))?;
        Ok(Arc::<Int32Array>::new(
            array
                .as_any()
                .downcast_ref::<Int32Array>()
                .unwrap()
                .unary(|v| v - UNIX_EPOCH_YEAR),
        ))
    }

    fn transform_literal(&self, input: &crate::spec::Datum) -> Result<Option<crate::spec::Datum>> {
        let val = match input.literal() {
            PrimitiveLiteral::Date(v) => Date32Type::to_naive_date(*v).year() - UNIX_EPOCH_YEAR,
            PrimitiveLiteral::Timestamp(v) => Self::timestamp_to_year(*v)?,
            PrimitiveLiteral::Timestamptz(v) => Self::timestamp_to_year(*v)?,
            _ => {
                return Err(crate::Error::new(
                    crate::ErrorKind::FeatureUnsupported,
                    format!(
                        "Unsupported data type for year transform: {:?}",
                        input.data_type()
                    ),
                ))
            }
        };
        Ok(Some(Datum::int(val)))
    }
}

/// Extract a date or timestamp month, as months from 1970-01-01
#[derive(Debug)]
pub struct Month;

impl Month {
    #[inline]
    fn timestamp_to_month(timestamp: i64) -> Result<i32> {
        // date: aaaa-aa-aa
        // unix epoch date: 1970-01-01
        // if date > unix epoch date, delta month = (aa - 1) + 12 * (aaaa-1970)
        // if date < unix epoch date, delta month = (12 - (aa - 1)) + 12 * (1970-aaaa-1)
        let date = DateTime::from_timestamp_micros(timestamp).ok_or_else(|| {
            Error::new(
                ErrorKind::DataInvalid,
                "Fail to convert timestamp to date in month transform",
            )
        })?;
        let unix_epoch_date = DateTime::from_timestamp_micros(0)
            .expect("0 timestamp from unix epoch should be valid");
        if date > unix_epoch_date {
            Ok((date.month0() as i32) + 12 * (date.year() - UNIX_EPOCH_YEAR))
        } else {
            let delta = (12 - date.month0() as i32) + 12 * (UNIX_EPOCH_YEAR - date.year() - 1);
            Ok(-delta)
        }
    }
}

impl TransformFunction for Month {
    fn transform(&self, input: ArrayRef) -> Result<ArrayRef> {
        let year_array = date_part(&input, DatePart::Year)
            .map_err(|err| Error::new(ErrorKind::Unexpected, format!("{err}")))?;
        let year_array: Int32Array = year_array
            .as_any()
            .downcast_ref::<Int32Array>()
            .unwrap()
            .unary(|v| 12 * (v - UNIX_EPOCH_YEAR));
        let month_array = date_part(&input, DatePart::Month)
            .map_err(|err| Error::new(ErrorKind::Unexpected, format!("{err}")))?;
        Ok(Arc::<Int32Array>::new(
            binary(
                month_array.as_any().downcast_ref::<Int32Array>().unwrap(),
                year_array.as_any().downcast_ref::<Int32Array>().unwrap(),
                // Compute month from 1970-01-01, so minus 1 here.
                |a, b| a + b - 1,
            )
            .unwrap(),
        ))
    }

    fn transform_literal(&self, input: &crate::spec::Datum) -> Result<Option<crate::spec::Datum>> {
        let val = match input.literal() {
            PrimitiveLiteral::Date(v) => {
                (Date32Type::to_naive_date(*v).year() - UNIX_EPOCH_YEAR) * 12
                    + Date32Type::to_naive_date(*v).month0() as i32
            }
            PrimitiveLiteral::Timestamp(v) => Self::timestamp_to_month(*v)?,
            PrimitiveLiteral::Timestamptz(v) => Self::timestamp_to_month(*v)?,
            _ => {
                return Err(crate::Error::new(
                    crate::ErrorKind::FeatureUnsupported,
                    format!(
                        "Unsupported data type for month transform: {:?}",
                        input.data_type()
                    ),
                ))
            }
        };
        Ok(Some(Datum::int(val)))
    }
}

/// Extract a date or timestamp day, as days from 1970-01-01
#[derive(Debug)]
pub struct Day;

impl Day {
    #[inline]
    fn day_timestamp_micro(v: i64) -> Result<i32> {
        let secs = v / MICROS_PER_SECOND;

        let (nanos, offset) = if v >= 0 {
            let nanos = (v.rem_euclid(MICROS_PER_SECOND) * 1_000) as u32;
            let offset = 0i64;
            (nanos, offset)
        } else {
            let v = v + 1;
            let nanos = (v.rem_euclid(MICROS_PER_SECOND) * 1_000) as u32;
            let offset = 1i64;
            (nanos, offset)
        };

        let delta = Duration::new(secs, nanos).ok_or_else(|| {
            Error::new(
                ErrorKind::DataInvalid,
                format!(
                    "Failed to create 'TimeDelta' from seconds {} and nanos {}",
                    secs, nanos
                ),
            )
        })?;

        let days = (delta.num_days() - offset) as i32;

        Ok(days)
    }
}

impl TransformFunction for Day {
    fn transform(&self, input: ArrayRef) -> Result<ArrayRef> {
        let res: Int32Array = match input.data_type() {
            DataType::Timestamp(TimeUnit::Microsecond, _) => input
                .as_any()
                .downcast_ref::<TimestampMicrosecondArray>()
                .unwrap()
                .try_unary(|v| -> Result<i32> { Self::day_timestamp_micro(v) })?,
            DataType::Date32 => input
                .as_any()
                .downcast_ref::<Date32Array>()
                .unwrap()
                .unary(|v| -> i32 { v }),
            _ => {
                return Err(Error::new(
                    ErrorKind::Unexpected,
                    format!(
                        "Should not call internally for unsupported data type {:?}",
                        input.data_type()
                    ),
                ))
            }
        };
        Ok(Arc::new(res))
    }

    fn transform_literal(&self, input: &crate::spec::Datum) -> Result<Option<crate::spec::Datum>> {
        let val = match input.literal() {
            PrimitiveLiteral::Date(v) => *v,
            PrimitiveLiteral::Timestamp(v) => Self::day_timestamp_micro(*v)?,
            PrimitiveLiteral::Timestamptz(v) => Self::day_timestamp_micro(*v)?,
            _ => {
                return Err(crate::Error::new(
                    crate::ErrorKind::FeatureUnsupported,
                    format!(
                        "Unsupported data type for day transform: {:?}",
                        input.data_type()
                    ),
                ))
            }
        };
        Ok(Some(Datum::int(val)))
    }
}

/// Extract a timestamp hour, as hours from 1970-01-01 00:00:00
#[derive(Debug)]
pub struct Hour;

impl Hour {
    #[inline]
    fn hour_timestamp_micro(v: i64) -> i32 {
        (v as f64 / 1000.0 / 1000.0 * HOUR_PER_SECOND) as i32
    }
}

impl TransformFunction for Hour {
    fn transform(&self, input: ArrayRef) -> Result<ArrayRef> {
        let res: Int32Array = match input.data_type() {
            DataType::Timestamp(TimeUnit::Microsecond, _) => input
                .as_any()
                .downcast_ref::<TimestampMicrosecondArray>()
                .unwrap()
                .unary(|v| -> i32 { Self::hour_timestamp_micro(v) }),
            _ => {
                return Err(crate::Error::new(
                    crate::ErrorKind::FeatureUnsupported,
                    format!(
                        "Unsupported data type for hour transform: {:?}",
                        input.data_type()
                    ),
                ));
            }
        };
        Ok(Arc::new(res))
    }

    fn transform_literal(&self, input: &crate::spec::Datum) -> Result<Option<crate::spec::Datum>> {
        let val = match input.literal() {
            PrimitiveLiteral::Timestamp(v) => Self::hour_timestamp_micro(*v),
            PrimitiveLiteral::Timestamptz(v) => Self::hour_timestamp_micro(*v),
            _ => {
                return Err(crate::Error::new(
                    crate::ErrorKind::FeatureUnsupported,
                    format!(
                        "Unsupported data type for hour transform: {:?}",
                        input.data_type()
                    ),
                ))
            }
        };
        Ok(Some(Datum::int(val)))
    }
}

