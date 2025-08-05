//! # Account manager module.

use std::collections::BTreeMap;
use std::future::Future;
use std::path::{Path, PathBuf};

use anyhow::{ensure, Context as _, Result};
use futures::future::join_all;
use serde::{Deserialize, Serialize};
use tokio::fs;
use tokio::io::AsyncWriteExt;
use tokio::task::JoinHandle;
use uuid::Uuid;

#[cfg(not(target_os = "ios"))]
use tokio::sync::oneshot;
#[cfg(not(target_os = "ios"))]
use tokio::time::{sleep, Duration};

use crate::context::{Context, ContextBuilder};
use crate::events::{Event, EventEmitter, EventType, Events};
use crate::push::PushSubscriber;
use crate::stock_str::StockStrings;

/// Account manager, that can handle multiple accounts in a single place.
#[derive(Debug)]
pub struct Accounts {
    dir: PathBuf,
    config: Config,
    /// Map from account ID to the account.
    accounts: BTreeMap<u32, Context>,

    /// Event channel to emit account manager errors.
    events: Events,

    /// Stock string translations shared by all created contexts.
    ///
    /// This way changing a translation for one context automatically
    /// changes it for all other contexts.
    pub(crate) stockstrings: StockStrings,

    /// Push notification subscriber shared between accounts.
    push_subscriber: PushSubscriber,
}

impl Accounts {
    /// Loads or creates an accounts folder at the given `dir`.
    pub async fn new(dir: PathBuf, writable: bool) -> Result<Self> {
        if writable && !dir.exists() {
            Accounts::create(&dir).await?;
        }

        Accounts::open(dir, writable).await
    }

    /// Creates a new default structure.
    async fn create(dir: &Path) -> Result<()> {
        fs::create_dir_all(dir)
            .await
            .context("failed to create folder")?;

        Config::new(dir).await?;

        Ok(())
    }

    /// Opens an existing accounts structure. Will error if the folder doesn't exist,
    /// no account exists and no config exists.
    async fn open(dir: PathBuf, writable: bool) -> Result<Self> {
        ensure!(dir.exists(), "directory does not exist");

        let config_file = dir.join(CONFIG_NAME);
        ensure!(config_file.exists(), "{:?} does not exist", config_file);

        let config = Config::from_file(config_file, writable)
            .await
            .context("failed to load accounts config")?;
        let events = Events::new();
        let stockstrings = StockStrings::new();
        let push_subscriber = PushSubscriber::new();
        let accounts = config
            .load_accounts(&events, &stockstrings, push_subscriber.clone(), &dir)
            .await
            .context("failed to load accounts")?;

        Ok(Self {
            dir,
            config,
            accounts,
            events,
            stockstrings,
            push_subscriber,
        })
    }

    /// Returns an account by its `id`:
    pub fn get_account(&self, id: u32) -> Option<Context> {
        self.accounts.get(&id).cloned()
    }

    /// Returns the currently selected account.
    pub fn get_selected_account(&self) -> Option<Context> {
        let id = self.config.get_selected_account();
        self.accounts.get(&id).cloned()
    }

    /// Returns the currently selected account's id or None if no account is selected.
    pub fn get_selected_account_id(&self) -> Option<u32> {
        match self.config.get_selected_account() {
            0 => None,
            id => Some(id),
        }
    }

    /// Selects the given account.
    pub async fn select_account(&mut self, id: u32) -> Result<()> {
        self.config.select_account(id).await?;

        Ok(())
    }

    /// Adds a new account and opens it.
    ///
    /// Returns account ID.
    pub async fn add_account(&mut self) -> Result<u32> {
        let account_config = self.config.new_account().await?;
        let dbfile = account_config.dbfile(&self.dir);

        let ctx = ContextBuilder::new(dbfile)
            .with_id(account_config.id)
            .with_events(self.events.clone())
            .with_stock_strings(self.stockstrings.clone())
            .with_push_subscriber(self.push_subscriber.clone())
            .build()
            .await?;
        // Try to open without a passphrase,
        // but do not return an error if account is passphare-protected.
        ctx.open("".to_string()).await?;

        self.accounts.insert(account_config.id, ctx);

        Ok(account_config.id)
    }

