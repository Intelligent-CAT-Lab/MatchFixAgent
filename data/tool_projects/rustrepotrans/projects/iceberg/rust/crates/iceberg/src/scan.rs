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

//! Table scan api.

use crate::arrow::ArrowReaderBuilder;
use crate::expr::visitors::expression_evaluator::ExpressionEvaluator;
use crate::expr::visitors::inclusive_metrics_evaluator::InclusiveMetricsEvaluator;
use crate::expr::visitors::inclusive_projection::InclusiveProjection;
use crate::expr::visitors::manifest_evaluator::ManifestEvaluator;
use crate::expr::{Bind, BoundPredicate, Predicate};
use crate::io::FileIO;
use crate::spec::{
    DataContentType, ManifestContentType, ManifestFile, Schema, SchemaRef, SnapshotRef,
    TableMetadataRef,
};
use crate::table::Table;
use crate::{Error, ErrorKind, Result};
use arrow_array::RecordBatch;
use async_stream::try_stream;
use futures::stream::BoxStream;
use futures::StreamExt;
use serde::{Deserialize, Serialize};
use std::collections::hash_map::Entry;
use std::collections::HashMap;
use std::sync::Arc;

/// A stream of [`FileScanTask`].
pub type FileScanTaskStream = BoxStream<'static, Result<FileScanTask>>;
/// A stream of arrow [`RecordBatch`]es.
pub type ArrowRecordBatchStream = BoxStream<'static, Result<RecordBatch>>;

/// Builder to create table scan.
pub struct TableScanBuilder<'a> {
    table: &'a Table,
    // Empty column names means to select all columns
    column_names: Vec<String>,
    predicates: Option<Predicate>,
    snapshot_id: Option<i64>,
    batch_size: Option<usize>,
    case_sensitive: bool,
    filter: Option<Predicate>,
}

impl<'a> TableScanBuilder<'a> {
    pub(crate) fn new(table: &'a Table) -> Self {
        Self {
            table,
            column_names: vec![],
            predicates: None,
            snapshot_id: None,
            batch_size: None,
            case_sensitive: true,
            filter: None,
        }
    }

    /// Sets the desired size of batches in the response
    /// to something other than the default
    pub fn with_batch_size(mut self, batch_size: Option<usize>) -> Self {
        self.batch_size = batch_size;
        self
    }

    /// Sets the scan's case sensitivity
    pub fn with_case_sensitive(mut self, case_sensitive: bool) -> Self {
        self.case_sensitive = case_sensitive;
        self
    }

    /// Specifies a predicate to use as a filter
    pub fn with_filter(mut self, predicate: Predicate) -> Self {
        // calls rewrite_not to remove Not nodes, which must be absent
        // when applying the manifest evaluator
        self.filter = Some(predicate.rewrite_not());
        self
    }

    /// Select all columns.
    pub fn select_all(mut self) -> Self {
        self.column_names.clear();
        self
    }

    /// Add a predicate to the scan. The scan will only return rows that match the predicate.
    pub fn filter(mut self, predicate: Predicate) -> Self {
        self.predicates = Some(predicate);
        self
    }

    /// Select some columns of the table.
    pub fn select(mut self, column_names: impl IntoIterator<Item = impl ToString>) -> Self {
        self.column_names = column_names
            .into_iter()
            .map(|item| item.to_string())
            .collect();
        self
    }

    /// Set the snapshot to scan. When not set, it uses current snapshot.
    pub fn snapshot_id(mut self, snapshot_id: i64) -> Self {
        self.snapshot_id = Some(snapshot_id);
        self
    }

    /// Build the table scan.
    pub fn build(self) -> Result<TableScan> {
        let snapshot = match self.snapshot_id {
            Some(snapshot_id) => self
                .table
                .metadata()
                .snapshot_by_id(snapshot_id)
                .ok_or_else(|| {
                    Error::new(
                        ErrorKind::DataInvalid,
                        format!("Snapshot with id {} not found", snapshot_id),
                    )
                })?
                .clone(),
            None => self
                .table
                .metadata()
                .current_snapshot()
                .ok_or_else(|| {
                    Error::new(
                        ErrorKind::FeatureUnsupported,
                        "Can't scan table without snapshots",
                    )
                })?
                .clone(),
        };

        let schema = snapshot.schema(self.table.metadata())?;

        // Check that all column names exist in the schema.
        if !self.column_names.is_empty() {
            for column_name in &self.column_names {
                if schema.field_by_name(column_name).is_none() {
                    return Err(Error::new(
                        ErrorKind::DataInvalid,
                        format!(
                            "Column {} not found in table. Schema: {}",
                            column_name, schema
                        ),
                    ));
                }
            }
        }

        let bound_predicates = if let Some(ref predicates) = self.predicates {
            Some(predicates.bind(schema.clone(), true)?)
        } else {
            None
        };

        Ok(TableScan {
            snapshot,
            file_io: self.table.file_io().clone(),
            table_metadata: self.table.metadata_ref(),
            column_names: self.column_names,
            bound_predicates,
            schema,
            batch_size: self.batch_size,
            case_sensitive: self.case_sensitive,
            filter: self.filter.map(Arc::new),
        })
    }
}

