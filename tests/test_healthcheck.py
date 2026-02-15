import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_api_is_up():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
