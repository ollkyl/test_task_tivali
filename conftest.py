import pytest
import requests


@pytest.fixture(scope="session")
def session() -> requests.Session:
    s = requests.Session()
    yield s
    s.close()


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base API URL."""
    return "https://jsonplaceholder.typicode.com"
