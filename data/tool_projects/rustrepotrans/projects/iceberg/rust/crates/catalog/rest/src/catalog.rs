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

//! This module contains rest catalog implementation.

use std::collections::HashMap;
use std::str::FromStr;

use async_trait::async_trait;
use itertools::Itertools;
use reqwest::header::{self, HeaderMap, HeaderName, HeaderValue};
use reqwest::{Client, Request, Response, StatusCode, Url};
use serde::de::DeserializeOwned;
use typed_builder::TypedBuilder;
use urlencoding::encode;

use crate::catalog::_serde::{
    CommitTableRequest, CommitTableResponse, CreateTableRequest, LoadTableResponse,
};
use iceberg::io::FileIO;
use iceberg::table::Table;
use iceberg::Result;
use iceberg::{
    Catalog, Error, ErrorKind, Namespace, NamespaceIdent, TableCommit, TableCreation, TableIdent,
};

use self::_serde::{
    CatalogConfig, ErrorResponse, ListNamespaceResponse, ListTableResponse, NamespaceSerde,
    RenameTableRequest, TokenResponse, NO_CONTENT, OK,
};

const ICEBERG_REST_SPEC_VERSION: &str = "0.14.1";
const CARGO_PKG_VERSION: &str = env!("CARGO_PKG_VERSION");
const PATH_V1: &str = "v1";

/// Rest catalog configuration.
#[derive(Debug, TypedBuilder)]
pub struct RestCatalogConfig {
    uri: String,
    #[builder(default, setter(strip_option))]
    warehouse: Option<String>,

    #[builder(default)]
    props: HashMap<String, String>,
}

impl RestCatalogConfig {
    fn url_prefixed(&self, parts: &[&str]) -> String {
        [&self.uri, PATH_V1]
            .into_iter()
            .chain(self.props.get("prefix").map(|s| &**s))
            .chain(parts.iter().cloned())
            .join("/")
    }

    fn config_endpoint(&self) -> String {
        [&self.uri, PATH_V1, "config"].join("/")
    }

    fn get_token_endpoint(&self) -> String {
        if let Some(auth_url) = self.props.get("rest.authorization-url") {
            auth_url.to_string()
        } else {
            [&self.uri, PATH_V1, "oauth", "tokens"].join("/")
        }
    }

    fn namespaces_endpoint(&self) -> String {
        self.url_prefixed(&["namespaces"])
    }

    fn namespace_endpoint(&self, ns: &NamespaceIdent) -> String {
        self.url_prefixed(&["namespaces", &ns.encode_in_url()])
    }

    fn tables_endpoint(&self, ns: &NamespaceIdent) -> String {
        self.url_prefixed(&["namespaces", &ns.encode_in_url(), "tables"])
    }

    fn rename_table_endpoint(&self) -> String {
        self.url_prefixed(&["tables", "rename"])
    }

    fn table_endpoint(&self, table: &TableIdent) -> String {
        self.url_prefixed(&[
            "namespaces",
            &table.namespace.encode_in_url(),
            "tables",
            encode(&table.name).as_ref(),
        ])
    }

    fn http_headers(&self) -> Result<HeaderMap> {
        let mut headers = HeaderMap::from_iter([
            (
                header::CONTENT_TYPE,
                HeaderValue::from_static("application/json"),
            ),
            (
                HeaderName::from_static("x-client-version"),
                HeaderValue::from_static(ICEBERG_REST_SPEC_VERSION),
            ),
            (
                header::USER_AGENT,
                HeaderValue::from_str(&format!("iceberg-rs/{}", CARGO_PKG_VERSION)).unwrap(),
            ),
        ]);

        if let Some(token) = self.props.get("token") {
            headers.insert(
                header::AUTHORIZATION,
                HeaderValue::from_str(&format!("Bearer {token}")).map_err(|e| {
                    Error::new(
                        ErrorKind::DataInvalid,
                        "Invalid token received from catalog server!",
                    )
                    .with_source(e)
                })?,
            );
        }

        for (key, value) in self.props.iter() {
            if let Some(stripped_key) = key.strip_prefix("header.") {
                // Avoid overwriting default headers
                if !headers.contains_key(stripped_key) {
                    headers.insert(
                        HeaderName::from_str(stripped_key).map_err(|e| {
                            Error::new(
                                ErrorKind::DataInvalid,
                                format!("Invalid header name: {stripped_key}!"),
                            )
                            .with_source(e)
                        })?,
                        HeaderValue::from_str(value).map_err(|e| {
                            Error::new(
                                ErrorKind::DataInvalid,
                                format!("Invalid header value: {value}!"),
                            )
                            .with_source(e)
                        })?,
                    );
                }
            }
        }
        Ok(headers)
    }

