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
use crate::expr::{BoundPredicate, BoundReference, Predicate};
use crate::spec::{Datum, PartitionField, PartitionSpecRef};
use crate::Error;
use fnv::FnvHashSet;
use std::collections::HashMap;

pub(crate) struct InclusiveProjection {
    partition_spec: PartitionSpecRef,
    cached_parts: HashMap<i32, Vec<PartitionField>>,
}

impl InclusiveProjection {
    pub(crate) fn new(partition_spec: PartitionSpecRef) -> Self {
        Self {
            partition_spec,
            cached_parts: HashMap::new(),
        }
    }

    fn get_parts_for_field_id(&mut self, field_id: i32) -> &Vec<PartitionField> {
        if let std::collections::hash_map::Entry::Vacant(e) = self.cached_parts.entry(field_id) {
            let mut parts: Vec<PartitionField> = vec![];
            for partition_spec_field in &self.partition_spec.fields {
                if partition_spec_field.source_id == field_id {
                    parts.push(partition_spec_field.clone())
                }
            }

            e.insert(parts);
        }

        &self.cached_parts[&field_id]
    }

    pub(crate) fn project(&mut self, predicate: &BoundPredicate) -> crate::Result<Predicate> {
        visit(self, predicate)
    }

    fn get_parts(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> Result<Predicate, Error> {
        let field_id = reference.field().id;

        // This could be made a bit neater if `try_reduce` ever becomes stable
        self.get_parts_for_field_id(field_id)
            .iter()
            .try_fold(Predicate::AlwaysTrue, |res, part| {
                Ok(
                    if let Some(pred_for_part) = part.transform.project(&part.name, predicate)? {
                        if res == Predicate::AlwaysTrue {
                            pred_for_part
                        } else {
                            res.and(pred_for_part)
                        }
                    } else {
                        res
                    },
                )
            })
    }
}

impl BoundPredicateVisitor for InclusiveProjection {
    type T = Predicate;

    fn always_true(&mut self) -> crate::Result<Self::T> {
        Ok(Predicate::AlwaysTrue)
    }

    fn always_false(&mut self) -> crate::Result<Self::T> {
        Ok(Predicate::AlwaysFalse)
    }

    fn and(&mut self, lhs: Self::T, rhs: Self::T) -> crate::Result<Self::T> {
        Ok(lhs.and(rhs))
    }

    fn or(&mut self, lhs: Self::T, rhs: Self::T) -> crate::Result<Self::T> {
        Ok(lhs.or(rhs))
    }

    fn not(&mut self, _inner: Self::T) -> crate::Result<Self::T> {
        panic!("InclusiveProjection should not be performed against Predicates that contain a Not operator. Ensure that \"Rewrite Not\" gets applied to the originating Predicate before binding it.")
    }

    fn is_null(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn not_null(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn is_nan(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn not_nan(
        &mut self,
        reference: &BoundReference,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn less_than(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn less_than_or_eq(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn greater_than(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn greater_than_or_eq(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn eq(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn not_eq(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn starts_with(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn not_starts_with(
        &mut self,
        reference: &BoundReference,
        _literal: &Datum,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn r#in(
        &mut self,
        reference: &BoundReference,
        _literals: &FnvHashSet<Datum>,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }

    fn not_in(
        &mut self,
        reference: &BoundReference,
        _literals: &FnvHashSet<Datum>,
        predicate: &BoundPredicate,
    ) -> crate::Result<Self::T> {
        self.get_parts(reference, predicate)
    }
}

