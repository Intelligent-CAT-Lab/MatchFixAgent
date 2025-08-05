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

//! Defines the [table metadata](https://iceberg.apache.org/spec/#table-metadata).
//! The main struct here is [TableMetadataV2] which defines the data for a table.

use serde::{Deserialize, Serialize};
use serde_repr::{Deserialize_repr, Serialize_repr};
use std::cmp::Ordering;
use std::fmt::{Display, Formatter};
use std::{collections::HashMap, sync::Arc};
use uuid::Uuid;

use super::{
    snapshot::{Snapshot, SnapshotReference, SnapshotRetention},
    PartitionSpecRef, SchemaId, SchemaRef, SnapshotRef, SortOrderRef,
};
use super::{PartitionSpec, SortOrder};

use _serde::TableMetadataEnum;

use crate::error::Result;
use crate::{Error, ErrorKind, TableCreation};
use chrono::{DateTime, TimeZone, Utc};

static MAIN_BRANCH: &str = "main";
static DEFAULT_SPEC_ID: i32 = 0;
static DEFAULT_SORT_ORDER_ID: i64 = 0;

pub(crate) static EMPTY_SNAPSHOT_ID: i64 = -1;
pub(crate) static INITIAL_SEQUENCE_NUMBER: i64 = 0;

/// Reference to [`TableMetadata`].
pub type TableMetadataRef = Arc<TableMetadata>;

#[derive(Debug, PartialEq, Deserialize, Eq, Clone)]
#[serde(try_from = "TableMetadataEnum")]
/// Fields for the version 2 of the table metadata.
///
/// We assume that this data structure is always valid, so we will panic when invalid error happens.
/// We check the validity of this data structure when constructing.
pub struct TableMetadata {
    /// Integer Version for the format.
    pub(crate) format_version: FormatVersion,
    /// A UUID that identifies the table
    pub(crate) table_uuid: Uuid,
    /// Location tables base location
    pub(crate) location: String,
    /// The tables highest sequence number
    pub(crate) last_sequence_number: i64,
    /// Timestamp in milliseconds from the unix epoch when the table was last updated.
    pub(crate) last_updated_ms: i64,
    /// An integer; the highest assigned column ID for the table.
    pub(crate) last_column_id: i32,
    /// A list of schemas, stored as objects with schema-id.
    pub(crate) schemas: HashMap<i32, SchemaRef>,
    /// ID of the table’s current schema.
    pub(crate) current_schema_id: i32,
    /// A list of partition specs, stored as full partition spec objects.
    pub(crate) partition_specs: HashMap<i32, PartitionSpecRef>,
    /// ID of the “current” spec that writers should use by default.
    pub(crate) default_spec_id: i32,
    /// An integer; the highest assigned partition field ID across all partition specs for the table.
    pub(crate) last_partition_id: i32,
    ///A string to string map of table properties. This is used to control settings that
    /// affect reading and writing and is not intended to be used for arbitrary metadata.
    /// For example, commit.retry.num-retries is used to control the number of commit retries.
    pub(crate) properties: HashMap<String, String>,
    /// long ID of the current table snapshot; must be the same as the current
    /// ID of the main branch in refs.
    pub(crate) current_snapshot_id: Option<i64>,
    ///A list of valid snapshots. Valid snapshots are snapshots for which all
    /// data files exist in the file system. A data file must not be deleted
    /// from the file system until the last snapshot in which it was listed is
    /// garbage collected.
    pub(crate) snapshots: HashMap<i64, SnapshotRef>,
    /// A list (optional) of timestamp and snapshot ID pairs that encodes changes
    /// to the current snapshot for the table. Each time the current-snapshot-id
    /// is changed, a new entry should be added with the last-updated-ms
    /// and the new current-snapshot-id. When snapshots are expired from
    /// the list of valid snapshots, all entries before a snapshot that has
    /// expired should be removed.
    pub(crate) snapshot_log: Vec<SnapshotLog>,

    /// A list (optional) of timestamp and metadata file location pairs
    /// that encodes changes to the previous metadata files for the table.
    /// Each time a new metadata file is created, a new entry of the
    /// previous metadata file location should be added to the list.
    /// Tables can be configured to remove oldest metadata log entries and
    /// keep a fixed-size log of the most recent entries after a commit.
    pub(crate) metadata_log: Vec<MetadataLog>,

