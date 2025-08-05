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
use crate::spec::{Datum, FieldSummary, ManifestFile, PrimitiveLiteral, Type};
use crate::Result;
use crate::{Error, ErrorKind};
use fnv::FnvHashSet;

/// Evaluates a [`ManifestFile`] to see if the partition summaries
/// match a provided [`BoundPredicate`].
///
/// Used by [`TableScan`] to prune the list of [`ManifestFile`]s
/// in which data might be found that matches the TableScan's filter.
#[derive(Debug)]
pub(crate) struct ManifestEvaluator {
    partition_filter: BoundPredicate,
}

impl ManifestEvaluator {
    pub(crate) fn new(partition_filter: BoundPredicate) -> Self {
        Self { partition_filter }
    }

    /// Evaluate this `ManifestEvaluator`'s filter predicate against the
    /// provided [`ManifestFile`]'s partitions. Used by [`TableScan`] to
    /// see if this `ManifestFile` could possibly contain data that matches
    /// the scan's filter.
    pub(crate) fn eval(&self, manifest_file: &ManifestFile) -> Result<bool> {
        if manifest_file.partitions.is_empty() {
            return Ok(true);
        }

        let mut evaluator = ManifestFilterVisitor::new(self, &manifest_file.partitions);

        visit(&mut evaluator, &self.partition_filter)
    }
}

struct ManifestFilterVisitor<'a> {
    manifest_evaluator: &'a ManifestEvaluator,
    partitions: &'a Vec<FieldSummary>,
}

impl<'a> ManifestFilterVisitor<'a> {
    fn new(manifest_evaluator: &'a ManifestEvaluator, partitions: &'a Vec<FieldSummary>) -> Self {
        ManifestFilterVisitor {
            manifest_evaluator,
            partitions,
        }
    }
}

const ROWS_MIGHT_MATCH: Result<bool> = Ok(true);
const ROWS_CANNOT_MATCH: Result<bool> = Ok(false);
const IN_PREDICATE_LIMIT: usize = 200;

