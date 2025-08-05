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

use std::collections::HashMap;

use aws_config::{BehaviorVersion, Region, SdkConfig};
use aws_sdk_glue::{
    config::Credentials,
    types::{Database, DatabaseInput, StorageDescriptor, TableInput},
};
use iceberg::spec::TableMetadata;
use iceberg::{Error, ErrorKind, Namespace, NamespaceIdent, Result};
use uuid::Uuid;

use crate::{error::from_aws_build_error, schema::GlueSchemaBuilder};

/// Property aws profile name
pub const AWS_PROFILE_NAME: &str = "profile_name";
/// Property aws region
pub const AWS_REGION_NAME: &str = "region_name";
/// Property aws access key
pub const AWS_ACCESS_KEY_ID: &str = "aws_access_key_id";
/// Property aws secret access key
pub const AWS_SECRET_ACCESS_KEY: &str = "aws_secret_access_key";
/// Property aws session token
pub const AWS_SESSION_TOKEN: &str = "aws_session_token";
/// Parameter namespace description
const DESCRIPTION: &str = "description";
/// Parameter namespace location uri
const LOCATION: &str = "location_uri";
/// Property `metadata_location` for `TableInput`
const METADATA_LOCATION: &str = "metadata_location";
/// Property `previous_metadata_location` for `TableInput`
const PREV_METADATA_LOCATION: &str = "previous_metadata_location";
/// Property external table for `TableInput`
const EXTERNAL_TABLE: &str = "EXTERNAL_TABLE";
/// Parameter key `table_type` for `TableInput`
const TABLE_TYPE: &str = "table_type";
/// Parameter value `table_type` for `TableInput`
const ICEBERG: &str = "ICEBERG";

/// Creates an aws sdk configuration based on
/// provided properties and an optional endpoint URL.
pub(crate) async fn create_sdk_config(
    properties: &HashMap<String, String>,
    endpoint_uri: Option<&String>,
) -> SdkConfig {
    let mut config = aws_config::defaults(BehaviorVersion::latest());

    if let Some(endpoint) = endpoint_uri {
        config = config.endpoint_url(endpoint)
    };

    if properties.is_empty() {
        return config.load().await;
    }

    if let (Some(access_key), Some(secret_key)) = (
        properties.get(AWS_ACCESS_KEY_ID),
        properties.get(AWS_SECRET_ACCESS_KEY),
    ) {
        let session_token = properties.get(AWS_SESSION_TOKEN).cloned();
        let credentials_provider =
            Credentials::new(access_key, secret_key, session_token, None, "properties");

        config = config.credentials_provider(credentials_provider)
    };

    if let Some(profile_name) = properties.get(AWS_PROFILE_NAME) {
        config = config.profile_name(profile_name);
    }

    if let Some(region_name) = properties.get(AWS_REGION_NAME) {
        let region = Region::new(region_name.clone());
        config = config.region(region);
    }

    config.load().await
}

/// Create `DatabaseInput` from `NamespaceIdent` and properties
pub(crate) fn convert_to_database(
    namespace: &NamespaceIdent,
    properties: &HashMap<String, String>,
) -> Result<DatabaseInput> {
    let db_name = validate_namespace(namespace)?;
    let mut builder = DatabaseInput::builder().name(db_name);

    for (k, v) in properties.iter() {
        match k.as_ref() {
            DESCRIPTION => {
                builder = builder.description(v);
            }
            LOCATION => {
                builder = builder.location_uri(v);
            }
            _ => {
                builder = builder.parameters(k, v);
            }
        }
    }

    builder.build().map_err(from_aws_build_error)
}

/// Create `Namespace` from aws sdk glue `Database`
pub(crate) fn convert_to_namespace(database: &Database) -> Namespace {
    let db_name = database.name().to_string();
    let mut properties = database
        .parameters()
        .map_or_else(HashMap::new, |p| p.clone());

    if let Some(location_uri) = database.location_uri() {
        properties.insert(LOCATION.to_string(), location_uri.to_string());
    };

    if let Some(description) = database.description() {
        properties.insert(DESCRIPTION.to_string(), description.to_string());
    }

    Namespace::with_properties(NamespaceIdent::new(db_name), properties)
}

