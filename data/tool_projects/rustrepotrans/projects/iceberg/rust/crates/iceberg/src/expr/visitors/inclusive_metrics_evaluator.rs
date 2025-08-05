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

use crate::expr::visitors::bound_predicate_visitor::{visit, BoundPredicateVisitor};
use crate::expr::{BoundPredicate, BoundReference};
use crate::spec::{DataFile, Datum, PrimitiveLiteral};
use crate::{Error, ErrorKind};
use fnv::FnvHashSet;

const IN_PREDICATE_LIMIT: usize = 200;
const ROWS_MIGHT_MATCH: crate::Result<bool> = Ok(true);
const ROWS_CANNOT_MATCH: crate::Result<bool> = Ok(false);

pub(crate) struct InclusiveMetricsEvaluator<'a> {
    data_file: &'a DataFile,
}

impl<'a> InclusiveMetricsEvaluator<'a> {
    fn new(data_file: &'a DataFile) -> Self {
        InclusiveMetricsEvaluator { data_file }
    }

    /// Evaluate this `InclusiveMetricsEvaluator`'s filter predicate against the
    /// provided [`DataFile`]'s metrics. Used by [`TableScan`] to
    /// see if this `DataFile` contains data that could match
    /// the scan's filter.
    pub(crate) fn eval(
        filter: &'a BoundPredicate,
        data_file: &'a DataFile,
        include_empty_files: bool,
    ) -> crate::Result<bool> {
        if !include_empty_files && data_file.record_count == 0 {
            return ROWS_CANNOT_MATCH;
        }

        let mut evaluator = Self::new(data_file);
        visit(&mut evaluator, filter)
    }

    fn nan_count(&self, field_id: i32) -> Option<&u64> {
        self.data_file.nan_value_counts.get(&field_id)
    }

    fn null_count(&self, field_id: i32) -> Option<&u64> {
        self.data_file.null_value_counts.get(&field_id)
    }

    fn value_count(&self, field_id: i32) -> Option<&u64> {
        self.data_file.value_counts.get(&field_id)
    }

    fn lower_bound(&self, field_id: i32) -> Option<&Datum> {
        self.data_file.lower_bounds.get(&field_id)
    }

    fn upper_bound(&self, field_id: i32) -> Option<&Datum> {
        self.data_file.upper_bounds.get(&field_id)
    }

    fn contains_nans_only(&self, field_id: i32) -> bool {
        let nan_count = self.nan_count(field_id);
        let value_count = self.value_count(field_id);

        nan_count.is_some() && nan_count == value_count
    }

    fn contains_nulls_only(&self, field_id: i32) -> bool {
        let null_count = self.null_count(field_id);
        let value_count = self.value_count(field_id);

        null_count.is_some() && null_count == value_count
    }

    fn may_contain_null(&self, field_id: i32) -> bool {
        if let Some(&null_count) = self.null_count(field_id) {
            null_count > 0
        } else {
            true
        }
    }

    fn visit_inequality(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        cmp_fn: fn(&Datum, &Datum) -> bool,
        use_lower_bound: bool,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        if self.contains_nulls_only(field_id) || self.contains_nans_only(field_id) {
            return ROWS_CANNOT_MATCH;
        }

        if datum.is_nan() {
            // NaN indicates unreliable bounds.
            // See the InclusiveMetricsEvaluator docs for more.
            return ROWS_MIGHT_MATCH;
        }

        let bound = if use_lower_bound {
            self.lower_bound(field_id)
        } else {
            self.upper_bound(field_id)
        };

        if let Some(bound) = bound {
            if cmp_fn(bound, datum) {
                return ROWS_MIGHT_MATCH;
            }

            return ROWS_CANNOT_MATCH;
        }

        ROWS_MIGHT_MATCH
    }
}

