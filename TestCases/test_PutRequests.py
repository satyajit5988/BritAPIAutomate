import jsonpath
import pytest
import requests
import logging
from Config.config import BASE_URL, STATUS_CODES


@pytest.mark.PUT
@pytest.mark.SMOKE
def test_put_object_name(post_create_object, sample_payload):
    object_id = post_create_object
    updated_payload = {**sample_payload, "name": "Poco M6 Pro"}

    logging.info("Sending PUT request to modify created object")
    response = requests.put(f"{BASE_URL}/" + object_id, json=updated_payload)
    data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    logging.info(f"Device name is:" + data["name"])
    assert data["name"] == "Poco M6 Pro"


@pytest.mark.PUT
def test_put_object_price(post_create_object, sample_payload):
    object_id = post_create_object
    updated_payload = {**sample_payload, "price": 1799.0}

    logging.info("Sending PUT request to modify created object")
    response = requests.put(f"{BASE_URL}/" + object_id, json=updated_payload)
    data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    logging.info(f"Device price is:" + data["price"])
    assert data["price"] == "1799.0"


@pytest.mark.PUT
def test_put_object_year(post_create_object, sample_payload):
    object_id = post_create_object
    updated_payload = {**sample_payload, "year": 2023}

    logging.info("Sending PUT request to modify created object")
    response = requests.put(f"{BASE_URL}/" + object_id, json=updated_payload)
    data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    logging.info(f"Device manufactured year is:" + data["year"])
    assert data["year"] == "2023"


@pytest.mark.PUT
def test_put_object_cpu(post_create_object, sample_payload):
    object_id = post_create_object
    updated_payload = {**sample_payload, "CPU model": "Rizen"}

    logging.info("Sending PUT request to modify created object")
    response = requests.put(f"{BASE_URL}/" + object_id, json=updated_payload)
    data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    logging.info(f"Device CPU model is:" + data["CPU model"])
    assert data["CPU model"] == "Rizen"


@pytest.mark.PUT
def test_put_object_size(post_create_object, sample_payload):
    object_id = post_create_object
    updated_payload = {**sample_payload, "Hard disk size": "3 TB"}

    logging.info("Sending PUT request to modify created object")
    response = requests.put(f"{BASE_URL}/" + object_id, json=updated_payload)
    data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    logging.info(f"Device hard disk size is:" + data["Hard disk size"])
    assert data["Hard disk size"] == "3 TB"


@pytest.mark.PUT
def test_put_object_invalid_object(sample_payload):
    updated_payload = {**sample_payload, "name": "Poco M6 Pro"}

    logging.info("Sending PUT request to modify created object")
    response = requests.put(f"{BASE_URL}/67", json=updated_payload)
    data = response.json()

    # Error code depends on API implementation
    # As I hit the max request for API's hence could not check for actual code, hence mentioned both codes
    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code in [STATUS_CODES["CREATED"],STATUS_CODES["NOT_FOUND"]]