    /// A list of sort orders, stored as full sort order objects.
    pub(crate) sort_orders: HashMap<i64, SortOrderRef>,
    /// Default sort order id of the table. Note that this could be used by
    /// writers, but is not used when reading because reads use the specs
    /// stored in manifest files.
    pub(crate) default_sort_order_id: i64,
    ///A map of snapshot references. The map keys are the unique snapshot reference
    /// names in the table, and the map values are snapshot reference objects.
    /// There is always a main branch reference pointing to the current-snapshot-id
    /// even if the refs map is null.
    pub(crate) refs: HashMap<String, SnapshotReference>,
}

impl TableMetadata {
    /// Returns format version of this metadata.
    #[inline]
    pub fn format_version(&self) -> FormatVersion {
        self.format_version
    }

    /// Returns uuid of current table.
    #[inline]
    pub fn uuid(&self) -> Uuid {
        self.table_uuid
    }

    /// Returns table location.
    #[inline]
    pub fn location(&self) -> &str {
        self.location.as_str()
    }

    /// Returns last sequence number.
    #[inline]
    pub fn last_sequence_number(&self) -> i64 {
        self.last_sequence_number
    }

    /// Returns last updated time.
    #[inline]
    pub fn last_updated_ms(&self) -> DateTime<Utc> {
        Utc.timestamp_millis_opt(self.last_updated_ms).unwrap()
    }

    /// Returns schemas
    #[inline]
    pub fn schemas_iter(&self) -> impl Iterator<Item = &SchemaRef> {
        self.schemas.values()
    }

    /// Lookup schema by id.
    #[inline]
    pub fn schema_by_id(&self, schema_id: SchemaId) -> Option<&SchemaRef> {
        self.schemas.get(&schema_id)
    }

    /// Get current schema
    #[inline]
    pub fn current_schema(&self) -> &SchemaRef {
        self.schema_by_id(self.current_schema_id)
            .expect("Current schema id set, but not found in table metadata")
    }

    /// Returns all partition specs.
    #[inline]
    pub fn partition_specs_iter(&self) -> impl Iterator<Item = &PartitionSpecRef> {
        self.partition_specs.values()
    }

    /// Lookup partition spec by id.
    #[inline]
    pub fn partition_spec_by_id(&self, spec_id: i32) -> Option<&PartitionSpecRef> {
        self.partition_specs.get(&spec_id)
    }

    /// Get default partition spec
    #[inline]
    pub fn default_partition_spec(&self) -> Option<&PartitionSpecRef> {
        if self.default_spec_id == DEFAULT_SPEC_ID {
            self.partition_spec_by_id(DEFAULT_SPEC_ID)
        } else {
            Some(
                self.partition_spec_by_id(self.default_spec_id)
                    .expect("Default partition spec id set, but not found in table metadata"),
            )
        }
    }

    /// Returns all snapshots
    #[inline]
    pub fn snapshots(&self) -> impl Iterator<Item = &SnapshotRef> {
        self.snapshots.values()
    }

    /// Lookup snapshot by id.
    #[inline]
    pub fn snapshot_by_id(&self, snapshot_id: i64) -> Option<&SnapshotRef> {
        self.snapshots.get(&snapshot_id)
    }

    /// Returns snapshot history.
    #[inline]
    pub fn history(&self) -> &[SnapshotLog] {
        &self.snapshot_log
    }

    /// Get current snapshot
    #[inline]
    pub fn current_snapshot(&self) -> Option<&SnapshotRef> {
        self.current_snapshot_id.map(|s| {
            self.snapshot_by_id(s)
                .expect("Current snapshot id has been set, but doesn't exist in metadata")
        })
    }

    /// Return all sort orders.
    #[inline]
    pub fn sort_orders_iter(&self) -> impl Iterator<Item = &SortOrderRef> {
        self.sort_orders.values()
    }

    /// Lookup sort order by id.
    #[inline]
    pub fn sort_order_by_id(&self, sort_order_id: i64) -> Option<&SortOrderRef> {
        self.sort_orders.get(&sort_order_id)
    }

    /// Returns default sort order id.
    #[inline]
    pub fn default_sort_order(&self) -> Option<&SortOrderRef> {
        if self.default_sort_order_id == DEFAULT_SORT_ORDER_ID {
            self.sort_orders.get(&DEFAULT_SORT_ORDER_ID)
        } else {
            Some(
                self.sort_orders
                    .get(&self.default_sort_order_id)
                    .expect("Default order id has been set, but not found in table metadata!"),
            )
        }
    }

