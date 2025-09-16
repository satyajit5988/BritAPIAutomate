import jsonpath
import pytest
import requests
import logging
from Config.config import BASE_URL, STATUS_CODES


@pytest.mark.GET
@pytest.mark.SMOKE
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


@pytest.mark.GET
def test_get_multiple_objects():
    params = [("id", device_id1[0]), ("id", device_id2[0])]
    logging.info("Sending GET request to fetch single object")
    response = requests.get(f"{BASE_URL}/", params=params)

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]


@pytest.mark.GET
@pytest.mark.SMOKE
def test_get_single_object():
    logging.info("Sending GET request to fetch single object")
    response = requests.get(f"{BASE_URL}/" + str(device_id1[0]))

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]
    data = response.json()
    assert "id" in data

    logging.info(f"Device IDs fetched:" + data["id"])
    assert data["id"] == "1"


@pytest.mark.GET
def test_get_object_no_id():
    logging.info("Sending GET request to fetch single object")
    response = requests.get(f"{BASE_URL}/" + "")

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["SUCCESS"]


@pytest.mark.GET
def test_get_invalid_object():
    logging.info("Sending GET request to fetch invalid object")
    response = requests.get(f"{BASE_URL}/100")

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == STATUS_CODES["NOT_FOUND"]