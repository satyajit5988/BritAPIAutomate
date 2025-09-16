import jsonpath
import pytest
import requests
import logging
from Config.config import BASE_URL, STATUS_CODES


@pytest.mark.END2END
def test_get_all_objects():
    global device_id1, device_id2
    logging.info("Sending GET request to fetch all objects")
    response = requests.get(BASE_URL)

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    device_id1 = jsonpath.jsonpath(response.json(), '$[0].id')
    device_id2 = jsonpath.jsonpath(response.json(), '$[1].id')
    logging.info(f"Device IDs fetched: {device_id1}, {device_id2}")
    assert device_id1[0] == "1"


@pytest.mark.END2END
def test_get_single_object():
    logging.info("Sending GET request to fetch single object")
    response = requests.get(f"{BASE_URL}/" + str(device_id1[0]))

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]
    data = response.json()
    assert "id" in data

    logging.info(f"Device IDs fetched:" + data["id"])
    assert data["id"] == "1"


@pytest.mark.END2END
def test_get_invalid_object():
    logging.info("Sending GET request to fetch invalid object")
    response = requests.get(f"{BASE_URL}/100")

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["NOT_FOUND"]


@pytest.mark.END2END
def test_put_update_object(post_create_object, sample_payload):
    object_id = post_create_object
    updated_payload = {**sample_payload, "name": "Poco M6 Pro", "price": 1799.0}

    logging.info("Sending PUT request to modify created object")
    response = requests.put(f"{BASE_URL}/" + object_id, json=updated_payload)
    data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    logging.info(f"Device name is:" + data["name"])
    assert data["name"] == "Poco M6 Pro"


@pytest.mark.END2END
def test_patch_update_object(post_create_object):
    object_id = post_create_object
    patch_payload = {"name": "POCO X7 Pro 5G 256GB Smartphone"}

    logging.info("Sending PATCH request to partially modify created object")
    response = requests.patch(f"{BASE_URL}/" + object_id, json=patch_payload)
    data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    logging.info(f"Device name is:" + data["name"])
    assert response.json()["name"] == "POCO X7 Pro 5G 256GB Smartphone"


@pytest.mark.END2END
def test_delete_object(post_create_object):
    object_id = post_create_object

    logging.info("Sending DELETE request to delete created object")
    response = requests.delete(f"{BASE_URL}/" + object_id)

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]

    # Verify if the object is deleted
    logging.info("Sending GET request to fetch deleted object")
    response_check = requests.get(f"{BASE_URL}/" + object_id)

    logging.info(f"Response status code: {response_check.status_code}")
    assert response_check.status_code == STATUS_CODES["NOT_FOUND"]