impl BoundPredicateVisitor for ManifestFilterVisitor<'_> {
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
        Ok(self.field_summary_for_reference(reference).contains_null)
    }

    fn not_null(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);

        // contains_null encodes whether at least one partition value is null,
        // lowerBound is null if all partition values are null
        if ManifestFilterVisitor::are_all_null(field, &reference.field().field_type) {
            ROWS_CANNOT_MATCH
        } else {
            ROWS_MIGHT_MATCH
        }
    }

    fn is_nan(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);
        if let Some(contains_nan) = field.contains_nan {
            if !contains_nan {
                return ROWS_CANNOT_MATCH;
            }
        }

        if ManifestFilterVisitor::are_all_null(field, &reference.field().field_type) {
            return ROWS_CANNOT_MATCH;
        }

        ROWS_MIGHT_MATCH
    }

    fn not_nan(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);
        if let Some(contains_nan) = field.contains_nan {
            // check if all values are nan
            if contains_nan && !field.contains_null && field.lower_bound.is_none() {
                return ROWS_CANNOT_MATCH;
            }
        }
        ROWS_MIGHT_MATCH
    }

    fn less_than(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);
        match &field.lower_bound {
            Some(bound) if datum <= bound => ROWS_CANNOT_MATCH,
            Some(_) => ROWS_MIGHT_MATCH,
            None => ROWS_CANNOT_MATCH,
        }
    }

    fn less_than_or_eq(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);
        match &field.lower_bound {
            Some(bound) if datum < bound => ROWS_CANNOT_MATCH,
            Some(_) => ROWS_MIGHT_MATCH,
            None => ROWS_CANNOT_MATCH,
        }
    }

    fn greater_than(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);
        match &field.upper_bound {
            Some(bound) if datum >= bound => ROWS_CANNOT_MATCH,
            Some(_) => ROWS_MIGHT_MATCH,
            None => ROWS_CANNOT_MATCH,
        }
    }

    fn greater_than_or_eq(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);
        match &field.upper_bound {
            Some(bound) if datum > bound => ROWS_CANNOT_MATCH,
            Some(_) => ROWS_MIGHT_MATCH,
            None => ROWS_CANNOT_MATCH,
        }
    }

    fn eq(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);

        if field.lower_bound.is_none() || field.upper_bound.is_none() {
            return ROWS_CANNOT_MATCH;
        }

        if let Some(lower_bound) = &field.lower_bound {
            if lower_bound > datum {
                return ROWS_CANNOT_MATCH;
            }
        }

        if let Some(upper_bound) = &field.upper_bound {
            if upper_bound < datum {
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
        // because the bounds are not necessarily a min or max value, this cannot be answered using
        // them. notEq(col, X) with (X, Y) doesn't guarantee that X is a value in col.
        ROWS_MIGHT_MATCH
    }

    fn starts_with(
        &mut self,
        reference: &BoundReference,
        datum: &Datum,
        _predicate: &BoundPredicate,
    ) -> crate::Result<bool> {
        let field = self.field_summary_for_reference(reference);

        if field.lower_bound.is_none() || field.upper_bound.is_none() {
            return ROWS_CANNOT_MATCH;
        }

        let prefix = ManifestFilterVisitor::datum_as_str(
            datum,
            "Cannot perform starts_with on non-string value",
        )?;
        let prefix_len = prefix.len();

        if let Some(lower_bound) = &field.lower_bound {
            let lower_bound_str = ManifestFilterVisitor::datum_as_str(
                lower_bound,
                "Cannot perform starts_with on non-string lower bound",
            )?;
            let min_len = lower_bound_str.len().min(prefix_len);
            if prefix.as_bytes().lt(&lower_bound_str.as_bytes()[..min_len]) {
                return ROWS_CANNOT_MATCH;
            }
        }

        if let Some(upper_bound) = &field.upper_bound {
            let upper_bound_str = ManifestFilterVisitor::datum_as_str(
                upper_bound,
                "Cannot perform starts_with on non-string upper bound",
            )?;
            let min_len = upper_bound_str.len().min(prefix_len);
            if prefix.as_bytes().gt(&upper_bound_str.as_bytes()[..min_len]) {
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
        let field = self.field_summary_for_reference(reference);

        if field.contains_null || field.lower_bound.is_none() || field.upper_bound.is_none() {
            return ROWS_MIGHT_MATCH;
        }

        let prefix = ManifestFilterVisitor::datum_as_str(
            datum,
            "Cannot perform not_starts_with on non-string value",
        )?;
        let prefix_len = prefix.len();

        // not_starts_with will match unless all values must start with the prefix. This happens when
        // the lower and upper bounds both start with the prefix.
        if let Some(lower_bound) = &field.lower_bound {
            let lower_bound_str = ManifestFilterVisitor::datum_as_str(
                lower_bound,
                "Cannot perform not_starts_with on non-string lower bound",
            )?;

            // if lower is shorter than the prefix then lower doesn't start with the prefix
            if prefix_len > lower_bound_str.len() {
                return ROWS_MIGHT_MATCH;
            }

            if prefix
                .as_bytes()
                .eq(&lower_bound_str.as_bytes()[..prefix_len])
            {
                if let Some(upper_bound) = &field.upper_bound {
                    let upper_bound_str = ManifestFilterVisitor::datum_as_str(
                        upper_bound,
                        "Cannot perform not_starts_with on non-string upper bound",
                    )?;

                    // if upper is shorter than the prefix then upper can't start with the prefix
                    if prefix_len > upper_bound_str.len() {
                        return ROWS_MIGHT_MATCH;
                    }

                    if prefix
                        .as_bytes()
                        .eq(&upper_bound_str.as_bytes()[..prefix_len])
                    {
                        return ROWS_CANNOT_MATCH;
                    }
                }
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
        let field = self.field_summary_for_reference(reference);
        if field.lower_bound.is_none() {
            return ROWS_CANNOT_MATCH;
        }

        if literals.len() > IN_PREDICATE_LIMIT {
            return ROWS_MIGHT_MATCH;
        }

        if let Some(lower_bound) = &field.lower_bound {
            if literals.iter().all(|datum| lower_bound > datum) {
                return ROWS_CANNOT_MATCH;
            }
        }

        if let Some(upper_bound) = &field.upper_bound {
            if literals.iter().all(|datum| upper_bound < datum) {
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
        // because the bounds are not necessarily a min or max value, this cannot be answered using
        // them. notIn(col, {X, ...}) with (X, Y) doesn't guarantee that X is a value in col.
        ROWS_MIGHT_MATCH
    }
}

impl ManifestFilterVisitor<'_> {
    fn field_summary_for_reference(&self, reference: &BoundReference) -> &FieldSummary {
        let pos = reference.accessor().position();
        &self.partitions[pos]
    }

    fn are_all_null(field: &FieldSummary, r#type: &Type) -> bool {
        // contains_null encodes whether at least one partition value is null,
        // lowerBound is null if all partition values are null
        let mut all_null: bool = field.contains_null && field.lower_bound.is_none();

        if all_null && r#type.is_floating_type() {
            // floating point types may include NaN values, which we check separately.
            // In case bounds don't include NaN value, contains_nan needs to be checked against.
            all_null = match field.contains_nan {
                Some(val) => !val,
                None => false,
            }
        }

        all_null
    }

    fn datum_as_str<'a>(bound: &'a Datum, err_msg: &str) -> crate::Result<&'a String> {
        let PrimitiveLiteral::String(bound) = bound.literal() else {
            return Err(Error::new(ErrorKind::Unexpected, err_msg));
        };
        Ok(bound)
    }
}