    /// Adds a new closed account.
    pub async fn add_closed_account(&mut self) -> Result<u32> {
        let account_config = self.config.new_account().await?;
        let dbfile = account_config.dbfile(&self.dir);

        let ctx = ContextBuilder::new(dbfile)
            .with_id(account_config.id)
            .with_events(self.events.clone())
            .with_stock_strings(self.stockstrings.clone())
            .with_push_subscriber(self.push_subscriber.clone())
            .build()
            .await?;
        self.accounts.insert(account_config.id, ctx);

        Ok(account_config.id)
    }

    /// Removes an account.
    pub async fn remove_account(&mut self, id: u32) -> Result<()> {
        let ctx = self
            .accounts
            .remove(&id)
            .with_context(|| format!("no account with id {id}"))?;
        ctx.stop_io().await;
        drop(ctx);

        if let Some(cfg) = self.config.get_account(id) {
            let account_path = self.dir.join(cfg.dir);

            try_many_times(|| fs::remove_dir_all(&account_path))
                .await
                .context("failed to remove account data")?;
        }
        self.config.remove_account(id).await?;

        Ok(())
    }

    /// Migrates an existing account into this structure.
    ///
    /// Returns the ID of new account.
    pub async fn migrate_account(&mut self, dbfile: PathBuf) -> Result<u32> {
        let blobdir = Context::derive_blobdir(&dbfile);
        let walfile = Context::derive_walfile(&dbfile);

        ensure!(dbfile.exists(), "no database found: {}", dbfile.display());
        ensure!(blobdir.exists(), "no blobdir found: {}", blobdir.display());

        let old_id = self.config.get_selected_account();

        // create new account
        let account_config = self
            .config
            .new_account()
            .await
            .context("failed to create new account")?;

        let new_dbfile = account_config.dbfile(&self.dir);
        let new_blobdir = Context::derive_blobdir(&new_dbfile);
        let new_walfile = Context::derive_walfile(&new_dbfile);

        let res = {
            fs::create_dir_all(self.dir.join(&account_config.dir))
                .await
                .context("failed to create dir")?;
            try_many_times(|| fs::rename(&dbfile, &new_dbfile))
                .await
                .context("failed to rename dbfile")?;
            try_many_times(|| fs::rename(&blobdir, &new_blobdir))
                .await
                .context("failed to rename blobdir")?;
            if walfile.exists() {
                fs::rename(&walfile, &new_walfile)
                    .await
                    .context("failed to rename walfile")?;
            }
            Ok(())
        };

        match res {
            Ok(_) => {
                let ctx = Context::new(
                    &new_dbfile,
                    account_config.id,
                    self.events.clone(),
                    self.stockstrings.clone(),
                )
                .await?;
                self.accounts.insert(account_config.id, ctx);
                Ok(account_config.id)
            }
            Err(err) => {
                let account_path = std::path::PathBuf::from(&account_config.dir);
                try_many_times(|| fs::remove_dir_all(&account_path))
                    .await
                    .context("failed to remove account data")?;
                self.config.remove_account(account_config.id).await?;

                // set selection back
                self.select_account(old_id).await?;

                Err(err)
            }
        }
    }

    /// Get a list of all account ids.
    pub fn get_all(&self) -> Vec<u32> {
        self.accounts.keys().copied().collect()
    }

    /// Starts background tasks such as IMAP and SMTP loops for all accounts.
    pub async fn start_io(&mut self) {
        for account in self.accounts.values_mut() {
            account.start_io().await;
        }
    }

    /// Stops background tasks for all accounts.
    pub async fn stop_io(&self) {
        // Sending an event here wakes up event loop even
        // if there are no accounts.
        info!(self, "Stopping IO for all accounts.");
        for account in self.accounts.values() {
            account.stop_io().await;
        }
    }

