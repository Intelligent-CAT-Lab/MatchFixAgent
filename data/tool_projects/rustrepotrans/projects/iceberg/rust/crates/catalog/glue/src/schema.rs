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

/// Property `iceberg.field.id` for `Column`
pub(crate) const ICEBERG_FIELD_ID: &str = "iceberg.field.id";
/// Property `iceberg.field.optional` for `Column`
pub(crate) const ICEBERG_FIELD_OPTIONAL: &str = "iceberg.field.optional";
/// Property `iceberg.field.current` for `Column`
pub(crate) const ICEBERG_FIELD_CURRENT: &str = "iceberg.field.current";

use std::collections::HashMap;

use iceberg::{
    spec::{visit_schema, PrimitiveType, SchemaVisitor, TableMetadata},
    Error, ErrorKind, Result,
};

use aws_sdk_glue::types::Column;

use crate::error::from_aws_build_error;

type GlueSchema = Vec<Column>;

#[derive(Debug, Default)]
pub(crate) struct GlueSchemaBuilder {
    schema: GlueSchema,
    is_current: bool,
    depth: usize,
}

impl GlueSchemaBuilder {
    /// Creates a new `GlueSchemaBuilder` from iceberg `Schema`
    pub fn from_iceberg(metadata: &TableMetadata) -> Result<GlueSchemaBuilder> {
        let current_schema = metadata.current_schema();

        let mut builder = Self {
            schema: Vec::new(),
            is_current: true,
            depth: 0,
        };

        visit_schema(current_schema, &mut builder)?;

        builder.is_current = false;

        for schema in metadata.schemas_iter() {
            if schema.schema_id() == current_schema.schema_id() {
                continue;
            }

            visit_schema(schema, &mut builder)?;
        }

        Ok(builder)
    }

    /// Returns the newly converted `GlueSchema`
    pub fn build(self) -> GlueSchema {
        self.schema
    }

    /// Check if is in `StructType` while traversing schema
    fn is_inside_struct(&self) -> bool {
        self.depth > 0
    }
}

impl SchemaVisitor for GlueSchemaBuilder {
    type T = String;

    fn schema(
        &mut self,
        _schema: &iceberg::spec::Schema,
        value: Self::T,
    ) -> iceberg::Result<String> {
        Ok(value)
    }

    fn before_struct_field(&mut self, _field: &iceberg::spec::NestedFieldRef) -> Result<()> {
        self.depth += 1;
        Ok(())
    }

    fn r#struct(
        &mut self,
        r#_struct: &iceberg::spec::StructType,
        results: Vec<String>,
    ) -> iceberg::Result<String> {
        Ok(format!("struct<{}>", results.join(", ")))
    }

    fn after_struct_field(&mut self, _field: &iceberg::spec::NestedFieldRef) -> Result<()> {
        self.depth -= 1;
        Ok(())
    }

    fn field(
        &mut self,
        field: &iceberg::spec::NestedFieldRef,
        value: String,
    ) -> iceberg::Result<String> {
        if self.is_inside_struct() {
            return Ok(format!("{}:{}", field.name, &value));
        }

        let parameters = HashMap::from([
            (ICEBERG_FIELD_ID.to_string(), format!("{}", field.id)),
            (
                ICEBERG_FIELD_OPTIONAL.to_string(),
                format!("{}", field.required).to_lowercase(),
            ),
            (
                ICEBERG_FIELD_CURRENT.to_string(),
                format!("{}", self.is_current).to_lowercase(),
            ),
        ]);

        let mut builder = Column::builder()
            .name(field.name.clone())
            .r#type(&value)
            .set_parameters(Some(parameters));

        if let Some(comment) = field.doc.as_ref() {
            builder = builder.comment(comment);
        }

        let column = builder.build().map_err(from_aws_build_error)?;

        self.schema.push(column);

        Ok(value)
    }

    fn list(&mut self, _list: &iceberg::spec::ListType, value: String) -> iceberg::Result<String> {
        Ok(format!("array<{}>", value))
    }

    fn map(
        &mut self,
        _map: &iceberg::spec::MapType,
        key_value: String,
        value: String,
    ) -> iceberg::Result<String> {
        Ok(format!("map<{},{}>", key_value, value))
    }

    fn primitive(&mut self, p: &iceberg::spec::PrimitiveType) -> iceberg::Result<Self::T> {
        let glue_type = match p {
            PrimitiveType::Boolean => "boolean".to_string(),
            PrimitiveType::Int => "int".to_string(),
            PrimitiveType::Long => "bigint".to_string(),
            PrimitiveType::Float => "float".to_string(),
            PrimitiveType::Double => "double".to_string(),
            PrimitiveType::Date => "date".to_string(),
            PrimitiveType::Timestamp => "timestamp".to_string(),
            PrimitiveType::Time | PrimitiveType::String | PrimitiveType::Uuid => {
                "string".to_string()
            }
            PrimitiveType::Binary | PrimitiveType::Fixed(_) => "binary".to_string(),
            PrimitiveType::Decimal { precision, scale } => {
                format!("decimal({},{})", precision, scale)
            }
            _ => {
                return Err(Error::new(
                    ErrorKind::FeatureUnsupported,
                    "Conversion from 'Timestamptz' is not supported",
                ))
            }
        };

        Ok(glue_type)
    }
}

