import pytest, requests, json
import os, time

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://reqres.in/api",
        help="Base URL for the API under test",
    )
    parser.addoption(
        "--api-key",
        action="store",
        default="reqres-free-v1",
        help="ReqRes API key (x-api-key header)"
    )
    parser.addoption(
        "--max-ms",
        type=int,
        default=int(os.getenv("API_MAX_MS", "1500")),
        help="Max acceptable response time in milliseconds for perf assertions",
    )

@pytest.fixture(scope="session")
def base_url(pytestconfig) -> str:
    """Base URL for all tests (overridable via --base-url)."""
    return pytestconfig.getoption("base_url")

@pytest.fixture(scope="session")
def max_ms(pytestconfig) -> int:
    """Global performance threshold (ms)."""
    return pytestconfig.getoption("max_ms")

@pytest.fixture(scope="session")
def api(pytestconfig) -> requests.Session:
    """Shared HTTP session with default headers."""
    s = requests.Session()
    # expect the response body to be JSON
    s.headers.update({"Accept": "application/json"})
    # add the API key header
    s.headers.update({"x-api-key": pytestconfig.getoption("api_key")})
    
    def _log_response(response): # HELPER function to log requests information
        print(f"\n{response.request.method} {response.request.url}")
        print(f"{response.status_code} {response.reason}")
        try:
            print(json.dumps(response.json(), indent=2))
        except ValueError:
            print(response.text[:400])
    
    # get the original request
    original_request = s.request

    def logged_request(method, url, **kwargs):
        response = original_request(method, url, **kwargs)
        _log_response(response)
        return response
    s.request = logged_request
    return s
