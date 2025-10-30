use bytes::Bytes;
use http_body_util::Full;
use hyper_tls::HttpsConnector;
use hyper_util::client::legacy::Client as LegacyClient;
use hyper_util::client::legacy::{connect::HttpConnector, Builder};
use hyper_util::rt::TokioExecutor;
use once_cell::sync::Lazy;
use std::sync::Arc;
use tokio::runtime::Runtime;

/// global tokio runtime
pub static RUNTIME: Lazy<Runtime> = Lazy::new(|| {
    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .worker_threads(4)
        .build()
        .expect("Failed to create Tokio runtime")
});

/// shared hyper client
pub static CLIENT: Lazy<Arc<LegacyClient<HttpsConnector<HttpConnector>, Full<Bytes>>>> =
    Lazy::new(|| {
        let https = HttpsConnector::new();
        Arc::new(
            Builder::new(TokioExecutor::new())
                .pool_idle_timeout(None)
                .build(https),
        )
    });
