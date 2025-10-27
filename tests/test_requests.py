import json
import pytest
from pikahttp import Session
from tests.mock_server import MockServer

@pytest.fixture
def mock_server():
    server = MockServer()
    base_url = server.start()
    yield base_url
    server.stop()

def test_get_request(mock_server):
    session = Session()
    response = session.request(
        "GET",
        f"{mock_server}/get",
        headers={"User-Agent": "pikahttp-test/0.1.0"}
    )
    assert response['status_code'] == 200
    content = json.loads(response['content'])
    assert content['headers']['User-Agent'] == "pikahttp-test/0.1.0"
    assert content['method'] == 'GET'

def test_post_request(mock_server):
    session = Session()
    data = {"test": "data"}
    response = session.request(
        "POST",
        f"{mock_server}/post",
        headers={
            "User-Agent": "pikahttp-test/0.1.0",
            "Content-Type": "application/json"
        },
        body=json.dumps(data)
    )
    assert response['status_code'] == 200
    content = json.loads(response['content'])
    assert content['json'] == data
    assert content['method'] == 'POST'

def test_custom_headers(mock_server):
    session = Session()
    custom_headers = {
        "User-Agent": "pikahttp-test/0.1.0",
        "X-Test-Header": "test-value"
    }
    response = session.request(
        "GET",
        f"{mock_server}/headers",
        headers=custom_headers
    )
    assert response['status_code'] == 200
    content = json.loads(response['content'])
    assert content['headers']['X-Test-Header'] == "test-value"
