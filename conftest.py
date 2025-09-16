import pytest
import requests
import logging

from Config.config import BASE_URL


@pytest.fixture(scope="module")
def sample_payload():
    return {
        "name": "Test Object",
        "data": {
            "year": 2025,
            "price": 123.45,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

@pytest.fixture(scope="module")
def empty_payload():
    return {}


@pytest.fixture(scope="module")
def post_create_object(sample_payload):
    response = requests.post(BASE_URL, json=sample_payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "createdAt" in data

    # Storing ID for request chaining
    object_id = data["id"]
    yield object_id


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)