    fn try_create_rest_client(&self) -> Result<HttpClient> {
        // TODO: We will add ssl config, sigv4 later
        let headers = self.http_headers()?;

        Ok(HttpClient(
            Client::builder().default_headers(headers).build()?,
        ))
    }

    fn optional_oauth_params(&self) -> HashMap<&str, &str> {
        let mut optional_oauth_param = HashMap::new();
        if let Some(scope) = self.props.get("scope") {
            optional_oauth_param.insert("scope", scope.as_str());
        } else {
            optional_oauth_param.insert("scope", "catalog");
        }
        let set_of_optional_params = ["audience", "resource"];
        for param_name in set_of_optional_params.iter() {
            if let Some(value) = self.props.get(*param_name) {
                optional_oauth_param.insert(param_name.to_owned(), value);
            }
        }
        optional_oauth_param
    }
}

#[derive(Debug)]
struct HttpClient(Client);

impl HttpClient {
    async fn query<
        R: DeserializeOwned,
        E: DeserializeOwned + Into<Error>,
        const SUCCESS_CODE: u16,
    >(
        &self,
        request: Request,
    ) -> Result<R> {
        let resp = self.0.execute(request).await?;

        if resp.status().as_u16() == SUCCESS_CODE {
            let text = resp.bytes().await?;
            Ok(serde_json::from_slice::<R>(&text).map_err(|e| {
                Error::new(
                    ErrorKind::Unexpected,
                    "Failed to parse response from rest catalog server!",
                )
                .with_context("json", String::from_utf8_lossy(&text))
                .with_source(e)
            })?)
        } else {
            let code = resp.status();
            let text = resp.bytes().await?;
            let e = serde_json::from_slice::<E>(&text).map_err(|e| {
                Error::new(
                    ErrorKind::Unexpected,
                    "Failed to parse response from rest catalog server!",
                )
                .with_context("json", String::from_utf8_lossy(&text))
                .with_context("code", code.to_string())
                .with_source(e)
            })?;
            Err(e.into())
        }
    }

    async fn execute<E: DeserializeOwned + Into<Error>, const SUCCESS_CODE: u16>(
        &self,
        request: Request,
    ) -> Result<()> {
        let resp = self.0.execute(request).await?;

        if resp.status().as_u16() == SUCCESS_CODE {
            Ok(())
        } else {
            let code = resp.status();
            let text = resp.bytes().await?;
            let e = serde_json::from_slice::<E>(&text).map_err(|e| {
                Error::new(
                    ErrorKind::Unexpected,
                    "Failed to parse response from rest catalog server!",
                )
                .with_context("json", String::from_utf8_lossy(&text))
                .with_context("code", code.to_string())
                .with_source(e)
            })?;
            Err(e.into())
        }
    }

    /// More generic logic handling for special cases like head.
    async fn do_execute<R, E: DeserializeOwned + Into<Error>>(
        &self,
        request: Request,
        handler: impl FnOnce(&Response) -> Option<R>,
    ) -> Result<R> {
        let resp = self.0.execute(request).await?;

        if let Some(ret) = handler(&resp) {
            Ok(ret)
        } else {
            let code = resp.status();
            let text = resp.bytes().await?;
            let e = serde_json::from_slice::<E>(&text).map_err(|e| {
                Error::new(
                    ErrorKind::Unexpected,
                    "Failed to parse response from rest catalog server!",
                )
                .with_context("code", code.to_string())
                .with_context("json", String::from_utf8_lossy(&text))
                .with_source(e)
            })?;
            Err(e.into())
        }
    }
}