/// Table scan.
#[derive(Debug)]
#[allow(dead_code)]
pub struct TableScan {
    snapshot: SnapshotRef,
    table_metadata: TableMetadataRef,
    file_io: FileIO,
    column_names: Vec<String>,
    bound_predicates: Option<BoundPredicate>,
    schema: SchemaRef,
    batch_size: Option<usize>,
    case_sensitive: bool,
    filter: Option<Arc<Predicate>>,
}

impl TableScan {
    /// Returns a stream of [`FileScanTask`]s.
    pub async fn plan_files(&self) -> Result<FileScanTaskStream> {
        let context = FileScanStreamContext::new(
            self.schema.clone(),
            self.snapshot.clone(),
            self.table_metadata.clone(),
            self.file_io.clone(),
            self.filter.clone(),
            self.case_sensitive,
        )?;

        let mut partition_filter_cache = PartitionFilterCache::new();
        let mut manifest_evaluator_cache = ManifestEvaluatorCache::new();
        let mut expression_evaluator_cache = ExpressionEvaluatorCache::new();

        Ok(try_stream! {
            let manifest_list = context
                .snapshot
                .load_manifest_list(&context.file_io, &context.table_metadata)
                .await?;

            for entry in manifest_list.entries() {
                if !Self::content_type_is_data(entry) {
                    continue;
                }

                let partition_spec_id = entry.partition_spec_id;

                let partition_filter = partition_filter_cache.get(
                    partition_spec_id,
                    &context,
                )?;

                if let Some(partition_filter) = partition_filter {
                    let manifest_evaluator = manifest_evaluator_cache.get(
                        partition_spec_id,
                        partition_filter,
                    );

                    if !manifest_evaluator.eval(entry)? {
                        continue;
                    }
                }

                let manifest = entry.load_manifest(&context.file_io).await?;
                let mut manifest_entries_stream =
                    futures::stream::iter(manifest.entries().iter().filter(|e| e.is_alive()));

                while let Some(manifest_entry) = manifest_entries_stream.next().await {
                    let data_file = manifest_entry.data_file();

                    if let Some(partition_filter) = partition_filter {
                        let expression_evaluator = expression_evaluator_cache.get(partition_spec_id, partition_filter);

                        if !expression_evaluator.eval(data_file)? {
                            continue;
                        }
                    }


                    if let Some(bound_predicate) = context.bound_filter() {
                        // reject any manifest entries whose data file's metrics don't match the filter.
                        if !InclusiveMetricsEvaluator::eval(
                            bound_predicate,
                            manifest_entry.data_file(),
                            false
                        )? {
                            continue;
                        }
                    }

                    match manifest_entry.content_type() {
                        DataContentType::EqualityDeletes | DataContentType::PositionDeletes => {
                            yield Err(Error::new(
                                ErrorKind::FeatureUnsupported,
                                "Delete files are not supported yet.",
                            ))?;
                        }
                        DataContentType::Data => {
                            let scan_task: Result<FileScanTask> = Ok(FileScanTask {
                                data_file_path: manifest_entry.data_file().file_path().to_string(),
                                start: 0,
                                length: manifest_entry.file_size_in_bytes(),
                            });
                            yield scan_task?;
                        }
                    }
                }
            }
        }
        .boxed())
    }

    /// Returns an [`ArrowRecordBatchStream`].
    pub async fn to_arrow(&self) -> Result<ArrowRecordBatchStream> {
        let mut arrow_reader_builder =
            ArrowReaderBuilder::new(self.file_io.clone(), self.schema.clone());

        let mut field_ids = vec![];
        for column_name in &self.column_names {
            let field_id = self.schema.field_id_by_name(column_name).ok_or_else(|| {
                Error::new(
                    ErrorKind::DataInvalid,
                    format!(
                        "Column {} not found in table. Schema: {}",
                        column_name, self.schema
                    ),
                )
            })?;

            let field = self.schema
                .as_struct()
                .field_by_id(field_id)
                .ok_or_else(|| {
                    Error::new(
                        ErrorKind::FeatureUnsupported,
                        format!(
                            "Column {} is not a direct child of schema but a nested field, which is not supported now. Schema: {}",
                            column_name, self.schema
                        ),
                    )
                })?;

            if !field.field_type.is_primitive() {
                return Err(Error::new(
                    ErrorKind::FeatureUnsupported,
                    format!(
                        "Column {} is not a primitive type. Schema: {}",
                        column_name, self.schema
                    ),
                ));
            }

            field_ids.push(field_id as usize);
        }

        arrow_reader_builder = arrow_reader_builder.with_field_ids(field_ids);

        if let Some(batch_size) = self.batch_size {
            arrow_reader_builder = arrow_reader_builder.with_batch_size(batch_size);
        }

        if let Some(ref bound_predicates) = self.bound_predicates {
            arrow_reader_builder = arrow_reader_builder.with_predicates(bound_predicates.clone());
        }

        arrow_reader_builder.build().read(self.plan_files().await?)
    }