/// Converts Iceberg table metadata into an
/// AWS Glue `TableInput` representation.
///
/// This function facilitates the integration of Iceberg tables with AWS Glue
/// by converting Iceberg table metadata into a Glue-compatible `TableInput`
/// structure.
pub(crate) fn convert_to_glue_table(
    table_name: impl Into<String>,
    metadata_location: String,
    metadata: &TableMetadata,
    properties: &HashMap<String, String>,
    prev_metadata_location: Option<String>,
) -> Result<TableInput> {
    let glue_schema = GlueSchemaBuilder::from_iceberg(metadata)?.build();

    let storage_descriptor = StorageDescriptor::builder()
        .set_columns(Some(glue_schema))
        .location(&metadata_location)
        .build();

    let mut parameters = HashMap::from([
        (TABLE_TYPE.to_string(), ICEBERG.to_string()),
        (METADATA_LOCATION.to_string(), metadata_location),
    ]);

    if let Some(prev) = prev_metadata_location {
        parameters.insert(PREV_METADATA_LOCATION.to_string(), prev);
    }

    let mut table_input_builder = TableInput::builder()
        .name(table_name)
        .set_parameters(Some(parameters))
        .storage_descriptor(storage_descriptor)
        .table_type(EXTERNAL_TABLE);

    if let Some(description) = properties.get(DESCRIPTION) {
        table_input_builder = table_input_builder.description(description);
    }

    let table_input = table_input_builder.build().map_err(from_aws_build_error)?;

    Ok(table_input)
}

/// Checks if provided `NamespaceIdent` is valid
pub(crate) fn validate_namespace(namespace: &NamespaceIdent) -> Result<String> {
    let name = namespace.as_ref();

    if name.len() != 1 {
        return Err(Error::new(
            ErrorKind::DataInvalid,
            format!(
                "Invalid database name: {:?}, hierarchical namespaces are not supported",
                namespace
            ),
        ));
    }

    let name = name[0].clone();

    if name.is_empty() {
        return Err(Error::new(
            ErrorKind::DataInvalid,
            "Invalid database, provided namespace is empty.",
        ));
    }

    Ok(name)
}

/// Get default table location from `Namespace` properties
pub(crate) fn get_default_table_location(
    namespace: &Namespace,
    db_name: impl AsRef<str>,
    table_name: impl AsRef<str>,
    warehouse: impl AsRef<str>,
) -> String {
    let properties = namespace.properties();

    match properties.get(LOCATION) {
        Some(location) => format!("{}/{}", location, table_name.as_ref()),
        None => {
            let warehouse_location = warehouse.as_ref().trim_end_matches('/');

            format!(
                "{}/{}.db/{}",
                warehouse_location,
                db_name.as_ref(),
                table_name.as_ref()
            )
        }
    }
}

/// Create metadata location from `location` and `version`
pub(crate) fn create_metadata_location(location: impl AsRef<str>, version: i32) -> Result<String> {
    if version < 0 {
        return Err(Error::new(
            ErrorKind::DataInvalid,
            format!(
                "Table metadata version: '{}' must be a non-negative integer",
                version
            ),
        ));
    };

    let version = format!("{:0>5}", version);
    let id = Uuid::new_v4();
    let metadata_location = format!(
        "{}/metadata/{}-{}.metadata.json",
        location.as_ref(),
        version,
        id
    );

    Ok(metadata_location)
}

/// Get metadata location from `GlueTable` parameters
pub(crate) fn get_metadata_location(
    parameters: &Option<HashMap<String, String>>,
) -> Result<String> {
    match parameters {
        Some(properties) => match properties.get(METADATA_LOCATION) {
            Some(location) => Ok(location.to_string()),
            None => Err(Error::new(
                ErrorKind::DataInvalid,
                format!("No '{}' set on table", METADATA_LOCATION),
            )),
        },
        None => Err(Error::new(
            ErrorKind::DataInvalid,
            "No 'parameters' set on table. Location of metadata is undefined",
        )),
    }
}

#[macro_export]
/// Extends aws sdk builder with `catalog_id` if present
macro_rules! with_catalog_id {
    ($builder:expr, $config:expr) => {{
        if let Some(catalog_id) = &$config.catalog_id {
            $builder.catalog_id(catalog_id)
        } else {
            $builder
        }
    }};
}