/// Rest catalog implementation.
#[derive(Debug)]
pub struct RestCatalog {
    config: RestCatalogConfig,
    client: HttpClient,
}

#[async_trait]
impl Catalog for RestCatalog {
    /// List namespaces from table.
    async fn list_namespaces(
        &self,
        parent: Option<&NamespaceIdent>,
    ) -> Result<Vec<NamespaceIdent>> {
        let mut request = self.client.0.get(self.config.namespaces_endpoint());
        if let Some(ns) = parent {
            request = request.query(&[("parent", ns.encode_in_url())]);
        }

        let resp = self
            .client
            .query::<ListNamespaceResponse, ErrorResponse, OK>(request.build()?)
            .await?;

        resp.namespaces
            .into_iter()
            .map(NamespaceIdent::from_vec)
            .collect::<Result<Vec<NamespaceIdent>>>()
    }

    /// Create a new namespace inside the catalog.
    async fn create_namespace(
        &self,
        namespace: &NamespaceIdent,
        properties: HashMap<String, String>,
    ) -> Result<Namespace> {
        let request = self
            .client
            .0
            .post(self.config.namespaces_endpoint())
            .json(&NamespaceSerde {
                namespace: namespace.as_ref().clone(),
                properties: Some(properties),
            })
            .build()?;

        let resp = self
            .client
            .query::<NamespaceSerde, ErrorResponse, OK>(request)
            .await?;

        Namespace::try_from(resp)
    }

    /// Get a namespace information from the catalog.
    async fn get_namespace(&self, namespace: &NamespaceIdent) -> Result<Namespace> {
        let request = self
            .client
            .0
            .get(self.config.namespace_endpoint(namespace))
            .build()?;

        let resp = self
            .client
            .query::<NamespaceSerde, ErrorResponse, OK>(request)
            .await?;
        Namespace::try_from(resp)
    }

    /// Update a namespace inside the catalog.
    ///
    /// # Behavior
    ///
    /// The properties must be the full set of namespace.
    async fn update_namespace(
        &self,
        _namespace: &NamespaceIdent,
        _properties: HashMap<String, String>,
    ) -> Result<()> {
        Err(Error::new(
            ErrorKind::FeatureUnsupported,
            "Updating namespace not supported yet!",
        ))
    }

    async fn namespace_exists(&self, ns: &NamespaceIdent) -> Result<bool> {
        let request = self
            .client
            .0
            .head(self.config.namespace_endpoint(ns))
            .build()?;

        self.client
            .do_execute::<bool, ErrorResponse>(request, |resp| match resp.status() {
                StatusCode::NO_CONTENT => Some(true),
                StatusCode::NOT_FOUND => Some(false),
                _ => None,
            })
            .await
    }

    /// Drop a namespace from the catalog.
    async fn drop_namespace(&self, namespace: &NamespaceIdent) -> Result<()> {
        let request = self
            .client
            .0
            .delete(self.config.namespace_endpoint(namespace))
            .build()?;

        self.client
            .execute::<ErrorResponse, NO_CONTENT>(request)
            .await
    }

    /// List tables from namespace.
    async fn list_tables(&self, namespace: &NamespaceIdent) -> Result<Vec<TableIdent>> {
        let request = self
            .client
            .0
            .get(self.config.tables_endpoint(namespace))
            .build()?;

        let resp = self
            .client
            .query::<ListTableResponse, ErrorResponse, OK>(request)
            .await?;

        Ok(resp.identifiers)
    }

