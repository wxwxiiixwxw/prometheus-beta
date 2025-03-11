import pytest
import requests
from src.http_get_request import send_http_get_request

class MockResponse:
    def __init__(self, status_code=200, headers=None, text="", json_data=None):
        self.status_code = status_code
        self.headers = headers or {}
        self._text = text
        self._json = json_data
        
    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.exceptions.HTTPError(f"HTTP Error {self.status_code}")
    
    @property
    def text(self):
        return self._text
    
    def json(self):
        return self._json

def test_valid_http_get_request(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(
            status_code=200, 
            headers={'content-type': 'application/json'},
            text='{"key": "value"}',
            json_data={"key": "value"}
        )
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    result = send_http_get_request('https://example.com')
    
    assert result['status_code'] == 200
    assert result['content'] == '{"key": "value"}'
    assert result['json'] == {"key": "value"}

def test_http_get_request_with_headers(monkeypatch):
    def mock_get(*args, **kwargs):
        assert kwargs['headers'] == {'Authorization': 'Bearer token'}
        return MockResponse(status_code=200)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    send_http_get_request(
        'https://example.com', 
        headers={'Authorization': 'Bearer token'}
    )

def test_http_get_request_with_params(monkeypatch):
    def mock_get(*args, **kwargs):
        assert kwargs['params'] == {'key1': 'value1'}
        return MockResponse(status_code=200)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    send_http_get_request(
        'https://example.com', 
        params={'key1': 'value1'}
    )

def test_invalid_url_raises_error():
    with pytest.raises(ValueError):
        send_http_get_request('')
    
    with pytest.raises(ValueError):
        send_http_get_request(None)

def test_http_request_failure(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.exceptions.RequestException("Connection Error")
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(RuntimeError, match="HTTP GET request failed"):
        send_http_get_request('https://example.com')

def test_http_status_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(status_code=404)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(requests.exceptions.HTTPError):
        send_http_get_request('https://example.com')