    /// Returns properties of table.
    #[inline]
    pub fn properties(&self) -> &HashMap<String, String> {
        &self.properties
    }

    /// Append snapshot to table
    pub fn append_snapshot(&mut self, snapshot: Snapshot) {
        self.last_updated_ms = snapshot.timestamp().timestamp_millis();
        self.last_sequence_number = snapshot.sequence_number();

        self.refs
            .entry(MAIN_BRANCH.to_string())
            .and_modify(|s| {
                s.snapshot_id = snapshot.snapshot_id();
            })
            .or_insert_with(|| {
                SnapshotReference::new(
                    snapshot.snapshot_id(),
                    SnapshotRetention::Branch {
                        min_snapshots_to_keep: None,
                        max_snapshot_age_ms: None,
                        max_ref_age_ms: None,
                    },
                )
            });

        self.snapshot_log.push(snapshot.log());
        self.snapshots
            .insert(snapshot.snapshot_id(), Arc::new(snapshot));
    }
}

/// Manipulating table metadata.
pub struct TableMetadataBuilder(TableMetadata);

impl TableMetadataBuilder {
    /// Creates a new table metadata builder from the given table metadata.
    pub fn new(origin: TableMetadata) -> Self {
        Self(origin)
    }

    /// Creates a new table metadata builder from the given table creation.
    pub fn from_table_creation(table_creation: TableCreation) -> Result<Self> {
        let TableCreation {
            name: _,
            location,
            schema,
            partition_spec,
            sort_order,
            properties,
        } = table_creation;

        let partition_specs = match partition_spec {
            Some(_) => {
                return Err(Error::new(
                    ErrorKind::FeatureUnsupported,
                    "Can't create table with partition spec now",
                ))
            }
            None => HashMap::from([(
                DEFAULT_SPEC_ID,
                Arc::new(PartitionSpec {
                    spec_id: DEFAULT_SPEC_ID,
                    fields: vec![],
                }),
            )]),
        };

        let sort_orders = match sort_order {
            Some(_) => {
                return Err(Error::new(
                    ErrorKind::FeatureUnsupported,
                    "Can't create table with sort order now",
                ))
            }
            None => HashMap::from([(
                DEFAULT_SORT_ORDER_ID,
                Arc::new(SortOrder {
                    order_id: DEFAULT_SORT_ORDER_ID,
                    fields: vec![],
                }),
            )]),
        };

        let table_metadata = TableMetadata {
            format_version: FormatVersion::V2,
            table_uuid: Uuid::new_v4(),
            location: location.ok_or_else(|| {
                Error::new(
                    ErrorKind::DataInvalid,
                    "Can't create table without location",
                )
            })?,
            last_sequence_number: 0,
            last_updated_ms: Utc::now().timestamp_millis(),
            last_column_id: schema.highest_field_id(),
            current_schema_id: schema.schema_id(),
            schemas: HashMap::from([(schema.schema_id(), Arc::new(schema))]),
            partition_specs,
            default_spec_id: DEFAULT_SPEC_ID,
            last_partition_id: 0,
            properties,
            current_snapshot_id: None,
            snapshots: Default::default(),
            snapshot_log: vec![],
            sort_orders,
            metadata_log: vec![],
            default_sort_order_id: DEFAULT_SORT_ORDER_ID,
            refs: Default::default(),
        };

        Ok(Self(table_metadata))
    }

    /// Changes uuid of table metadata.
    pub fn assign_uuid(mut self, uuid: Uuid) -> Result<Self> {
        self.0.table_uuid = uuid;
        Ok(self)
    }

    /// Returns the new table metadata after changes.
    pub fn build(self) -> Result<TableMetadata> {
        Ok(self.0)
    }
}

pub(super) mod _serde {
    /// This is a helper module that defines types to help with serialization/deserialization.
    /// For deserialization the input first gets read into either the [TableMetadataV1] or [TableMetadataV2] struct
    /// and then converted into the [TableMetadata] struct. Serialization works the other way around.
    /// [TableMetadataV1] and [TableMetadataV2] are internal struct that are only used for serialization and deserialization.
    use std::{collections::HashMap, sync::Arc};

