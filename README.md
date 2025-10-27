# PikaHTTP

A fast, Rust-powered HTTP client library for Python that aims to be a drop-in replacement for `requests` with significantly better performance.

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