    /// Notifies all accounts that the network may have become available.
    pub async fn maybe_network(&self) {
        for account in self.accounts.values() {
            account.scheduler.maybe_network().await;
        }
    }

    /// Notifies all accounts that the network connection may have been lost.
    pub async fn maybe_network_lost(&self) {
        for account in self.accounts.values() {
            account.scheduler.maybe_network_lost(account).await;
        }
    }

    /// Performs a background fetch for all accounts in parallel.
    ///
    /// This is an auxiliary function and not part of public API.
    /// Use [Accounts::background_fetch] instead.
    async fn background_fetch_without_timeout(&self) {
        async fn background_fetch_and_log_error(account: Context) {
            if let Err(error) = account.background_fetch().await {
                warn!(account, "{error:#}");
            }
        }

        join_all(
            self.accounts
                .values()
                .cloned()
                .map(background_fetch_and_log_error),
        )
        .await;
    }

    /// Performs a background fetch for all accounts in parallel with a timeout.
    ///
    /// The `AccountsBackgroundFetchDone` event is emitted at the end,
    /// process all events until you get this one and you can safely return to the background
    /// without forgetting to create notifications caused by timing race conditions.
    pub async fn background_fetch(&self, timeout: std::time::Duration) {
        if let Err(_err) =
            tokio::time::timeout(timeout, self.background_fetch_without_timeout()).await
        {
            self.emit_event(EventType::Warning(
                "Background fetch timed out.".to_string(),
            ));
        }
        self.emit_event(EventType::AccountsBackgroundFetchDone);
    }

    /// Emits a single event.
    pub fn emit_event(&self, event: EventType) {
        self.events.emit(Event { id: 0, typ: event })
    }

    /// Returns event emitter.
    pub fn get_event_emitter(&self) -> EventEmitter {
        self.events.get_emitter()
    }

    /// Sets notification token for Apple Push Notification service.
    pub async fn set_push_device_token(&mut self, token: &str) -> Result<()> {
        self.push_subscriber.set_device_token(token).await;
        Ok(())
    }
}

/// Configuration file name.
const CONFIG_NAME: &str = "accounts.toml";

/// Lockfile name.
#[cfg(not(target_os = "ios"))]
const LOCKFILE_NAME: &str = "accounts.lock";

/// Database file name.
const DB_NAME: &str = "dc.db";

/// Account manager configuration file.
#[derive(Debug)]
struct Config {
    file: PathBuf,
    inner: InnerConfig,
    // We lock the lockfile in the Config constructors to protect also from having multiple Config
    // objects for the same config file.
    lock_task: Option<JoinHandle<anyhow::Result<()>>>,
}

/// Account manager configuration file contents.
///
/// This is serialized into TOML.
#[derive(Serialize, Deserialize, Debug, Clone, PartialEq)]
struct InnerConfig {
    /// The currently selected account.
    pub selected_account: u32,
    pub next_id: u32,
    pub accounts: Vec<AccountConfig>,
}

impl Drop for Config {
    fn drop(&mut self) {
        if let Some(lock_task) = self.lock_task.take() {
            lock_task.abort();
        }
    }
}

impl Config {
    #[cfg(target_os = "ios")]
    async fn create_lock_task(_dir: PathBuf) -> Result<Option<JoinHandle<anyhow::Result<()>>>> {
        // Do not lock accounts.toml on iOS.
        // This results in 0xdead10cc crashes on suspend.
        // iOS itself ensures that multiple instances of Delta Chat are not running.
        Ok(None)
    }