    use itertools::Itertools;
    use serde::{Deserialize, Serialize};
    use uuid::Uuid;

    use crate::spec::{Snapshot, EMPTY_SNAPSHOT_ID};
    use crate::{
        spec::{
            schema::_serde::{SchemaV1, SchemaV2},
            snapshot::_serde::{SnapshotV1, SnapshotV2},
            PartitionField, PartitionSpec, Schema, SnapshotReference, SnapshotRetention, SortOrder,
        },
        Error, ErrorKind,
    };

    use super::{
        FormatVersion, MetadataLog, SnapshotLog, TableMetadata, DEFAULT_SORT_ORDER_ID,
        DEFAULT_SPEC_ID, MAIN_BRANCH,
    };

    #[derive(Debug, Serialize, Deserialize, PartialEq, Eq)]
    #[serde(untagged)]
    pub(super) enum TableMetadataEnum {
        V2(TableMetadataV2),
        V1(TableMetadataV1),
    }

    #[derive(Debug, Serialize, Deserialize, PartialEq, Eq)]
    #[serde(rename_all = "kebab-case")]
    /// Defines the structure of a v2 table metadata for serialization/deserialization
    pub(super) struct TableMetadataV2 {
        pub format_version: VersionNumber<2>,
        pub table_uuid: Uuid,
        pub location: String,
        pub last_sequence_number: i64,
        pub last_updated_ms: i64,
        pub last_column_id: i32,
        pub schemas: Vec<SchemaV2>,
        pub current_schema_id: i32,
        pub partition_specs: Vec<PartitionSpec>,
        pub default_spec_id: i32,
        pub last_partition_id: i32,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub properties: Option<HashMap<String, String>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub current_snapshot_id: Option<i64>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub snapshots: Option<Vec<SnapshotV2>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub snapshot_log: Option<Vec<SnapshotLog>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub metadata_log: Option<Vec<MetadataLog>>,
        pub sort_orders: Vec<SortOrder>,
        pub default_sort_order_id: i64,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub refs: Option<HashMap<String, SnapshotReference>>,
    }

    #[derive(Debug, Serialize, Deserialize, PartialEq, Eq)]
    #[serde(rename_all = "kebab-case")]
    /// Defines the structure of a v1 table metadata for serialization/deserialization
    pub(super) struct TableMetadataV1 {
        pub format_version: VersionNumber<1>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub table_uuid: Option<Uuid>,
        pub location: String,
        pub last_updated_ms: i64,
        pub last_column_id: i32,
        pub schema: SchemaV1,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub schemas: Option<Vec<SchemaV1>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub current_schema_id: Option<i32>,
        pub partition_spec: Vec<PartitionField>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub partition_specs: Option<Vec<PartitionSpec>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub default_spec_id: Option<i32>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub last_partition_id: Option<i32>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub properties: Option<HashMap<String, String>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub current_snapshot_id: Option<i64>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub snapshots: Option<Vec<SnapshotV1>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub snapshot_log: Option<Vec<SnapshotLog>>,
        #[serde(skip_serializing_if = "Option::is_none")]
        pub metadata_log: Option<Vec<MetadataLog>>,
        pub sort_orders: Option<Vec<SortOrder>>,
        pub default_sort_order_id: Option<i64>,
    }

    /// Helper to serialize and deserialize the format version.
    #[derive(Debug, PartialEq, Eq)]
    pub(super) struct VersionNumber<const V: u8>;

    impl Serialize for TableMetadata {
        fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
        where
            S: serde::Serializer,
        {
            // we must do a clone here
            let table_metadata_enum: TableMetadataEnum =
                self.clone().try_into().map_err(serde::ser::Error::custom)?;

            table_metadata_enum.serialize(serializer)
        }
    }

    impl<const V: u8> Serialize for VersionNumber<V> {
        fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
        where
            S: serde::Serializer,
        {
            serializer.serialize_u8(V)
        }
    }

    impl<'de, const V: u8> Deserialize<'de> for VersionNumber<V> {
        fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
        where
            D: serde::Deserializer<'de>,
        {
            let value = u8::deserialize(deserializer)?;
            if value == V {
                Ok(VersionNumber::<V>)
            } else {
                Err(serde::de::Error::custom("Invalid Version"))
            }
        }
    }

