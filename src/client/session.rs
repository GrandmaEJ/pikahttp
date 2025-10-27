use crate::runtime::{CLIENT, RUNTIME};
use bytes::Bytes;
use http_body_util::{BodyExt, Full};
use hyper::{Method, Request};
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyDict};
use std::collections::HashMap;

#[pyclass(name = "Session")]
pub struct PySession {}

#[pymethods]
impl PySession {
    #[new]
    pub fn new() -> PyResult<Self> {
        Ok(Self {})
    }

    #[pyo3(signature = (method, url, headers=None, body=None))]
    pub fn request<'py>(
        &self,
        py: Python<'py>,
        method: String,
        url: String,
        headers: Option<Bound<'py, PyDict>>,
        body: Option<String>,
    ) -> PyResult<Bound<'py, PyDict>> {
        let method = method
            .parse::<Method>()
            .map_err(|e| pyo3::exceptions::PyValueError::new_err(e.to_string()))?;

        let headers_map: HashMap<String, String> = match headers {
            Some(h) => h.extract()?,
            None => HashMap::new(),
        };

        let body_bytes = body.unwrap_or_default();

        let fut = async move {
            let mut builder = Request::builder().method(method).uri(&url);

            for (k, v) in &headers_map {
                builder = builder.header(k, v);
            }

            let body = Full::new(Bytes::from(body_bytes));
            let req = builder
                .body(body)
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))?;

            let client = CLIENT.clone();
            let resp = client
                .request(req)
                .await
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))?;

            let status = resp.status().as_u16();
            let hdrs = resp.headers().clone();
            let bytes = resp.into_body().collect().await
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))?
                .to_bytes();

            Ok::<_, pyo3::PyErr>((status, hdrs, bytes))
        };

        let (status, hdrs, bytes): (u16, _, Bytes) = RUNTIME.block_on(fut)?;

        let out = PyDict::new_bound(py);
        out.set_item("status_code", status)?;
        out.set_item("content", PyBytes::new_bound(py, &bytes))?;

        let hdict = PyDict::new_bound(py);
        for (k, v) in hdrs.iter() {
            hdict.set_item(k.as_str(), v.to_str().unwrap_or(""))?;
        }
        out.set_item("headers", hdict)?;

        Ok(out)
    }

    #[pyo3(signature = (url, headers=None))]
    pub fn get<'py>(
        &self,
        py: Python<'py>,
        url: String,
        headers: Option<Bound<'py, PyDict>>,
    ) -> PyResult<Bound<'py, PyDict>> {
        self.request(py, "GET".into(), url, headers, None)
    }

    #[pyo3(signature = (url, headers=None, body=None))]
    pub fn post<'py>(
        &self,
        py: Python<'py>,
        url: String,
        headers: Option<Bound<'py, PyDict>>,
        body: Option<String>,
    ) -> PyResult<Bound<'py, PyDict>> {
        self.request(py, "POST".into(), url, headers, body)
    }
}