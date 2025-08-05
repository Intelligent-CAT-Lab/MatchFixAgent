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

use hive_metastore::FieldSchema;
use iceberg::spec::{visit_schema, PrimitiveType, Schema, SchemaVisitor};
use iceberg::{Error, ErrorKind, Result};

type HiveSchema = Vec<FieldSchema>;

#[derive(Debug, Default)]
pub(crate) struct HiveSchemaBuilder {
    schema: HiveSchema,
    depth: usize,
}

impl HiveSchemaBuilder {
    /// Creates a new `HiveSchemaBuilder` from iceberg `Schema`
    pub fn from_iceberg(schema: &Schema) -> Result<HiveSchemaBuilder> {
        let mut builder = Self::default();
        visit_schema(schema, &mut builder)?;
        Ok(builder)
    }

    /// Returns the newly converted `HiveSchema`
    pub fn build(self) -> HiveSchema {
        self.schema
    }

    /// Check if is in `StructType` while traversing schema
    fn is_inside_struct(&self) -> bool {
        self.depth > 0
    }
}

impl SchemaVisitor for HiveSchemaBuilder {
    type T = String;

    fn schema(
        &mut self,
        _schema: &iceberg::spec::Schema,
        value: String,
    ) -> iceberg::Result<String> {
        Ok(value)
    }

    fn before_struct_field(
        &mut self,
        _field: &iceberg::spec::NestedFieldRef,
    ) -> iceberg::Result<()> {
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

    fn after_struct_field(
        &mut self,
        _field: &iceberg::spec::NestedFieldRef,
    ) -> iceberg::Result<()> {
        self.depth -= 1;
        Ok(())
    }

    fn field(
        &mut self,
        field: &iceberg::spec::NestedFieldRef,
        value: String,
    ) -> iceberg::Result<String> {
        if self.is_inside_struct() {
            return Ok(format!("{}:{}", field.name, value));
        }

        self.schema.push(FieldSchema {
            name: Some(field.name.clone().into()),
            r#type: Some(value.clone().into()),
            comment: field.doc.clone().map(|doc| doc.into()),
        });

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

    fn primitive(&mut self, p: &iceberg::spec::PrimitiveType) -> iceberg::Result<String> {
        let hive_type = match p {
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

        Ok(hive_type)
    }
}

