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

use chrono::Utc;
use hive_metastore::{Database, PrincipalType, SerDeInfo, StorageDescriptor};
use iceberg::{spec::Schema, Error, ErrorKind, Namespace, NamespaceIdent, Result};
use pilota::{AHashMap, FastStr};
use std::collections::HashMap;
use uuid::Uuid;

use crate::schema::HiveSchemaBuilder;

/// hive.metastore.database.owner setting
const HMS_DB_OWNER: &str = "hive.metastore.database.owner";
/// hive.metastore.database.owner default setting
const HMS_DEFAULT_DB_OWNER: &str = "user.name";
/// hive.metastore.database.owner-type setting
const HMS_DB_OWNER_TYPE: &str = "hive.metastore.database.owner-type";
/// hive metatore `owner` property
const OWNER: &str = "owner";
/// hive metatore `description` property
const COMMENT: &str = "comment";
/// hive metatore `location` property
const LOCATION: &str = "location";
/// hive metatore `metadat_location` property
const METADATA_LOCATION: &str = "metadata_location";
/// hive metatore `external` property
const EXTERNAL: &str = "EXTERNAL";
/// hive metatore `external_table` property
const EXTERNAL_TABLE: &str = "EXTERNAL_TABLE";
/// hive metatore `table_type` property
const TABLE_TYPE: &str = "table_type";
/// hive metatore `SerDeInfo` serialization_lib parameter
const SERIALIZATION_LIB: &str = "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe";
/// hive metatore input format
const INPUT_FORMAT: &str = "org.apache.hadoop.mapred.FileInputFormat";
/// hive metatore output format
const OUTPUT_FORMAT: &str = "org.apache.hadoop.mapred.FileOutputFormat";

/// Returns a `Namespace` by extracting database name and properties
/// from `hive_metastore::hms::Database`
pub(crate) fn convert_to_namespace(database: &Database) -> Result<Namespace> {
    let mut properties = HashMap::new();

    let name = database
        .name
        .as_ref()
        .ok_or_else(|| Error::new(ErrorKind::DataInvalid, "Database name must be specified"))?
        .to_string();

    if let Some(description) = &database.description {
        properties.insert(COMMENT.to_string(), description.to_string());
    };

    if let Some(location) = &database.location_uri {
        properties.insert(LOCATION.to_string(), location.to_string());
    };

    if let Some(owner) = &database.owner_name {
        properties.insert(HMS_DB_OWNER.to_string(), owner.to_string());
    };

    if let Some(owner_type) = &database.owner_type {
        let value = match owner_type {
            PrincipalType::User => "User",
            PrincipalType::Group => "Group",
            PrincipalType::Role => "Role",
        };

        properties.insert(HMS_DB_OWNER_TYPE.to_string(), value.to_string());
    };

    if let Some(params) = &database.parameters {
        params.iter().for_each(|(k, v)| {
            properties.insert(k.clone().into(), v.clone().into());
        });
    };

    Ok(Namespace::with_properties(
        NamespaceIdent::new(name),
        properties,
    ))
}

/// Converts name and properties into `hive_metastore::hms::Database`
/// after validating the `namespace` and `owner-settings`.
pub(crate) fn convert_to_database(
    namespace: &NamespaceIdent,
    properties: &HashMap<String, String>,
) -> Result<Database> {
    let name = validate_namespace(namespace)?;
    validate_owner_settings(properties)?;

    let mut db = Database::default();
    let mut parameters = AHashMap::new();

    db.name = Some(name.into());

    for (k, v) in properties {
        match k.as_str() {
            COMMENT => db.description = Some(v.clone().into()),
            LOCATION => db.location_uri = Some(format_location_uri(v.clone()).into()),
            HMS_DB_OWNER => db.owner_name = Some(v.clone().into()),
            HMS_DB_OWNER_TYPE => {
                let owner_type = match v.to_lowercase().as_str() {
                    "user" => PrincipalType::User,
                    "group" => PrincipalType::Group,
                    "role" => PrincipalType::Role,
                    _ => {
                        return Err(Error::new(
                            ErrorKind::DataInvalid,
                            format!("Invalid value for setting 'owner_type': {}", v),
                        ))
                    }
                };
                db.owner_type = Some(owner_type);
            }
            _ => {
                parameters.insert(
                    FastStr::from_string(k.clone()),
                    FastStr::from_string(v.clone()),
                );
            }
        }
    }

    db.parameters = Some(parameters);

    // Set default owner, if none provided
    // https://github.com/apache/iceberg/blob/main/hive-metastore/src/main/java/org/apache/iceberg/hive/HiveHadoopUtil.java#L44
    if db.owner_name.is_none() {
        db.owner_name = Some(HMS_DEFAULT_DB_OWNER.into());
        db.owner_type = Some(PrincipalType::User);
    }

    Ok(db)
}