    /// Create a new table inside the namespace.
    async fn create_table(
        &self,
        namespace: &NamespaceIdent,
        creation: TableCreation,
    ) -> Result<Table> {
        let table_ident = TableIdent::new(namespace.clone(), creation.name.clone());

        let request = self
            .client
            .0
            .post(self.config.tables_endpoint(namespace))
            .json(&CreateTableRequest {
                name: creation.name,
                location: creation.location,
                schema: creation.schema,
                partition_spec: creation.partition_spec,
                write_order: creation.sort_order,
                // We don't support stage create yet.
                stage_create: Some(false),
                properties: if creation.properties.is_empty() {
                    None
                } else {
                    Some(creation.properties)
                },
            })
            .build()?;

        let resp = self
            .client
            .query::<LoadTableResponse, ErrorResponse, OK>(request)
            .await?;

        let file_io = self.load_file_io(resp.metadata_location.as_deref(), resp.config)?;

        let table = Table::builder()
            .identifier(table_ident)
            .file_io(file_io)
            .metadata(resp.metadata)
            .metadata_location(resp.metadata_location.ok_or_else(|| {
                Error::new(
                    ErrorKind::DataInvalid,
                    "Metadata location missing in create table response!",
                )
            })?)
            .build();

        Ok(table)
    }

    /// Load table from the catalog.
    async fn load_table(&self, table: &TableIdent) -> Result<Table> {
        let request = self
            .client
            .0
            .get(self.config.table_endpoint(table))
            .build()?;

        let resp = self
            .client
            .query::<LoadTableResponse, ErrorResponse, OK>(request)
            .await?;

        let file_io = self.load_file_io(resp.metadata_location.as_deref(), resp.config)?;

        let table_builder = Table::builder()
            .identifier(table.clone())
            .file_io(file_io)
            .metadata(resp.metadata);

        if let Some(metadata_location) = resp.metadata_location {
            Ok(table_builder.metadata_location(metadata_location).build())
        } else {
            Ok(table_builder.build())
        }
    }

    /// Drop a table from the catalog.
    async fn drop_table(&self, table: &TableIdent) -> Result<()> {
        let request = self
            .client
            .0
            .delete(self.config.table_endpoint(table))
            .build()?;

        self.client
            .execute::<ErrorResponse, NO_CONTENT>(request)
            .await
    }

    /// Check if a table exists in the catalog.
    async fn table_exists(&self, table: &TableIdent) -> Result<bool> {
        let request = self
            .client
            .0
            .head(self.config.table_endpoint(table))
            .build()?;

        self.client
            .do_execute::<bool, ErrorResponse>(request, |resp| match resp.status() {
                StatusCode::NO_CONTENT => Some(true),
                StatusCode::NOT_FOUND => Some(false),
                _ => None,
            })
            .await
    }

    /// Rename a table in the catalog.
    async fn rename_table(&self, src: &TableIdent, dest: &TableIdent) -> Result<()> {
        let request = self
            .client
            .0
            .post(self.config.rename_table_endpoint())
            .json(&RenameTableRequest {
                source: src.clone(),
                destination: dest.clone(),
            })
            .build()?;

        self.client
            .execute::<ErrorResponse, NO_CONTENT>(request)
            .await
    }

    /// Update table.
    async fn update_table(&self, mut commit: TableCommit) -> Result<Table> {
        let request = self
            .client
            .0
            .post(self.config.table_endpoint(commit.identifier()))
            .json(&CommitTableRequest {
                identifier: commit.identifier().clone(),
                requirements: commit.take_requirements(),
                updates: commit.take_updates(),
            })
            .build()?;

        let resp = self
            .client
            .query::<CommitTableResponse, ErrorResponse, OK>(request)
            .await?;

        let file_io = self.load_file_io(Some(&resp.metadata_location), None)?;
        Ok(Table::builder()
            .identifier(commit.identifier().clone())
            .file_io(file_io)
            .metadata(resp.metadata)
            .metadata_location(resp.metadata_location)
            .build())
    }
}

