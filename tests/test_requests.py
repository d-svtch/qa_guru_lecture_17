import requests
from jsonschema import validate
from schemas.schemas import get_single_user, create_user, update_user

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
    assert response.json()["name"] == "Neo"
    assert response.json()["job"] == "chosen"



def test_put_update_user():
    old_data = {"name": "Neo", "job": "chosen"}
    response = requests.post(url, old_data)
    user_to_update = response.json()["id"]

    new_data = {"name": "Morpheus", "job": "leader"}
    response = requests.put(url + user_to_update, new_data)
    assert response.status_code == 200
    validate(response.json(), schema=update_user)
    assert response.json()["name"] == "Morpheus"
    assert response.json()["job"] == "leader"


def test_delete_user():
    data = {"name": "Neo", "job": "chosen"}
    create_response = requests.post(url, data)
    user_to_delete = create_response.json()["id"]

    delete_response = requests.delete(url + user_to_delete)
    assert delete_response.status_code == 204


def test_get_user_not_found():
    response = requests.get(url + invalid_user_id)
    assert response.status_code == 404
    validate(response.json(), schema={})
