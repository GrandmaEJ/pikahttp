use hyper_util::client::legacy::{connect::HttpConnector, Client};
use hyper_util::rt::TokioExecutor;
use hyper_tls::HttpsConnector;
use once_cell::sync::Lazy;
use std::sync::Arc;
use tokio::runtime::Runtime;
use hyper::body::Body;

/// global tokio runtime
pub static RUNTIME: Lazy<Runtime> = Lazy::new(|| {
    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .worker_threads(4)
        .build()
        .expect("Failed to create Tokio runtime")
});

/// shared hyper client
pub static CLIENT: Lazy<Arc<Client<HttpsConnector<HttpConnector>, Body>>> = Lazy::new(|| {
    let https = HttpsConnector::new();
    Arc::new(Client::builder(TokioExecutor::new())
        .pool_idle_timeout(None)
        .build::<_, Body>(https))
});