impl RestCatalog {
    /// Creates a rest catalog from config.
    pub async fn new(config: RestCatalogConfig) -> Result<Self> {
        let mut catalog = Self {
            client: config.try_create_rest_client()?,
            config,
        };
        catalog.fetch_access_token().await?;
        catalog.client = catalog.config.try_create_rest_client()?;
        catalog.update_config().await?;
        catalog.client = catalog.config.try_create_rest_client()?;

        Ok(catalog)
    }

    async fn fetch_access_token(&mut self) -> Result<()> {
        if self.config.props.contains_key("token") {
            return Ok(());
        }
        if let Some(credential) = self.config.props.get("credential") {
            let (client_id, client_secret) = if credential.contains(':') {
                let (client_id, client_secret) = credential.split_once(':').unwrap();
                (Some(client_id), client_secret)
            } else {
                (None, credential.as_str())
            };
            let mut params = HashMap::with_capacity(4);
            params.insert("grant_type", "client_credentials");
            if let Some(client_id) = client_id {
                params.insert("client_id", client_id);
            }
            params.insert("client_secret", client_secret);
            let optional_oauth_params = self.config.optional_oauth_params();
            params.extend(optional_oauth_params);
            let req = self
                .client
                .0
                .post(self.config.get_token_endpoint())
                .form(&params)
                .build()?;
            let res = self
                .client
                .query::<TokenResponse, ErrorResponse, OK>(req)
                .await
                .map_err(|e| {
                    Error::new(
                        ErrorKind::Unexpected,
                        "Failed to fetch access token from catalog server!",
                    )
                    .with_source(e)
                })?;
            let token = res.access_token;
            self.config.props.insert("token".to_string(), token);
        }

        Ok(())
    }

    async fn update_config(&mut self) -> Result<()> {
        let mut request = self.client.0.get(self.config.config_endpoint());

        if let Some(warehouse_location) = &self.config.warehouse {
            request = request.query(&[("warehouse", warehouse_location)]);
        }

        let mut config = self
            .client
            .query::<CatalogConfig, ErrorResponse, OK>(request.build()?)
            .await?;

        let mut props = config.defaults;
        props.extend(self.config.props.clone());
        if let Some(uri) = config.overrides.remove("uri") {
            self.config.uri = uri;
        }
        props.extend(config.overrides);

        self.config.props = props;

        Ok(())
    }

    fn load_file_io(
        &self,
        metadata_location: Option<&str>,
        extra_config: Option<HashMap<String, String>>,
    ) -> Result<FileIO> {
        let mut props = self.config.props.clone();
        if let Some(config) = extra_config {
            props.extend(config);
        }

        // If the warehouse is a logical identifier instead of a URL we don't want
        // to raise an exception
        let warehouse_path = match self.config.warehouse.as_deref() {
            Some(url) if Url::parse(url).is_ok() => Some(url),
            Some(_) => None,
            None => None,
        };

        let file_io = match warehouse_path.or(metadata_location) {
            Some(url) => FileIO::from_path(url)?.with_props(props).build()?,
            None => {
                return Err(Error::new(
                    ErrorKind::Unexpected,
                    "Unable to load file io, neither warehouse nor metadata location is set!",
                ))?
            }
        };

        Ok(file_io)
    }
}

/// Requests and responses for rest api.
mod _serde {
    use std::collections::HashMap;

    use serde_derive::{Deserialize, Serialize};

    use iceberg::spec::{Schema, SortOrder, TableMetadata, UnboundPartitionSpec};
    use iceberg::{Error, ErrorKind, Namespace, TableIdent, TableRequirement, TableUpdate};

    pub(super) const OK: u16 = 200u16;
    pub(super) const NO_CONTENT: u16 = 204u16;

    #[derive(Clone, Debug, Serialize, Deserialize)]
    pub(super) struct CatalogConfig {
        pub(super) overrides: HashMap<String, String>,
        pub(super) defaults: HashMap<String, String>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct ErrorResponse {
        error: ErrorModel,
    }

