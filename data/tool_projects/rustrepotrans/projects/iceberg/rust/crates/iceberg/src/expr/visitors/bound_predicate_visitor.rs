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

use crate::expr::{BoundPredicate, BoundReference, PredicateOperator};
use crate::spec::Datum;
use crate::Result;
use fnv::FnvHashSet;

/// A visitor for [`BoundPredicate`]s. Visits in post-order.
pub trait BoundPredicateVisitor {
    /// The return type of this visitor
    type T;

    /// Called after an `AlwaysTrue` predicate is visited
    fn always_true(&mut self) -> Result<Self::T>;

    /// Called after an `AlwaysFalse` predicate is visited
    fn always_false(&mut self) -> Result<Self::T>;

    /// Called after an `And` predicate is visited
    fn and(&mut self, lhs: Self::T, rhs: Self::T) -> Result<Self::T>;

    /// Called after an `Or` predicate is visited
    fn or(&mut self, lhs: Self::T, rhs: Self::T) -> Result<Self::T>;

    /// Called after a `Not` predicate is visited
    fn not(&mut self, inner: Self::T) -> Result<Self::T>;

    /// Called after a predicate with an `IsNull` operator is visited
    fn is_null(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `NotNull` operator is visited
    fn not_null(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with an `IsNan` operator is visited
    fn is_nan(&mut self, reference: &BoundReference, predicate: &BoundPredicate)
        -> Result<Self::T>;

    /// Called after a predicate with a `NotNan` operator is visited
    fn not_nan(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `LessThan` operator is visited
    fn less_than(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `LessThanOrEq` operator is visited
    fn less_than_or_eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `GreaterThan` operator is visited
    fn greater_than(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `GreaterThanOrEq` operator is visited
    fn greater_than_or_eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with an `Eq` operator is visited
    fn eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `NotEq` operator is visited
    fn not_eq(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `StartsWith` operator is visited
    fn starts_with(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `NotStartsWith` operator is visited
    fn not_starts_with(
        &mut self,
        reference: &BoundReference,
        literal: &Datum,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with an `In` operator is visited
    fn r#in(
        &mut self,
        reference: &BoundReference,
        literals: &FnvHashSet<Datum>,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;

    /// Called after a predicate with a `NotIn` operator is visited
    fn not_in(
        &mut self,
        reference: &BoundReference,
        literals: &FnvHashSet<Datum>,
        predicate: &BoundPredicate,
    ) -> Result<Self::T>;
}

/// Visits a [`BoundPredicate`] with the provided visitor,
/// in post-order
pub(crate) fn visit<V: BoundPredicateVisitor>(
    visitor: &mut V,
    predicate: &BoundPredicate,
) -> Result<V::T> {
    match predicate {
        BoundPredicate::AlwaysTrue => visitor.always_true(),
        BoundPredicate::AlwaysFalse => visitor.always_false(),
        BoundPredicate::And(expr) => {
            let [left_pred, right_pred] = expr.inputs();

            let left_result = visit(visitor, left_pred)?;
            let right_result = visit(visitor, right_pred)?;

            visitor.and(left_result, right_result)
        }
        BoundPredicate::Or(expr) => {
            let [left_pred, right_pred] = expr.inputs();

            let left_result = visit(visitor, left_pred)?;
            let right_result = visit(visitor, right_pred)?;

            visitor.or(left_result, right_result)
        }
        BoundPredicate::Not(expr) => {
            let [inner_pred] = expr.inputs();

            let inner_result = visit(visitor, inner_pred)?;

            visitor.not(inner_result)
        }
        BoundPredicate::Unary(expr) => match expr.op() {
            PredicateOperator::IsNull => visitor.is_null(expr.term(), predicate),
            PredicateOperator::NotNull => visitor.not_null(expr.term(), predicate),
            PredicateOperator::IsNan => visitor.is_nan(expr.term(), predicate),
            PredicateOperator::NotNan => visitor.not_nan(expr.term(), predicate),
            op => {
                panic!("Unexpected op for unary predicate: {}", &op)
            }
        },
        BoundPredicate::Binary(expr) => {
            let reference = expr.term();
            let literal = expr.literal();
            match expr.op() {
                PredicateOperator::LessThan => visitor.less_than(reference, literal, predicate),
                PredicateOperator::LessThanOrEq => {
                    visitor.less_than_or_eq(reference, literal, predicate)
                }
                PredicateOperator::GreaterThan => {
                    visitor.greater_than(reference, literal, predicate)
                }
                PredicateOperator::GreaterThanOrEq => {
                    visitor.greater_than_or_eq(reference, literal, predicate)
                }
                PredicateOperator::Eq => visitor.eq(reference, literal, predicate),
                PredicateOperator::NotEq => visitor.not_eq(reference, literal, predicate),
                PredicateOperator::StartsWith => visitor.starts_with(reference, literal, predicate),
                PredicateOperator::NotStartsWith => {
                    visitor.not_starts_with(reference, literal, predicate)
                }
                op => {
                    panic!("Unexpected op for binary predicate: {}", &op)
                }
            }
        }
        BoundPredicate::Set(expr) => {
            let reference = expr.term();
            let literals = expr.literals();
            match expr.op() {
                PredicateOperator::In => visitor.r#in(reference, literals, predicate),
                PredicateOperator::NotIn => visitor.not_in(reference, literals, predicate),
                op => {
                    panic!("Unexpected op for set predicate: {}", &op)
                }
            }
        }
    }
}