    impl TryFrom<TableMetadataEnum> for TableMetadata {
        type Error = Error;
        fn try_from(value: TableMetadataEnum) -> Result<Self, Error> {
            match value {
                TableMetadataEnum::V2(value) => value.try_into(),
                TableMetadataEnum::V1(value) => value.try_into(),
            }
        }
    }

    impl TryFrom<TableMetadata> for TableMetadataEnum {
        type Error = Error;
        fn try_from(value: TableMetadata) -> Result<Self, Error> {
            Ok(match value.format_version {
                FormatVersion::V2 => TableMetadataEnum::V2(value.into()),
                FormatVersion::V1 => TableMetadataEnum::V1(value.try_into()?),
            })
        }
    }

    impl TryFrom<TableMetadataV2> for TableMetadata {
        type Error = Error;
        fn try_from(value: TableMetadataV2) -> Result<Self, self::Error> {
            let current_snapshot_id = if let &Some(-1) = &value.current_snapshot_id {
                None
            } else {
                value.current_snapshot_id
            };
            let schemas = HashMap::from_iter(
                value
                    .schemas
                    .into_iter()
                    .map(|schema| Ok((schema.schema_id, Arc::new(schema.try_into()?))))
                    .collect::<Result<Vec<_>, Error>>()?,
            );
            Ok(TableMetadata {
                format_version: FormatVersion::V2,
                table_uuid: value.table_uuid,
                location: value.location,
                last_sequence_number: value.last_sequence_number,
                last_updated_ms: value.last_updated_ms,
                last_column_id: value.last_column_id,
                current_schema_id: if schemas.keys().contains(&value.current_schema_id) {
                    Ok(value.current_schema_id)
                } else {
                    Err(self::Error::new(
                        ErrorKind::DataInvalid,
                        format!(
                            "No schema exists with the current schema id {}.",
                            value.current_schema_id
                        ),
                    ))
                }?,
                schemas,
                partition_specs: HashMap::from_iter(
                    value
                        .partition_specs
                        .into_iter()
                        .map(|x| (x.spec_id, Arc::new(x))),
                ),
                default_spec_id: value.default_spec_id,
                last_partition_id: value.last_partition_id,
                properties: value.properties.unwrap_or_default(),
                current_snapshot_id,
                snapshots: value
                    .snapshots
                    .map(|snapshots| {
                        HashMap::from_iter(
                            snapshots
                                .into_iter()
                                .map(|x| (x.snapshot_id, Arc::new(x.into()))),
                        )
                    })
                    .unwrap_or_default(),
                snapshot_log: value.snapshot_log.unwrap_or_default(),
                metadata_log: value.metadata_log.unwrap_or_default(),
                sort_orders: HashMap::from_iter(
                    value
                        .sort_orders
                        .into_iter()
                        .map(|x| (x.order_id, Arc::new(x))),
                ),
                default_sort_order_id: value.default_sort_order_id,
                refs: value.refs.unwrap_or_else(|| {
                    if let Some(snapshot_id) = current_snapshot_id {
                        HashMap::from_iter(vec![(
                            MAIN_BRANCH.to_string(),
                            SnapshotReference {
                                snapshot_id,
                                retention: SnapshotRetention::Branch {
                                    min_snapshots_to_keep: None,
                                    max_snapshot_age_ms: None,
                                    max_ref_age_ms: None,
                                },
                            },
                        )])
                    } else {
                        HashMap::new()
                    }
                }),
            })
        }
    }

