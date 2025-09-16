import logging
import pytest
import requests
from Config.config import BASE_URL, STATUS_CODES


@pytest.mark.DELETE
def test_post_object_delete(sample_payload):
    response = requests.post(BASE_URL, json=sample_payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "createdAt" in data

    # Storing ID for request chaining
    object_id = data["id"]


@pytest.mark.DELETE
def test_object_deletion(post_create_object):
    object_id = post_create_object

    logging.info("Sending DELETE request to delete created object")
    response = requests.delete(f"{BASE_URL}/" + object_id)

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]


@pytest.mark.DELETE
def test_object_already_deleted(post_create_object):
    object_id = post_create_object
    logging.info("Sending DELETE request to delete created object")
    response = requests.delete(f"{BASE_URL}/" + object_id)

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == [STATUS_CODES["NOT_FOUND"]]


@pytest.mark.DELETE
def test_invalid_object_deletion():

    logging.info("Sending DELETE request to delete created object")
    response = requests.delete(f"{BASE_URL}/" + "")

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code in [STATUS_CODES["NOT_FOUND"],STATUS_CODES["BAD_REQUEST"],STATUS_CODES["NOT_ALLOWED"]]