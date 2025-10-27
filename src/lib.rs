use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyDict};
use reqwest::header::{HeaderMap, HeaderName, HeaderValue};
use reqwest::Method;
use std::collections::HashMap;
use std::time::Duration;

/// Python-exposed HTTP session class using reqwest
#[pyclass(name = "Session")]
struct PySession {
    client: reqwest::Client,
}

#[pymethods]
impl PySession {
    #[new]
    fn new() -> PyResult<Self> {
        let client = reqwest::Client::builder()
            .cookie_store(true)
            .build()
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
        Ok(Self { client })
    }

    fn request<'p>(
        &self,
        py: Python<'p>,
        method: String,
        url: String,
        headers: Option<HashMap<String, String>>,
        params: Option<HashMap<String, String>>,
        json: Option<HashMap<String, String>>,
        data: Option<HashMap<String, String>>,
        timeout: Option<f64>,
    ) -> PyResult<&'p PyAny> {
        let client = self.client.clone();
        let method = method
            .parse::<Method>()
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;

        pyo3_asyncio::tokio::future_into_py(py, async move {
            let mut request = client.request(method, url);

            // Set headers
            if let Some(headers_map) = headers {
                let mut header_map = HeaderMap::new();
                for (key, value) in headers_map {
                    header_map.insert(
                        HeaderName::from_bytes(key.as_bytes())
                            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?,
                        HeaderValue::from_str(&value)
                            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?,
                    );
                }
                request = request.headers(header_map);
            }

            // Set query parameters
            if let Some(params_map) = params {
                request = request.query(&params_map);
            }

            // Set JSON body
            if let Some(json_map) = json {
                request = request.json(&json_map);
            }

            // Set form data
            if let Some(form_data) = data {
                request = request.form(&form_data);
            }

            // Set timeout
            if let Some(secs) = timeout {
                request = request.timeout(Duration::from_secs_f64(secs));
            }

            // Send request
            let response = request
                .send()
                .await
                .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;

            let status_code = response.status().as_u16();
            let headers = response.headers().clone();
            let body_bytes = response
                .bytes()
                .await
                .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;

            // Convert to Python dictionary safely
            Python::with_gil(|py| {
                let response_dict = PyDict::new(py);
                response_dict.set_item("status_code", status_code)?;
                response_dict.set_item("content", PyBytes::new(py, &body_bytes))?;

                let headers_dict = PyDict::new(py);
                for (key, value) in headers.iter() {
                    headers_dict.set_item(
                        key.as_str(),
                        value.to_str().unwrap_or("").to_string(),
                    )?;
                }
                response_dict.set_item("headers", headers_dict)?;
                Ok(response_dict.to_object(py))  // ✅ FIXED: return PyObject, not &PyDict
            })
        })
    }

    fn get<'p>(
        &self,
        py: Python<'p>,
        url: String,
        headers: Option<&PyDict>,
        params: Option<&PyDict>,
        timeout: Option<f64>,
    ) -> PyResult<&'p PyAny> {
        let headers_map: Option<HashMap<String, String>> = headers.map(|h| h.extract().unwrap());
        let params_map: Option<HashMap<String, String>> = params.map(|p| p.extract().unwrap());
        self.request(py, "GET".into(), url, headers_map, params_map, None, None, timeout)
    }

    fn post<'p>(
        &self,
        py: Python<'p>,
        url: String,
        headers: Option<&PyDict>,
        params: Option<&PyDict>,
        json: Option<&PyDict>,
        data: Option<&PyDict>,
        timeout: Option<f64>,
    ) -> PyResult<&'p PyAny> {
        let headers_map: Option<HashMap<String, String>> = headers.map(|h| h.extract().unwrap());
        let params_map: Option<HashMap<String, String>> = params.map(|p| p.extract().unwrap());
        let json_map: Option<HashMap<String, String>> = json.map(|j| j.extract().unwrap());
        let data_map: Option<HashMap<String, String>> = data.map(|d| d.extract().unwrap());
        self.request(py, "POST".into(), url, headers_map, params_map, json_map, data_map, timeout)
    }
}

#[pymodule]
fn _core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PySession>()?;
    Ok(())
}