    impl TryFrom<TableMetadataV1> for TableMetadata {
        type Error = Error;
        fn try_from(value: TableMetadataV1) -> Result<Self, Error> {
            let schemas = value
                .schemas
                .map(|schemas| {
                    Ok::<_, Error>(HashMap::from_iter(
                        schemas
                            .into_iter()
                            .enumerate()
                            .map(|(i, schema)| {
                                Ok((
                                    schema.schema_id.unwrap_or(i as i32),
                                    Arc::new(schema.try_into()?),
                                ))
                            })
                            .collect::<Result<Vec<_>, Error>>()?
                            .into_iter(),
                    ))
                })
                .or_else(|| {
                    Some(value.schema.try_into().map(|schema: Schema| {
                        HashMap::from_iter(vec![(schema.schema_id(), Arc::new(schema))])
                    }))
                })
                .transpose()?
                .unwrap_or_default();
            let partition_specs = HashMap::from_iter(
                value
                    .partition_specs
                    .unwrap_or_else(|| {
                        vec![PartitionSpec {
                            spec_id: DEFAULT_SPEC_ID,
                            fields: value.partition_spec,
                        }]
                    })
                    .into_iter()
                    .map(|x| (x.spec_id, Arc::new(x))),
            );
            Ok(TableMetadata {
                format_version: FormatVersion::V1,
                table_uuid: value.table_uuid.unwrap_or_default(),
                location: value.location,
                last_sequence_number: 0,
                last_updated_ms: value.last_updated_ms,
                last_column_id: value.last_column_id,
                current_schema_id: value
                    .current_schema_id
                    .unwrap_or_else(|| schemas.keys().copied().max().unwrap_or_default()),
                default_spec_id: value
                    .default_spec_id
                    .unwrap_or_else(|| partition_specs.keys().copied().max().unwrap_or_default()),
                last_partition_id: value
                    .last_partition_id
                    .unwrap_or_else(|| partition_specs.keys().copied().max().unwrap_or_default()),
                partition_specs,
                schemas,

                properties: value.properties.unwrap_or_default(),
                current_snapshot_id: if let &Some(id) = &value.current_snapshot_id {
                    if id == EMPTY_SNAPSHOT_ID {
                        None
                    } else {
                        Some(id)
                    }
                } else {
                    value.current_snapshot_id
                },
                snapshots: value
                    .snapshots
                    .map(|snapshots| {
                        Ok::<_, Error>(HashMap::from_iter(
                            snapshots
                                .into_iter()
                                .map(|x| Ok((x.snapshot_id, Arc::new(x.try_into()?))))
                                .collect::<Result<Vec<_>, Error>>()?,
                        ))
                    })
                    .transpose()?
                    .unwrap_or_default(),
                snapshot_log: value.snapshot_log.unwrap_or_default(),
                metadata_log: value.metadata_log.unwrap_or_default(),
                sort_orders: match value.sort_orders {
                    Some(sort_orders) => HashMap::from_iter(
                        sort_orders.into_iter().map(|x| (x.order_id, Arc::new(x))),
                    ),
                    None => HashMap::new(),
                },
                default_sort_order_id: value.default_sort_order_id.unwrap_or(DEFAULT_SORT_ORDER_ID),
                refs: HashMap::from_iter(vec![(
                    MAIN_BRANCH.to_string(),
                    SnapshotReference {
                        snapshot_id: value.current_snapshot_id.unwrap_or_default(),
                        retention: SnapshotRetention::Branch {
                            min_snapshots_to_keep: None,
                            max_snapshot_age_ms: None,
                            max_ref_age_ms: None,
                        },
                    },
                )]),
            })
        }
    }

    impl From<TableMetadata> for TableMetadataV2 {
        fn from(v: TableMetadata) -> Self {
            TableMetadataV2 {
                format_version: VersionNumber::<2>,
                table_uuid: v.table_uuid,
                location: v.location,
                last_sequence_number: v.last_sequence_number,
                last_updated_ms: v.last_updated_ms,
                last_column_id: v.last_column_id,
                schemas: v
                    .schemas
                    .into_values()
                    .map(|x| {
                        Arc::try_unwrap(x)
                            .unwrap_or_else(|schema| schema.as_ref().clone())
                            .into()
                    })
                    .collect(),
                current_schema_id: v.current_schema_id,
                partition_specs: v
                    .partition_specs
                    .into_values()
                    .map(|x| Arc::try_unwrap(x).unwrap_or_else(|s| s.as_ref().clone()))
                    .collect(),
                default_spec_id: v.default_spec_id,
                last_partition_id: v.last_partition_id,
                properties: Some(v.properties),
                current_snapshot_id: v.current_snapshot_id.or(Some(-1)),
                snapshots: if v.snapshots.is_empty() {
                    Some(vec![])
                } else {
                    Some(
                        v.snapshots
                            .into_values()
                            .map(|x| {
                                Arc::try_unwrap(x)
                                    .unwrap_or_else(|snapshot| snapshot.as_ref().clone())
                                    .into()
                            })
                            .collect(),
                    )
                },
                snapshot_log: if v.snapshot_log.is_empty() {
                    None
                } else {
                    Some(v.snapshot_log)
                },
                metadata_log: if v.metadata_log.is_empty() {
                    None
                } else {
                    Some(v.metadata_log)
                },
                sort_orders: v
                    .sort_orders
                    .into_values()
                    .map(|x| Arc::try_unwrap(x).unwrap_or_else(|s| s.as_ref().clone()))
                    .collect(),
                default_sort_order_id: v.default_sort_order_id,
                refs: Some(v.refs),
            }
        }
    }

