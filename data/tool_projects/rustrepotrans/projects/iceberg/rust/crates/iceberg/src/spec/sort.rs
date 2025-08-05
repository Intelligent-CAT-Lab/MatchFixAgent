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

/*!
 * Sorting
*/
use crate::error::Result;
use crate::spec::Schema;
use crate::{Error, ErrorKind};
use core::fmt;
use serde::{Deserialize, Serialize};
use std::fmt::Formatter;
use std::sync::Arc;
use typed_builder::TypedBuilder;

use super::transform::Transform;

/// Reference to [`SortOrder`].
pub type SortOrderRef = Arc<SortOrder>;
#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Copy, Clone)]
/// Sort direction in a partition, either ascending or descending
pub enum SortDirection {
    /// Ascending
    #[serde(rename = "asc")]
    Ascending,
    /// Descending
    #[serde(rename = "desc")]
    Descending,
}

impl fmt::Display for SortDirection {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match *self {
            SortDirection::Ascending => write!(f, "ascending"),
            SortDirection::Descending => write!(f, "descending"),
        }
    }
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Copy, Clone)]
/// Describes the order of null values when sorted.
pub enum NullOrder {
    #[serde(rename = "nulls-first")]
    /// Nulls are stored first
    First,
    #[serde(rename = "nulls-last")]
    /// Nulls are stored last
    Last,
}

impl fmt::Display for NullOrder {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match *self {
            NullOrder::First => write!(f, "first"),
            NullOrder::Last => write!(f, "last"),
        }
    }
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Clone, TypedBuilder)]
#[serde(rename_all = "kebab-case")]
/// Entry for every column that is to be sorted
pub struct SortField {
    /// A source column id from the table’s schema
    pub source_id: i32,
    /// A transform that is used to produce values to be sorted on from the source column.
    pub transform: Transform,
    /// A sort direction, that can only be either asc or desc
    pub direction: SortDirection,
    /// A null order that describes the order of null values when sorted.
    pub null_order: NullOrder,
}

impl fmt::Display for SortField {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "SortField {{ source_id: {}, transform: {}, direction: {}, null_order: {} }}",
            self.source_id, self.transform, self.direction, self.null_order
        )
    }
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Clone, Builder, Default)]
#[serde(rename_all = "kebab-case")]
#[builder(setter(prefix = "with"))]
#[builder(build_fn(skip))]
/// A sort order is defined by a sort order id and a list of sort fields.
/// The order of the sort fields within the list defines the order in which the sort is applied to the data.
pub struct SortOrder {
    /// Identifier for SortOrder, order_id `0` is no sort order.
    #[builder(default)]
    pub order_id: i64,
    /// Details of the sort
    #[builder(setter(each(name = "with_sort_field")), default)]
    pub fields: Vec<SortField>,
}

impl SortOrder {
    const UNSORTED_ORDER_ID: i64 = 0;

    /// Create sort order builder
    pub fn builder() -> SortOrderBuilder {
        SortOrderBuilder::default()
    }

    /// Create an unbound unsorted order
    pub fn unsorted_order() -> SortOrder {
        SortOrder {
            order_id: SortOrder::UNSORTED_ORDER_ID,
            fields: Vec::new(),
        }
    }

    /// Returns true if the sort order is unsorted.
    ///
    /// A [`SortOrder`] is unsorted if it has no sort fields.
    pub fn is_unsorted(&self) -> bool {
        self.fields.is_empty()
    }
}

impl SortOrderBuilder {
    /// Creates a new unbound sort order.
    pub fn build_unbound(&self) -> Result<SortOrder> {
        let fields = self.fields.clone().unwrap_or_default();
        return match (self.order_id, fields.as_slice()) {
            (Some(SortOrder::UNSORTED_ORDER_ID) | None, []) => Ok(SortOrder::unsorted_order()),
            (_, []) => Err(Error::new(
                ErrorKind::Unexpected,
                format!("Unsorted order ID must be {}", SortOrder::UNSORTED_ORDER_ID),
            )),
            (Some(SortOrder::UNSORTED_ORDER_ID), [..]) => Err(Error::new(
                ErrorKind::Unexpected,
                format!(
                    "Sort order ID {} is reserved for unsorted order",
                    SortOrder::UNSORTED_ORDER_ID
                ),
            )),
            (maybe_order_id, [..]) => Ok(SortOrder {
                order_id: maybe_order_id.unwrap_or(1),
                fields: fields.to_vec(),
            }),
        };
    }

    /// Creates a new bound sort order.
    pub fn build(&self, schema: Schema) -> Result<SortOrder> {
        let unbound_sort_order = self.build_unbound()?;
        SortOrderBuilder::check_compatibility(unbound_sort_order, schema)
    }

    /// Returns the given sort order if it is compatible with the given schema
    fn check_compatibility(sort_order: SortOrder, schema: Schema) -> Result<SortOrder> {
        let sort_fields = &sort_order.fields;
        for sort_field in sort_fields {
            match schema.field_by_id(sort_field.source_id) {
                None => {
                    return Err(Error::new(
                        ErrorKind::Unexpected,
                        format!("Cannot find source column for sort field: {sort_field}"),
                    ))
                }
                Some(source_field) => {
                    let source_type = source_field.field_type.as_ref();

                    if !source_type.is_primitive() {
                        return Err(Error::new(
                            ErrorKind::Unexpected,
                            format!("Cannot sort by non-primitive source field: {source_type}"),
                        ));
                    }

                    let field_transform = sort_field.transform;
                    if field_transform.result_type(source_type).is_err() {
                        return Err(Error::new(
                            ErrorKind::Unexpected,
                            format!(
                                "Invalid source type {source_type} for transform {field_transform}"
                            ),
                        ));
                    }
                }
            }
        }

        Ok(sort_order)
    }
}

