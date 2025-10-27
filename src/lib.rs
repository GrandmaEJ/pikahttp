mod client;
mod runtime;

use pyo3::prelude::*;

#[pymodule]
fn pikahttp(py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<client::PySession>()?;
    Ok(())
}
