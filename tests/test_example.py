import pytest
from utils.api_client import APIClient
from config.settings import BASE_URL


@pytest.mark.parametrize("endpoint", [
    "/posts",
    "/comments",
    "/albums",
])
def test_endpoints_return_data(endpoint):
    client = APIClient(BASE_URL)
    response = client.get(endpoint)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

