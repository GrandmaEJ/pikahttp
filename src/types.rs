use pyo3::exceptions;
use pyo3::PyErr;
use std::error::Error;
use std::fmt;

#[derive(Debug)]
pub enum HttpError {
    RequestError(String),
    HeaderError(String),
    RuntimeError(String),
}

impl fmt::Display for HttpError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            HttpError::RequestError(msg) => write!(f, "Request error: {}", msg),
            HttpError::HeaderError(msg) => write!(f, "Header error: {}", msg),
            HttpError::RuntimeError(msg) => write!(f, "Runtime error: {}", msg),
        }
    }
}

impl Error for HttpError {}

impl From<reqwest::Error> for HttpError {
    fn from(err: reqwest::Error) -> Self {
        HttpError::RequestError(err.to_string())
    }
}

impl From<HttpError> for PyErr {
    fn from(err: HttpError) -> PyErr {
        match err {
            HttpError::RequestError(msg) => exceptions::PyValueError::new_err(msg),
            HttpError::HeaderError(msg) => exceptions::PyValueError::new_err(msg),
            HttpError::RuntimeError(msg) => exceptions::PyRuntimeError::new_err(msg),
        }
    }
}

pub type Result<T> = std::result::Result<T, HttpError>;