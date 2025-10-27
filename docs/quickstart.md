# Quick Start

## Basic Usage

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

## Making POST Requests

```python
import json

# Create a session
session = Session()

# Set headers
headers = {
    "User-Agent": "pikahttp/0.1.0",
    "Content-Type": "application/json"
}

# Prepare data
data = {
    "title": "Test Post",
    "body": "This is a test post"
}

# Make POST request
response = session.request(
    "POST",
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers,
    body=json.dumps(data)
)

# Print response
print(f"Status code: {response['status_code']}")
print(f"Response: {response['content']}")
```

## Using Custom Headers

```python
# Create a session
session = Session()

# Set custom headers
headers = {
    "User-Agent": "pikahttp/0.1.0",
    "Accept": "application/vnd.github.v3+json",
    "X-Custom-Header": "custom value"
}

# Make request with custom headers
response = session.request(
    "GET",
    "https://api.github.com/users/octocat",
    headers=headers
)

# Print response
print(f"Status code: {response['status_code']}")
print(f"Response headers:")
print(response.get("headers", {}))
```