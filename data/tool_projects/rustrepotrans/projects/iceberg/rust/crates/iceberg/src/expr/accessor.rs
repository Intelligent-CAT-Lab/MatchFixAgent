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

use serde_derive::{Deserialize, Serialize};
use std::sync::Arc;

use crate::spec::{Datum, Literal, PrimitiveType, Struct};
use crate::{Error, ErrorKind, Result};

#[derive(Debug, Serialize, Deserialize, Clone, PartialEq, Eq)]
pub struct StructAccessor {
    position: usize,
    r#type: PrimitiveType,
    inner: Option<Box<StructAccessor>>,
}

pub(crate) type StructAccessorRef = Arc<StructAccessor>;

impl StructAccessor {
    pub(crate) fn new(position: usize, r#type: PrimitiveType) -> Self {
        StructAccessor {
            position,
            r#type,
            inner: None,
        }
    }

    pub(crate) fn wrap(position: usize, inner: Box<StructAccessor>) -> Self {
        StructAccessor {
            position,
            r#type: inner.r#type().clone(),
            inner: Some(inner),
        }
    }

    pub(crate) fn position(&self) -> usize {
        self.position
    }

    pub(crate) fn r#type(&self) -> &PrimitiveType {
        &self.r#type
    }

    pub(crate) fn get<'a>(&'a self, container: &'a Struct) -> Result<Option<Datum>> {
        match &self.inner {
            None => {
                if container.is_null_at_index(self.position) {
                    Ok(None)
                } else if let Literal::Primitive(literal) = &container[self.position] {
                    Ok(Some(Datum::new(self.r#type().clone(), literal.clone())))
                } else {
                    Err(Error::new(
                        ErrorKind::Unexpected,
                        "Expected Literal to be Primitive",
                    ))
                }
            }
            Some(inner) => {
                if let Literal::Struct(wrapped) = &container[self.position] {
                    inner.get(wrapped)
                } else {
                    Err(Error::new(
                        ErrorKind::Unexpected,
                        "Nested accessor should only be wrapping a Struct",
                    ))
                }
            }
        }
    }
}

