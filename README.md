# pikahttp

A fast HTTP client for Python powered by Rust and Hyper.

## Features

- Fast: Written in Rust using the high-performance Hyper HTTP library
- Simple: Clean Python API that's easy to use
- Reliable: Built on battle-tested Rust libraries
- Memory efficient: Minimizes allocations and copies

## Installation

```bash
pip install pikahttp
```

## Quick Start

```python
from pikahttp import Session

# Create a session
session = Session()

# Make a GET request
response = session.request(
    "GET", 
    "https://api.github.com/zen",
    headers={"User-Agent": "pikahttp/0.1.0"}
)

# Print response
print(f"Status code: {response['status_code']}")
print(f"Content: {response['content']}")
```

## Performance

Based on benchmarks making 100 HTTP requests to api.ipify.org:

```
Library         Mean (s)     Median (s)   Min (s)      Max (s)      StdDev (s)  
--------------------------------------------------------------------------------
urllib         0.2389       0.2351       0.2291       0.6488       0.0415      
requests       0.2590       0.2575       0.2524       0.3014       0.0071      
pikahttp       0.2193       0.2202       0.2162       0.2252       0.0021      
```

Key findings:
- 8.9% faster than urllib
- 18.1% faster than requests
- More consistent performance (lower standard deviation)

## Examples

See the `examples/` directory for more usage examples.

## License

MIT License. See LICENSE file for details.

## Features

- Async-first design powered by Rust and Tokio
- Simple, requests-like API
- HTTP/2 support
- Cookie handling
- Custom headers
- Query parameters
- JSON support
- Form data support
- Timeout configuration
- Session support

## Installation

```bash
pip install pikahttp
```

## Quick Start

```python
import asyncio
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