import requests
from jsonschema import validate
from tests.schemas import get_single_user, create_user, update_user

url = "https://reqres.in/api/users/"
user_id = "2"
invalid_user_id = "23"


def test_get_single_user():
    response = requests.get(url + user_id)
    assert response.status_code == 200
    validate(response.json(), schema=get_single_user)


def test_post_create_new_user():
    data = {"name": "Neo", "job": "chosen"}
    response = requests.post(url, data)
    assert response.status_code == 201
    validate(response.json(), schema=create_user)


def test_put_update_user():
    data = {"name": "Neo", "job": "chosen"}
    response = requests.put(url + user_id, data)
    assert response.status_code == 200
    validate(response.json(), schema=update_user)


def test_delete_user():
    response = requests.delete(url + user_id)
    assert response.status_code == 204


def test_get_user_not_found():
    response = requests.get(url + invalid_user_id)
    assert response.status_code == 404
    validate(response.json(), schema={})