    #[cfg(not(target_os = "ios"))]
    async fn create_lock_task(dir: PathBuf) -> Result<Option<JoinHandle<anyhow::Result<()>>>> {
        let lockfile = dir.join(LOCKFILE_NAME);
        let mut lock = fd_lock::RwLock::new(fs::File::create(lockfile).await?);
        let (locked_tx, locked_rx) = oneshot::channel();
        let lock_task: JoinHandle<anyhow::Result<()>> = tokio::spawn(async move {
            let mut timeout = Duration::from_millis(100);
            let _guard = loop {
                match lock.try_write() {
                    Ok(guard) => break Ok(guard),
                    Err(err) => {
                        if timeout.as_millis() > 1600 {
                            break Err(err);
                        }
                        // We need to wait for the previous lock_task to be aborted thus unlocking
                        // the lockfile. We don't open configs for writing often outside of the
                        // tests, so this adds delays to the tests, but otherwise ok.
                        sleep(timeout).await;
                        if err.kind() == std::io::ErrorKind::WouldBlock {
                            timeout *= 2;
                        }
                    }
                }
            }?;
            locked_tx
                .send(())
                .ok()
                .context("Cannot notify about lockfile locking")?;
            let (_tx, rx) = oneshot::channel();
            rx.await?;
            Ok(())
        });
        locked_rx.await?;
        Ok(Some(lock_task))
    }

    /// Creates a new Config for `file`, but doesn't open/sync it.
    async fn new_nosync(file: PathBuf, lock: bool) -> Result<Self> {
        let dir = file.parent().context("Cannot get config file directory")?;
        let inner = InnerConfig {
            accounts: Vec::new(),
            selected_account: 0,
            next_id: 1,
        };
        if !lock {
            let cfg = Self {
                file,
                inner,
                lock_task: None,
            };
            return Ok(cfg);
        }
        let lock_task = Self::create_lock_task(dir.to_path_buf()).await?;
        let cfg = Self {
            file,
            inner,
            lock_task,
        };
        Ok(cfg)
    }

    /// Creates a new configuration file in the given account manager directory.
    pub async fn new(dir: &Path) -> Result<Self> {
        let lock = true;
        let mut cfg = Self::new_nosync(dir.join(CONFIG_NAME), lock).await?;
        cfg.sync().await?;

        Ok(cfg)
    }

    /// Sync the inmemory representation to disk.
    /// Takes a mutable reference because the saved file is a part of the `Config` state. This
    /// protects from parallel calls resulting to a wrong file contents.
    async fn sync(&mut self) -> Result<()> {
        #[cfg(not(target_os = "ios"))]
        ensure!(!self
            .lock_task
            .as_ref()
            .context("Config is read-only")?
            .is_finished());

        let tmp_path = self.file.with_extension("toml.tmp");
        let mut file = fs::File::create(&tmp_path)
            .await
            .context("failed to create a tmp config")?;
        file.write_all(toml::to_string_pretty(&self.inner)?.as_bytes())
            .await
            .context("failed to write a tmp config")?;
        file.sync_data()
            .await
            .context("failed to sync a tmp config")?;
        drop(file);
        fs::rename(&tmp_path, &self.file)
            .await
            .context("failed to rename config")?;
        Ok(())
    }

    /// Read a configuration from the given file into memory.
    pub async fn from_file(file: PathBuf, writable: bool) -> Result<Self> {
        let mut config = Self::new_nosync(file, writable).await?;
        let bytes = fs::read(&config.file)
            .await
            .context("Failed to read file")?;
        let s = std::str::from_utf8(&bytes)?;
        config.inner = toml::from_str(s).context("Failed to parse config")?;

        // Previous versions of the core stored absolute paths in account config.
        // Convert them to relative paths.
        let mut modified = false;
        for account in &mut config.inner.accounts {
            if account.dir.is_absolute() {
                if let Some(old_path_parent) = account.dir.parent() {
                    if let Ok(new_path) = account.dir.strip_prefix(old_path_parent) {
                        account.dir = new_path.to_path_buf();
                        modified = true;
                    }
                }
            }
        }
        if modified && writable {
            config.sync().await?;
        }

        Ok(config)
    }

