import pytest
import requests
from config.settings import JSONPLACEHOLDER_URL

@pytest.mark.smoke
@pytest.mark.api
def test_api_is_up():
    response = requests.get(JSONPLACEHOLDER_URL)
    assert response.status_code == 200