    impl TryFrom<TableMetadata> for TableMetadataV1 {
        type Error = Error;
        fn try_from(v: TableMetadata) -> Result<Self, Error> {
            Ok(TableMetadataV1 {
                format_version: VersionNumber::<1>,
                table_uuid: Some(v.table_uuid),
                location: v.location,
                last_updated_ms: v.last_updated_ms,
                last_column_id: v.last_column_id,
                schema: v
                    .schemas
                    .get(&v.current_schema_id)
                    .ok_or(Error::new(
                        ErrorKind::Unexpected,
                        "current_schema_id not found in schemas",
                    ))?
                    .as_ref()
                    .clone()
                    .into(),
                schemas: Some(
                    v.schemas
                        .into_values()
                        .map(|x| {
                            Arc::try_unwrap(x)
                                .unwrap_or_else(|schema| schema.as_ref().clone())
                                .into()
                        })
                        .collect(),
                ),
                current_schema_id: Some(v.current_schema_id),
                partition_spec: v
                    .partition_specs
                    .get(&v.default_spec_id)
                    .map(|x| x.fields.clone())
                    .unwrap_or_default(),
                partition_specs: Some(
                    v.partition_specs
                        .into_values()
                        .map(|x| Arc::try_unwrap(x).unwrap_or_else(|s| s.as_ref().clone()))
                        .collect(),
                ),
                default_spec_id: Some(v.default_spec_id),
                last_partition_id: Some(v.last_partition_id),
                properties: if v.properties.is_empty() {
                    None
                } else {
                    Some(v.properties)
                },
                current_snapshot_id: v.current_snapshot_id.or(Some(-1)),
                snapshots: if v.snapshots.is_empty() {
                    None
                } else {
                    Some(
                        v.snapshots
                            .into_values()
                            .map(|x| Snapshot::clone(&x).into())
                            .collect(),
                    )
                },
                snapshot_log: if v.snapshot_log.is_empty() {
                    None
                } else {
                    Some(v.snapshot_log)
                },
                metadata_log: if v.metadata_log.is_empty() {
                    None
                } else {
                    Some(v.metadata_log)
                },
                sort_orders: Some(
                    v.sort_orders
                        .into_values()
                        .map(|s| Arc::try_unwrap(s).unwrap_or_else(|s| s.as_ref().clone()))
                        .collect(),
                ),
                default_sort_order_id: Some(v.default_sort_order_id),
            })
        }
    }
}

#[derive(Debug, Serialize_repr, Deserialize_repr, PartialEq, Eq, Clone, Copy)]
#[repr(u8)]
/// Iceberg format version
pub enum FormatVersion {
    /// Iceberg spec version 1
    V1 = 1u8,
    /// Iceberg spec version 2
    V2 = 2u8,
}

impl PartialOrd for FormatVersion {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for FormatVersion {
    fn cmp(&self, other: &Self) -> Ordering {
        (*self as u8).cmp(&(*other as u8))
    }
}

impl Display for FormatVersion {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            FormatVersion::V1 => write!(f, "v1"),
            FormatVersion::V2 => write!(f, "v2"),
        }
    }
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Clone)]
#[serde(rename_all = "kebab-case")]
/// Encodes changes to the previous metadata files for the table
pub struct MetadataLog {
    /// The file for the log.
    pub metadata_file: String,
    /// Time new metadata was created
    pub timestamp_ms: i64,
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Clone)]
#[serde(rename_all = "kebab-case")]
/// A log of when each snapshot was made.
pub struct SnapshotLog {
    /// Id of the snapshot.
    pub snapshot_id: i64,
    /// Last updated timestamp
    pub timestamp_ms: i64,
}

impl SnapshotLog {
    /// Returns the last updated timestamp as a DateTime<Utc> with millisecond precision
    pub fn timestamp(self) -> DateTime<Utc> {
        Utc.timestamp_millis_opt(self.timestamp_ms).unwrap()
    }
}