    /// Loads all accounts defined in the configuration file.
    ///
    /// Created contexts share the same event channel and stock string
    /// translations.
    pub async fn load_accounts(
        &self,
        events: &Events,
        stockstrings: &StockStrings,
        push_subscriber: PushSubscriber,
        dir: &Path,
    ) -> Result<BTreeMap<u32, Context>> {
        let mut accounts = BTreeMap::new();

        for account_config in &self.inner.accounts {
            let dbfile = account_config.dbfile(dir);
            let ctx = ContextBuilder::new(dbfile.clone())
                .with_id(account_config.id)
                .with_events(events.clone())
                .with_stock_strings(stockstrings.clone())
                .with_push_subscriber(push_subscriber.clone())
                .build()
                .await
                .with_context(|| format!("failed to create context from file {:?}", &dbfile))?;
            // Try to open without a passphrase,
            // but do not return an error if account is passphare-protected.
            ctx.open("".to_string()).await?;

            accounts.insert(account_config.id, ctx);
        }

        Ok(accounts)
    }

    /// Creates a new account in the account manager directory.
    async fn new_account(&mut self) -> Result<AccountConfig> {
        let id = {
            let id = self.inner.next_id;
            let uuid = Uuid::new_v4();
            let target_dir = PathBuf::from(uuid.to_string());

            self.inner.accounts.push(AccountConfig {
                id,
                dir: target_dir,
                uuid,
            });
            self.inner.next_id += 1;
            id
        };

        self.sync().await?;

        self.select_account(id)
            .await
            .context("failed to select just added account")?;
        let cfg = self
            .get_account(id)
            .context("failed to get just added account")?;
        Ok(cfg)
    }

    /// Removes an existing account entirely.
    pub async fn remove_account(&mut self, id: u32) -> Result<()> {
        {
            if let Some(idx) = self.inner.accounts.iter().position(|e| e.id == id) {
                // remove account from the configs
                self.inner.accounts.remove(idx);
            }
            if self.inner.selected_account == id {
                // reset selected account
                self.inner.selected_account = self
                    .inner
                    .accounts
                    .first()
                    .map(|e| e.id)
                    .unwrap_or_default();
            }
        }

        self.sync().await
    }

    /// Returns configuration file section for the given account ID.
    fn get_account(&self, id: u32) -> Option<AccountConfig> {
        self.inner.accounts.iter().find(|e| e.id == id).cloned()
    }

    /// Returns the ID of selected account.
    pub fn get_selected_account(&self) -> u32 {
        self.inner.selected_account
    }

    /// Changes selected account ID.
    pub async fn select_account(&mut self, id: u32) -> Result<()> {
        {
            ensure!(
                self.inner.accounts.iter().any(|e| e.id == id),
                "invalid account id: {}",
                id
            );

            self.inner.selected_account = id;
        }

        self.sync().await?;
        Ok(())
    }
}

/// Spend up to 1 minute trying to do the operation.
///
/// Even if Delta Chat itself does not hold the file lock,
/// there may be other processes such as antivirus,
/// or the filesystem may be network-mounted.
///
/// Without this workaround removing account may fail on Windows with an error
/// "The process cannot access the file because it is being used by another process. (os error 32)".
async fn try_many_times<F, Fut, T>(f: F) -> std::result::Result<(), T>
where
    F: Fn() -> Fut,
    Fut: Future<Output = std::result::Result<(), T>>,
{
    let mut counter = 0;
    loop {
        counter += 1;

        if let Err(err) = f().await {
            if counter > 60 {
                return Err(err);
            }

            // Wait 1 second and try again.
            tokio::time::sleep(std::time::Duration::from_millis(1000)).await;
        } else {
            break;
        }
    }
    Ok(())
}

/// Configuration of a single account.
#[derive(Serialize, Deserialize, Debug, Clone, PartialEq)]
struct AccountConfig {
    /// Unique id.
    pub id: u32,

    /// Root directory for all data for this account.
    ///
    /// The path is relative to the account manager directory.
    pub dir: std::path::PathBuf,

    /// Universally unique account identifier.
    pub uuid: Uuid,
}

impl AccountConfig {
    /// Get the canonical dbfile name for this configuration.
    pub fn dbfile(&self, accounts_dir: &Path) -> std::path::PathBuf {
        accounts_dir.join(&self.dir).join(DB_NAME)
    }
}