pub(crate) fn convert_to_hive_table(
    db_name: String,
    schema: &Schema,
    table_name: String,
    location: String,
    metadata_location: String,
    properties: &HashMap<String, String>,
) -> Result<hive_metastore::Table> {
    let serde_info = SerDeInfo {
        serialization_lib: Some(SERIALIZATION_LIB.into()),
        ..Default::default()
    };

    let hive_schema = HiveSchemaBuilder::from_iceberg(schema)?.build();

    let storage_descriptor = StorageDescriptor {
        location: Some(location.into()),
        cols: Some(hive_schema),
        input_format: Some(INPUT_FORMAT.into()),
        output_format: Some(OUTPUT_FORMAT.into()),
        serde_info: Some(serde_info),
        ..Default::default()
    };

    let parameters = AHashMap::from([
        (FastStr::from(EXTERNAL), FastStr::from("TRUE")),
        (FastStr::from(TABLE_TYPE), FastStr::from("ICEBERG")),
        (
            FastStr::from(METADATA_LOCATION),
            FastStr::from(metadata_location),
        ),
    ]);

    let current_time_ms = get_current_time()?;
    let owner = properties
        .get(OWNER)
        .map_or(HMS_DEFAULT_DB_OWNER.to_string(), |v| v.into());

    Ok(hive_metastore::Table {
        table_name: Some(table_name.into()),
        db_name: Some(db_name.into()),
        table_type: Some(EXTERNAL_TABLE.into()),
        owner: Some(owner.into()),
        create_time: Some(current_time_ms),
        last_access_time: Some(current_time_ms),
        sd: Some(storage_descriptor),
        parameters: Some(parameters),
        ..Default::default()
    })
}

/// Checks if provided `NamespaceIdent` is valid.
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
    table_name: impl AsRef<str>,
    warehouse: impl AsRef<str>,
) -> String {
    let properties = namespace.properties();

    let location = match properties.get(LOCATION) {
        Some(location) => location,
        None => warehouse.as_ref(),
    };

    format!("{}/{}", location, table_name.as_ref())
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

/// Get metadata location from `HiveTable` parameters
pub(crate) fn get_metadata_location(
    parameters: &Option<AHashMap<FastStr, FastStr>>,
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

/// Formats location_uri by e.g. removing trailing slashes.
fn format_location_uri(location: String) -> String {
    let mut location = location;

    if !location.starts_with('/') {
        location = format!("/{}", location);
    }

    if location.ends_with('/') && location.len() > 1 {
        location.pop();
    }

    location
}

/// Checks if `owner-settings` are valid.
/// If `owner_type` is set, then `owner` must also be set.
fn validate_owner_settings(properties: &HashMap<String, String>) -> Result<()> {
    let owner_is_set = properties.get(HMS_DB_OWNER).is_some();
    let owner_type_is_set = properties.get(HMS_DB_OWNER_TYPE).is_some();

    if owner_type_is_set && !owner_is_set {
        return Err(Error::new(
            ErrorKind::DataInvalid,
            format!(
                "Setting '{}' without setting '{}' is not allowed",
                HMS_DB_OWNER_TYPE, HMS_DB_OWNER
            ),
        ));
    }

    Ok(())
}

fn get_current_time() -> Result<i32> {
    let now = Utc::now();
    now.timestamp().try_into().map_err(|_| {
        Error::new(
            ErrorKind::Unexpected,
            "Current time is out of range for i32",
        )
    })
}

