import requests
from config.settings import BASE_URL


def test_api_is_up():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