    impl From<ErrorResponse> for Error {
        fn from(resp: ErrorResponse) -> Error {
            resp.error.into()
        }
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct ErrorModel {
        pub(super) message: String,
        pub(super) r#type: String,
        pub(super) code: u16,
        pub(super) stack: Option<Vec<String>>,
    }

    impl From<ErrorModel> for Error {
        fn from(value: ErrorModel) -> Self {
            let mut error = Error::new(ErrorKind::DataInvalid, value.message)
                .with_context("type", value.r#type)
                .with_context("code", format!("{}", value.code));

            if let Some(stack) = value.stack {
                error = error.with_context("stack", stack.join("\n"));
            }

            error
        }
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct OAuthError {
        pub(super) error: String,
        pub(super) error_description: Option<String>,
        pub(super) error_uri: Option<String>,
    }

    impl From<OAuthError> for Error {
        fn from(value: OAuthError) -> Self {
            let mut error = Error::new(
                ErrorKind::DataInvalid,
                format!("OAuthError: {}", value.error),
            );

            if let Some(desc) = value.error_description {
                error = error.with_context("description", desc);
            }

            if let Some(uri) = value.error_uri {
                error = error.with_context("uri", uri);
            }

            error
        }
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct TokenResponse {
        pub(super) access_token: String,
        pub(super) token_type: String,
        pub(super) expires_in: Option<u64>,
        pub(super) issued_token_type: Option<String>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct NamespaceSerde {
        pub(super) namespace: Vec<String>,
        pub(super) properties: Option<HashMap<String, String>>,
    }

    impl TryFrom<NamespaceSerde> for super::Namespace {
        type Error = Error;
        fn try_from(value: NamespaceSerde) -> std::result::Result<Self, Self::Error> {
            Ok(super::Namespace::with_properties(
                super::NamespaceIdent::from_vec(value.namespace)?,
                value.properties.unwrap_or_default(),
            ))
        }
    }

    impl From<&Namespace> for NamespaceSerde {
        fn from(value: &Namespace) -> Self {
            Self {
                namespace: value.name().as_ref().clone(),
                properties: Some(value.properties().clone()),
            }
        }
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct ListNamespaceResponse {
        pub(super) namespaces: Vec<Vec<String>>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct UpdateNamespacePropsRequest {
        removals: Option<Vec<String>>,
        updates: Option<HashMap<String, String>>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct UpdateNamespacePropsResponse {
        updated: Vec<String>,
        removed: Vec<String>,
        missing: Option<Vec<String>>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct ListTableResponse {
        pub(super) identifiers: Vec<TableIdent>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct RenameTableRequest {
        pub(super) source: TableIdent,
        pub(super) destination: TableIdent,
    }

    #[derive(Debug, Deserialize)]
    #[serde(rename_all = "kebab-case")]
    pub(super) struct LoadTableResponse {
        pub(super) metadata_location: Option<String>,
        pub(super) metadata: TableMetadata,
        pub(super) config: Option<HashMap<String, String>>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    #[serde(rename_all = "kebab-case")]
    pub(super) struct CreateTableRequest {
        pub(super) name: String,
        pub(super) location: Option<String>,
        pub(super) schema: Schema,
        pub(super) partition_spec: Option<UnboundPartitionSpec>,
        pub(super) write_order: Option<SortOrder>,
        pub(super) stage_create: Option<bool>,
        pub(super) properties: Option<HashMap<String, String>>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    pub(super) struct CommitTableRequest {
        pub(super) identifier: TableIdent,
        pub(super) requirements: Vec<TableRequirement>,
        pub(super) updates: Vec<TableUpdate>,
    }

    #[derive(Debug, Serialize, Deserialize)]
    #[serde(rename_all = "kebab-case")]
    pub(super) struct CommitTableResponse {
        pub(super) metadata_location: String,
        pub(super) metadata: TableMetadata,
    }
}

