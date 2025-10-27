import json
import pytest
from pikahttp import Session

def test_get_request():
    session = Session()
    response = session.request(
        "GET",
        "https://httpbin.org/get",
        headers={"User-Agent": "pikahttp-test/0.1.0"}
    )
    assert response['status_code'] == 200
    content = json.loads(response['content'])
    assert content['headers']['User-Agent'] == "pikahttp-test/0.1.0"

def test_post_request():
    session = Session()
    data = {"test": "data"}
    response = session.request(
        "POST",
        "https://httpbin.org/post",
        headers={
            "User-Agent": "pikahttp-test/0.1.0",
            "Content-Type": "application/json"
        },
        body=json.dumps(data)
    )
    assert response['status_code'] == 200
    content = json.loads(response['content'])
    assert content['json'] == data

def test_custom_headers():
    session = Session()
    custom_headers = {
        "User-Agent": "pikahttp-test/0.1.0",
        "X-Test-Header": "test-value"
    }
    response = session.request(
        "GET",
        "https://httpbin.org/headers",
        headers=custom_headers
    )
    assert response['status_code'] == 200
    content = json.loads(response['content'])
    assert content['headers']['X-Test-Header'] == "test-value"