impl BoundPredicateVisitor for InclusiveMetricsEvaluator<'_> {
    type T = bool;

    fn always_true(&mut self) -> crate::Result<bool> {
        ROWS_MIGHT_MATCH
    }

    fn always_false(&mut self) -> crate::Result<bool> {
        ROWS_CANNOT_MATCH
    }

    fn and(&mut self, lhs: bool, rhs: bool) -> crate::Result<bool> {
        Ok(lhs && rhs)
    }

    fn or(&mut self, lhs: bool, rhs: bool) -> crate::Result<bool> {
        Ok(lhs || rhs)
    }

    fn not(&mut self, inner: bool) -> crate::Result<bool> {
        Ok(!inner)
    }

    fn is_null(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        match self.null_count(field_id) {
            Some(&0) => ROWS_CANNOT_MATCH,
            Some(_) => ROWS_MIGHT_MATCH,
            None => ROWS_MIGHT_MATCH,
        }
    }

    fn not_null(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        if self.contains_nulls_only(field_id) {
            return ROWS_CANNOT_MATCH;
        }

        ROWS_MIGHT_MATCH
    }

    fn is_nan(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        match self.nan_count(field_id) {
            Some(&0) => ROWS_CANNOT_MATCH,
            _ if self.contains_nulls_only(field_id) => ROWS_CANNOT_MATCH,
            _ => ROWS_MIGHT_MATCH,
        }
    }

    fn not_nan(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        if self.contains_nans_only(field_id) {
            return ROWS_CANNOT_MATCH;
        }

        ROWS_MIGHT_MATCH
    }

    fn less_than(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        self.visit_inequality(reference, datum, PartialOrd::lt, true)
    }

    fn less_than_or_eq(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        self.visit_inequality(reference, datum, PartialOrd::le, true)
    }

    fn greater_than(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        self.visit_inequality(reference, datum, PartialOrd::gt, false)
    }

    fn greater_than_or_eq(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        self.visit_inequality(reference, datum, PartialOrd::ge, false)
    }

    fn eq(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        if self.contains_nulls_only(field_id) || self.contains_nans_only(field_id) {
            return ROWS_CANNOT_MATCH;
        }

        if let Some(lower_bound) = self.lower_bound(field_id) {
            if lower_bound.is_nan() {
                // NaN indicates unreliable bounds.
                // See the InclusiveMetricsEvaluator docs for more.
                return ROWS_MIGHT_MATCH;
            } else if lower_bound.gt(datum) {
                return ROWS_CANNOT_MATCH;
            }
        }

        if let Some(upper_bound) = self.upper_bound(field_id) {
            if upper_bound.is_nan() {
                // NaN indicates unreliable bounds.
                // See the InclusiveMetricsEvaluator docs for more.
                return ROWS_MIGHT_MATCH;
            } else if upper_bound.lt(datum) {
                return ROWS_CANNOT_MATCH;
            }
        }

        ROWS_MIGHT_MATCH
    }

    fn not_eq(
        &mut self,
        _reference: &BoundReference,
        _datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        // Because the bounds are not necessarily a min or max value,
        // this cannot be answered using them. notEq(col, X) with (X, Y)
        // doesn't guarantee that X is a value in col.
        ROWS_MIGHT_MATCH
    }

    fn starts_with(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        if self.contains_nulls_only(field_id) {
            return ROWS_CANNOT_MATCH;
        }

        let PrimitiveLiteral::String(datum) = datum.literal() else {
            return Err(Error::new(
                ErrorKind::Unexpected,
                "Cannot use StartsWith operator on non-string values",
            ));
        };

        if let Some(lower_bound) = self.lower_bound(field_id) {
            let PrimitiveLiteral::String(lower_bound) = lower_bound.literal() else {
                return Err(Error::new(
                    ErrorKind::Unexpected,
                    "Cannot use StartsWith operator on non-string lower_bound value",
                ));
            };

            let prefix_length = lower_bound.chars().count().min(datum.chars().count());

            // truncate lower bound so that its length
            // is not greater than the length of prefix
            let truncated_lower_bound = lower_bound.chars().take(prefix_length).collect::<String>();
            if datum < &truncated_lower_bound {
                return ROWS_CANNOT_MATCH;
            }
        }

        if let Some(upper_bound) = self.upper_bound(field_id) {
            let PrimitiveLiteral::String(upper_bound) = upper_bound.literal() else {
                return Err(Error::new(
                    ErrorKind::Unexpected,
                    "Cannot use StartsWith operator on non-string upper_bound value",
                ));
            };

            let prefix_length = upper_bound.chars().count().min(datum.chars().count());

            // truncate upper bound so that its length
            // is not greater than the length of prefix
            let truncated_upper_bound = upper_bound.chars().take(prefix_length).collect::<String>();
            if datum > &truncated_upper_bound {
                return ROWS_CANNOT_MATCH;
            }
        }

        ROWS_MIGHT_MATCH
    }

    fn not_starts_with(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        if self.may_contain_null(field_id) {
            return ROWS_MIGHT_MATCH;
        }

        // notStartsWith will match unless all values must start with the prefix.
        // This happens when the lower and upper bounds both start with the prefix.

        let PrimitiveLiteral::String(prefix) = datum.literal() else {
            return Err(Error::new(
                ErrorKind::Unexpected,
                "Cannot use StartsWith operator on non-string values",
            ));
        };

        let Some(lower_bound) = self.lower_bound(field_id) else {
            return ROWS_MIGHT_MATCH;
        };

        let PrimitiveLiteral::String(lower_bound_str) = lower_bound.literal() else {
            return Err(Error::new(
                ErrorKind::Unexpected,
                "Cannot use NotStartsWith operator on non-string lower_bound value",
            ));
        };

        if lower_bound_str < prefix {
            // if lower is shorter than the prefix then lower doesn't start with the prefix
            return ROWS_MIGHT_MATCH;
        }

        let prefix_len = prefix.chars().count();

        if lower_bound_str.chars().take(prefix_len).collect::<String>() == *prefix {
            // lower bound matches the prefix

            let Some(upper_bound) = self.upper_bound(field_id) else {
                return ROWS_MIGHT_MATCH;
            };

            let PrimitiveLiteral::String(upper_bound) = upper_bound.literal() else {
                return Err(Error::new(
                    ErrorKind::Unexpected,
                    "Cannot use NotStartsWith operator on non-string upper_bound value",
                ));
            };

            // if upper is shorter than the prefix then upper can't start with the prefix
            if upper_bound.chars().count() < prefix_len {
                return ROWS_MIGHT_MATCH;
            }

            if upper_bound.chars().take(prefix_len).collect::<String>() == *prefix {
                // both bounds match the prefix, so all rows must match the
                // prefix and therefore do not satisfy the predicate
                return ROWS_CANNOT_MATCH;
            }
        }

        ROWS_MIGHT_MATCH
    }

    fn r#in(
        &mut self,
        reference: &BoundReference,
        literals: &FnvHashSet<Datum>,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field_id = reference.field().id;

        if self.contains_nulls_only(field_id) || self.contains_nans_only(field_id) {
            return ROWS_CANNOT_MATCH;
        }

        if literals.len() > IN_PREDICATE_LIMIT {
            // skip evaluating the predicate if the number of values is too big
            return ROWS_MIGHT_MATCH;
        }

        if let Some(lower_bound) = self.lower_bound(field_id) {
            if lower_bound.is_nan() {
                // NaN indicates unreliable bounds. See the InclusiveMetricsEvaluator docs for more.
                return ROWS_MIGHT_MATCH;
            }

            if !literals.iter().any(|datum| datum.ge(lower_bound)) {
                // if all values are less than lower bound, rows cannot match.
                return ROWS_CANNOT_MATCH;
            }
        }

        if let Some(upper_bound) = self.upper_bound(field_id) {
            if upper_bound.is_nan() {
                // NaN indicates unreliable bounds. See the InclusiveMetricsEvaluator docs for more.
                return ROWS_MIGHT_MATCH;
            }

            if !literals.iter().any(|datum| datum.le(upper_bound)) {
                // if all values are greater than upper bound, rows cannot match.
                return ROWS_CANNOT_MATCH;
            }
        }

        ROWS_MIGHT_MATCH
    }

    fn not_in(
        &mut self,
        _reference: &BoundReference,
        _literals: &FnvHashSet<Datum>,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        // Because the bounds are not necessarily a min or max value,
        // this cannot be answered using them. notIn(col, {X, ...})
        // with (X, Y) doesn't guarantee that X is a value in col.
        ROWS_MIGHT_MATCH
    }
}

