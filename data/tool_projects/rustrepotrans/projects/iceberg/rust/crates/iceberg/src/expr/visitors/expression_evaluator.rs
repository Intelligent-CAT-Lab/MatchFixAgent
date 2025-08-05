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

use fnv::FnvHashSet;

use crate::{
    expr::{BoundPredicate, BoundReference},
    spec::{DataFile, Datum, PrimitiveLiteral, Struct},
    Error, ErrorKind, Result,
};

use super::bound_predicate_visitor::{visit, BoundPredicateVisitor};

/// Evaluates a [`DataFile`]'s partition [`Struct`] to check
/// if the partition tuples match the given [`BoundPredicate`].
///
/// Use within [`TableScan`] to prune the list of [`DataFile`]s
/// that could potentially match the TableScan's filter.
#[derive(Debug)]
pub(crate) struct ExpressionEvaluator {
    /// The provided partition filter.
    partition_filter: BoundPredicate,
}

impl ExpressionEvaluator {
    /// Creates a new [`ExpressionEvaluator`].
    pub(crate) fn new(partition_filter: BoundPredicate) -> Self {
        Self { partition_filter }
    }

    /// Evaluate this [`ExpressionEvaluator`]'s partition filter against
    /// the provided [`DataFile`]'s partition [`Struct`]. Used by [`TableScan`]
    /// to see if this [`DataFile`] could possibly contain data that matches
    /// the scan's filter.
    pub(crate) fn eval(&self, data_file: &DataFile) -> Result<bool> {
        let mut visitor = ExpressionEvaluatorVisitor::new(self, data_file.partition());

        visit(&mut visitor, &self.partition_filter)
    }
}

/// Acts as a visitor for [`ExpressionEvaluator`] to apply
/// evaluation logic to different parts of a data structure,
/// specifically for data file partitions.
#[derive(Debug)]
struct ExpressionEvaluatorVisitor<'a> {
    /// Reference to an [`ExpressionEvaluator`].
    expression_evaluator: &'a ExpressionEvaluator,
    /// Reference to a [`DataFile`]'s partition [`Struct`].
    partition: &'a Struct,
}

impl<'a> ExpressionEvaluatorVisitor<'a> {
    /// Creates a new [`ExpressionEvaluatorVisitor`].
    fn new(expression_evaluator: &'a ExpressionEvaluator, partition: &'a Struct) -> Self {
        Self {
            expression_evaluator,
            partition,
        }
    }
}

impl BoundPredicateVisitor for ExpressionEvaluatorVisitor<'_> {
    type T = bool;

    fn always_true(&mut self) -> Result<bool> {
        Ok(true)
    }

    fn always_false(&mut self) -> Result<bool> {
        Ok(false)
    }

    fn and(&mut self, lhs: bool, rhs: bool) -> Result<bool> {
        Ok(lhs && rhs)
    }

    fn or(&mut self, lhs: bool, rhs: bool) -> Result<bool> {
        Ok(lhs || rhs)
    }

    fn not(&mut self, _inner: bool) -> Result<bool> {
        Err(Error::new(ErrorKind::Unexpected, "The evaluation of expressions should not be performed against Predicates that contain a Not operator. Ensure that \"Rewrite Not\" gets applied to the originating Predicate before binding it."))
    }

    fn is_null(&mut self, reference: &BoundReference, _predicate: &BoundPredicate) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(_) => Ok(false),
            None => Ok(true),
        }
    }

    fn not_null(
        &mut self,
        reference: &BoundReference,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(_) => Ok(true),
            None => Ok(false),
        }
    }

    fn is_nan(&mut self, reference: &BoundReference, _predicate: &BoundPredicate) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(datum.is_nan()),
            None => Ok(false),
        }
    }

    fn not_nan(&mut self, reference: &BoundReference, _predicate: &BoundPredicate) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(!datum.is_nan()),
            None => Ok(true),
        }
    }

    fn less_than(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(&datum < literal),
            None => Ok(false),
        }
    }

    fn less_than_or_eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(&datum <= literal),
            None => Ok(false),
        }
    }

    fn greater_than(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(&datum > literal),
            None => Ok(false),
        }
    }

    fn greater_than_or_eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(&datum >= literal),
            None => Ok(false),
        }
    }

    fn eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(&datum == literal),
            None => Ok(false),
        }
    }

    fn not_eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(&datum != literal),
            None => Ok(true),
        }
    }

    fn starts_with(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        let Some(datum) = reference.accessor().get(self.partition)? else {
            return Ok(false);
        };

        match (datum.literal(), literal.literal()) {
            (PrimitiveLiteral::String(d), PrimitiveLiteral::String(l)) => Ok(d.starts_with(l)),
            _ => Ok(false),
        }
    }

    fn not_starts_with(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        Ok(!self.starts_with(reference, literal, _predicate)?)
    }

    fn r#in(
        &mut self,
        reference: &BoundReference,
        literals: &FnvHashSet<Datum>,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(literals.contains(&datum)),
            None => Ok(false),
        }
    }

    fn not_in(
        &mut self,
        reference: &BoundReference,
        literals: &FnvHashSet<Datum>,
        _predicate: &BoundPredicate,
    ) -> Result<bool> {
        match reference.accessor().get(self.partition)? {
            Some(datum) => Ok(!literals.contains(&datum)),
            None => Ok(true),
        }
    }
}

