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
    pub fn new() -> Self {
        Self {}
    }

    #[pyo3(signature = (method, url, headers=None, body=None))]
    pub fn request(
        &self,
        py: Python,
        method: String,
        url: String,
        headers: Option<&PyDict>,
        body: Option<String>,
    ) -> PyResult<Py<PyDict>> {
        let method = method
            .parse::<Method>()
            .map_err(|e| PyValueError::new_err(e.to_string()))?;

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
                .map_err(|e| PyRuntimeError::new_err(e.to_string()))?;

            let client = CLIENT.clone();
            let resp = client
                .request(req)
                .await
                .map_err(|e| PyRuntimeError::new_err(e.to_string()))?;

            let status = resp.status().as_u16();
            let hdrs = resp.headers().clone();
            let bytes = resp
                .into_body()
                .collect()
                .await
                .map_err(|e| PyRuntimeError::new_err(e.to_string()))?
                .to_bytes();

            Ok::<_, PyErr>((status, hdrs, bytes))
        };

        let (status, hdrs, bytes) = RUNTIME.block_on(fut)?;

        let out = PyDict::new(py);
        out.set_item("status_code", status)?;
        out.set_item("content", PyBytes::new(py, &bytes))?;

        let hdict = PyDict::new(py);
        for (k, v) in hdrs.iter() {
            hdict.set_item(k.as_str(), v.to_str().unwrap_or(""))?;
        }
        out.set_item("headers", hdict)?;

        Ok(out.into())
    }

    #[pyo3(signature = (url, headers=None))]
    pub fn get(
        &self,
        py: Python,
        url: String,
        headers: Option<&PyDict>,
    ) -> PyResult<Py<PyDict>> {
        self.request(py, "GET".into(), url, headers, None)
    }

    #[pyo3(signature = (url, headers=None, body=None))]
    pub fn post(
        &self,
        py: Python,
        url: String,
        headers: Option<&PyDict>,
        body: Option<String>,
    ) -> PyResult<Py<PyDict>> {
        self.request(py, "POST".into(), url, headers, body)
    }
}
