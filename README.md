# 🚀 pikahttp

[![CI](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml/badge.svg)](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/pikahttp.svg)](https://pypi.org/project/pikahttp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/pikahttp.svg)](https://pypi.org/project/pikahttp/)

> A blazingly fast HTTP client for Python, powered by Rust and Hyper.

`pikahttp` combines Python’s ease of use with Rust’s performance, providing a simple yet powerful HTTP client that’s up to 18% faster than traditional Python HTTP libraries.

---

## ✨ Features

* ⚡ **Fast**: Built with Rust and Hyper for maximum performance
* 🔄 **Simple**: Clean, intuitive Python API
* 🛡️ **Reliable**: Battle-tested Rust libraries under the hood
* 💾 **Efficient**: Minimal memory allocations and zero-copy operations
* 🔒 **Safe**: Thread-safe and memory-safe by design
* 🚀 **Async-first**: Fully asynchronous HTTP requests

---

## 🔧 Installation

```bash
pip install pikahttp
```

### From Source

```bash
git clone https://github.com/GrandmaEJ/pikahttp.git
cd pikahttp
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pip install maturin
maturin develop
```

---

## 🚀 Quick Start

### Using Session

```python
from pikahttp import Session
import json

# Create a session
session = Session()

# GET request
response = session.request(
    "GET",
    "https://httpbin.org/get",
    headers={"User-Agent": "pikahttp/0.1.0"}
)
print(f"Status code: {response['status_code']}")
print(f"Content: {response['content']}")

# POST request with JSON
data = {"hello": "world"}
response = session.request(
    "POST",
    "https://httpbin.org/post",
    headers={
        "User-Agent": "pikahttp/0.1.0",
        "Content-Type": "application/json"
    },
    body=json.dumps(data)
)
print(f"Status code: {response['status_code']}")
print(f"Response: {response['content']}")
```

### Using Async Convenience Functions

```python
import asyncio
import pikahttp

async def main():
    response = await pikahttp.get(
        "https://api.github.com/events",
        headers={"User-Agent": "pikahttp/0.1.0"}
    )
    print(response.status_code)
    print(response.headers)
    print(response.json())

    response = await pikahttp.post(
        "https://httpbin.org/post",
        json={"key": "value"},
        headers={"User-Agent": "pikahttp/0.1.0"}
    )
    print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## ⚡ Performance

Based on benchmarks with 100 requests each:

| Library  | Mean (s) | Median (s) | Min (s) | Max (s) | StdDev (s) |
| -------- | -------- | ---------- | ------- | ------- | ---------- |
| urllib   | 0.2389   | 0.2351     | 0.2291  | 0.6488  | 0.0415     |
| requests | 0.2590   | 0.2575     | 0.2524  | 0.3014  | 0.0071     |
| pikahttp | 0.2193   | 0.2202     | 0.2162  | 0.2252  | 0.0021     |

* 🚀 **18.1% faster** than `requests`
* 🎯 **8.9% faster** than `urllib`
* 📊 More consistent performance (lower standard deviation)

---

## 🛠️ Development

### Running Tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest tests/
```

### Running Benchmarks

```bash
python benchmark.py
```

---

## 🔒 Security & Features

* Async-first design powered by Rust and Tokio
* HTTP/2 support
* Cookie handling
* Custom headers, query parameters, and JSON/form support
* Proper error handling and timeout configuration
* Session support

---

## 📖 Documentation

* [Examples](examples/)
* [API Reference](README.md#api-reference)

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for details.

