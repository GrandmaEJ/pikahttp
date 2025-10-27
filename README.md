# 🚀 pikahttp# 🚀 pikahttp



[![CI](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml/badge.svg)](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml)[![CI](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml/badge.svg)](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml)

[![PyPI version](https://badge.fury.io/py/pikahttp.svg)](https://badge.fury.io/py/pikahttp)[![PyPI version](https://badge.fury.io/py/pikahttp.svg)](https://badge.fury.io/py/pikahttp)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python Versions](https://img.shields.io/pypi/pyversions/pikahttp.svg)](https://pypi.org/project/pikahttp/)

> A blazingly fast HTTP client for Python, powered by Rust and Hyper

> A blazingly fast HTTP client for Python, powered by Rust and Hyper

`pikahttp` combines Python's ease of use with Rust's performance, providing a simple yet powerful HTTP client that's up to 18% faster than traditional Python HTTP libraries.

`pikahttp` combines Python's ease of use with Rust's performance, providing a simple yet powerful HTTP client that's up to 18% faster than traditional Python HTTP libraries.

## ✨ Features

## ✨ Features

⚡️ **Fast**: Built with Rust and Hyper for maximum performance  

⚡️ **Fast**: Built with Rust and Hyper for maximum performance  🔄 **Simple**: Clean, intuitive Python API  

🔄 **Simple**: Clean, intuitive Python API  🛡️ **Reliable**: Battle-tested Rust libraries under the hood  

🛡️ **Reliable**: Battle-tested Rust libraries under the hood  💾 **Efficient**: Minimal memory allocations and zero-copy operations  

💾 **Efficient**: Minimal memory allocations and zero-copy operations  🔒 **Safe**: Thread-safe and memory-safe by design

🔒 **Safe**: Thread-safe and memory-safe by design

## Installation

## 🔧 Installation

```bash

### From PyPI (Recommended)pip install pikahttp

```bash```

pip install pikahttp

```## Quick Start



### From Source```python

```bashfrom pikahttp import Session

# Clone the repository

git clone https://github.com/GrandmaEJ/pikahttp.git# Create a session

cd pikahttpsession = Session()



# Create and activate virtual environment# GET request

python -m venv .venvresponse = session.request(

source .venv/bin/activate  # On Windows: .venv\Scripts\activate    "GET", 

    "https://httpbin.org/get",

# Install development dependencies    headers={"User-Agent": "pikahttp/0.1.0"}

pip install -r requirements-dev.txt)

print(f"Status code: {response['status_code']}")

# Build and installprint(f"Content: {response['content']}")

pip install maturin

maturin build --release# POST request with JSON

pip install target/wheels/*.whlimport json

```data = {"hello": "world"}

response = session.request(

## 🚀 Quick Start    "POST",

    "https://httpbin.org/post",

```python    headers={

from pikahttp import Session        "User-Agent": "pikahttp/0.1.0",

        "Content-Type": "application/json"

# Create a session    },

session = Session()    body=json.dumps(data)

)

# Make a GET requestprint(f"Status code: {response['status_code']}")

response = session.request(print(f"Response: {response['content']}")

    "GET", ```

    "https://api.github.com/zen",

    headers={"User-Agent": "pikahttp/0.1.0"}## Examples

)

print(f"Status: {response['status_code']}")### Basic GET Request

print(f"Content: {response['content'].decode()}")```python

```from pikahttp import Session



## 📚 Examplessession = Session()

response = session.request(

### POST Request with JSON    "GET",

```python    "https://httpbin.org/get",

import json    headers={"User-Agent": "pikahttp/0.1.0"}

from pikahttp import Session)

```

session = Session()

data = {"hello": "world"}### POST with JSON Data

```python

response = session.request(import json

    "POST",from pikahttp import Session

    "https://httpbin.org/post",

    headers={session = Session()

        "User-Agent": "pikahttp/0.1.0",data = {"hello": "world"}

        "Content-Type": "application/json"response = session.request(

    },    "POST",

    body=json.dumps(data)    "https://httpbin.org/post",

)    headers={

```        "User-Agent": "pikahttp/0.1.0",

        "Content-Type": "application/json"

### Custom Headers    },

```python    body=json.dumps(data)

from pikahttp import Session)

```

session = Session()

headers = {### Custom Headers

    "User-Agent": "pikahttp/0.1.0",```python

    "X-Custom-Header": "custom value",from pikahttp import Session

    "Accept": "application/json"

}session = Session()

headers = {

response = session.request(    "User-Agent": "pikahttp/0.1.0",

    "GET",    "X-Custom-Header": "custom value",

    "https://httpbin.org/headers",    "Accept": "application/json"

    headers=headers}

)response = session.request(

```    "GET",

    "https://httpbin.org/headers",

## ⚡️ Performance    headers=headers

)

Based on our benchmarks:```



```## Performance

Library         Mean (s)     Median (s)   Min (s)      Max (s)      StdDev (s)  

--------------------------------------------------------------------------------Based on benchmarks making 100 HTTP requests:

urllib         0.2389       0.2351       0.2291       0.6488       0.0415      

requests       0.2590       0.2575       0.2524       0.3014       0.0071      ```

pikahttp       0.2193       0.2202       0.2162       0.2252       0.0021      Library         Mean (s)     Median (s)   Min (s)      Max (s)      StdDev (s)  

```--------------------------------------------------------------------------------

urllib         0.2389       0.2351       0.2291       0.6488       0.0415      

- 🚀 **18.1% faster** than requestsrequests       0.2590       0.2575       0.2524       0.3014       0.0071      

- 🎯 **8.9% faster** than urllibpikahttp       0.2193       0.2202       0.2162       0.2252       0.0021      

- 📊 **More consistent** performance (lower standard deviation)```



## 🛠️ DevelopmentKey findings:

- 8.9% faster than urllib

### Running Tests- 18.1% faster than requests

```bash- More consistent performance (lower standard deviation)

# Create and activate virtualenv first

python -m venv .venv## Development

source .venv/bin/activate

### Running Tests

# Install dev dependencies```bash

pip install -r requirements-dev.txtpytest tests/

```

# Run tests

pytest tests/### Running Benchmarks

``````bash

python benchmark.py

### Running Benchmarks```

```bash

python benchmark.py## License

```

MIT License. See LICENSE file for details.

## 📖 Documentation

## Features

- [Examples](examples/)

- [API Reference](README.md#api-reference)- Async-first design powered by Rust and Tokio

- [Contributing Guidelines](CONTRIBUTING.md)- Simple, requests-like API

- HTTP/2 support

## 🔒 Security- Cookie handling

- Custom headers

This library follows best practices:- Query parameters

- Memory-safe Rust implementation- JSON support

- No blocking operations in async contexts- Form data support

- Proper error handling- Timeout configuration

- Regular security audits through CI- Session support



## 📝 License## Installation



MIT License - see [LICENSE](LICENSE) for details```bash

pip install pikahttp

## 🙏 Acknowledgments```



Built with:## Quick Start

- [Rust](https://www.rust-lang.org/)

- [Hyper](https://hyper.rs/)```python

- [PyO3](https://pyo3.rs/)import asyncio
import pikahttp

async def main():
    # Simple GET request
    response = await pikahttp.get('https://api.github.com/events')
    print(response.status_code)
    print(response.headers)
    print(response.json())

    # POST request with JSON data
    response = await pikahttp.post(
        'https://api.example.com/data',
        json={'key': 'value'},
        headers={'Authorization': 'Bearer token'}
    )
    print(response.text)

    # Using a session
    client = pikahttp.create_client()
    response = await client.get('https://api.example.com/data')
    print(response.json())

if __name__ == '__main__':
    asyncio.run(main())
```

## Key Differences from Requests

1. Async-first: All HTTP operations are asynchronous
2. Better Performance: Powered by Rust and reqwest
3. Modern Python: Type hints and async/await syntax
4. Memory Efficient: Rust-based memory management

## Performance

PikaHTTP is significantly faster than the requests library due to:
- Rust implementation of core functionality
- Async I/O with Tokio
- Efficient memory management
- HTTP/2 support by default

## License

MIT License