    /// Checks whether the [`ManifestContentType`] is `Data` or not.
    fn content_type_is_data(entry: &ManifestFile) -> bool {
        if let ManifestContentType::Data = entry.content {
            return true;
        }
        false
    }
}

/// Holds the context necessary for file scanning operations
/// in a streaming environment.
#[derive(Debug)]
struct FileScanStreamContext {
    schema: SchemaRef,
    snapshot: SnapshotRef,
    table_metadata: TableMetadataRef,
    file_io: FileIO,
    bound_filter: Option<BoundPredicate>,
    case_sensitive: bool,
}

impl FileScanStreamContext {
    /// Creates a new [`FileScanStreamContext`].
    fn new(
        schema: SchemaRef,
        snapshot: SnapshotRef,
        table_metadata: TableMetadataRef,
        file_io: FileIO,
        filter: Option<Arc<Predicate>>,
        case_sensitive: bool,
    ) -> Result<Self> {
        let bound_filter = match filter {
            Some(ref filter) => Some(filter.bind(schema.clone(), case_sensitive)?),
            None => None,
        };

        Ok(Self {
            schema,
            snapshot,
            table_metadata,
            file_io,
            bound_filter,
            case_sensitive,
        })
    }

    /// Returns a reference to the [`BoundPredicate`] filter.
    fn bound_filter(&self) -> Option<&BoundPredicate> {
        self.bound_filter.as_ref()
    }
}

/// Manages the caching of [`BoundPredicate`] objects
/// for [`PartitionSpec`]s based on partition spec id.
#[derive(Debug)]
struct PartitionFilterCache(HashMap<i32, BoundPredicate>);

impl PartitionFilterCache {
    /// Creates a new [`PartitionFilterCache`]
    /// with an empty internal HashMap.
    fn new() -> Self {
        Self(HashMap::new())
    }

    /// Retrieves a [`BoundPredicate`] from the cache
    /// or computes it if not present.
    fn get(
        &mut self,
        spec_id: i32,
        context: &FileScanStreamContext,
    ) -> Result<Option<&BoundPredicate>> {
        match context.bound_filter() {
            None => Ok(None),
            Some(filter) => match self.0.entry(spec_id) {
                Entry::Occupied(e) => Ok(Some(e.into_mut())),
                Entry::Vacant(e) => {
                    let partition_spec = context
                        .table_metadata
                        .partition_spec_by_id(spec_id)
                        .ok_or(Error::new(
                            ErrorKind::Unexpected,
                            format!("Could not find partition spec for id {}", spec_id),
                        ))?;

                    let partition_type = partition_spec.partition_type(context.schema.as_ref())?;
                    let partition_fields = partition_type.fields().to_owned();
                    let partition_schema = Arc::new(
                        Schema::builder()
                            .with_schema_id(partition_spec.spec_id)
                            .with_fields(partition_fields)
                            .build()?,
                    );

                    let mut inclusive_projection = InclusiveProjection::new(partition_spec.clone());

                    let partition_filter = inclusive_projection
                        .project(filter)?
                        .rewrite_not()
                        .bind(partition_schema.clone(), context.case_sensitive)?;

                    Ok(Some(e.insert(partition_filter)))
                }
            },
        }
    }
}

/// Manages the caching of [`ManifestEvaluator`] objects
/// for [`PartitionSpec`]s based on partition spec id.
#[derive(Debug)]
struct ManifestEvaluatorCache(HashMap<i32, ManifestEvaluator>);

impl ManifestEvaluatorCache {
    /// Creates a new [`ManifestEvaluatorCache`]
    /// with an empty internal HashMap.
    fn new() -> Self {
        Self(HashMap::new())
    }

    /// Retrieves a [`ManifestEvaluator`] from the cache
    /// or computes it if not present.
    fn get(&mut self, spec_id: i32, partition_filter: &BoundPredicate) -> &mut ManifestEvaluator {
        self.0
            .entry(spec_id)
            .or_insert(ManifestEvaluator::new(partition_filter.clone()))
    }
}

/// Manages the caching of [`ExpressionEvaluator`] objects
/// for [`PartitionSpec`]s based on partition spec id.
#[derive(Debug)]
struct ExpressionEvaluatorCache(HashMap<i32, ExpressionEvaluator>);

impl ExpressionEvaluatorCache {
    /// Creates a new [`ExpressionEvaluatorCache`]
    /// with an empty internal HashMap.
    fn new() -> Self {
        Self(HashMap::new())
    }

    /// Retrieves a [`ExpressionEvaluator`] from the cache
    /// or computes it if not present.
    fn get(&mut self, spec_id: i32, partition_filter: &BoundPredicate) -> &mut ExpressionEvaluator {
        self.0
            .entry(spec_id)
            .or_insert(ExpressionEvaluator::new(partition_filter.clone()))
    }
}

/// A task to scan part of file.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FileScanTask {
    data_file_path: String,
    #[allow(dead_code)]
    start: u64,
    #[allow(dead_code)]
    length: u64,
}

impl FileScanTask {
    /// Returns the data file path of this file scan task.
    pub fn data_file_path(&self) -> &str {
        &self.data_file_path
    }
}

