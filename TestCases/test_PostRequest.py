import pytest
import requests
from Config.config import BASE_URL


@pytest.mark.POST
@pytest.mark.SMOKE
def test_post_object(sample_payload):
    response = requests.post(BASE_URL, json=sample_payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "createdAt" in data


@pytest.mark.POST
def test_invalid_post_object(empty_payload):
    response = requests.post(BASE_URL, json=empty_payload)
    assert response.status_code == 400

