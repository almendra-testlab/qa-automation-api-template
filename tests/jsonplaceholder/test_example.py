import pytest
from utils.api_client import APIClient
from config.settings import JSONPLACEHOLDER_URL

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("endpoint", [
    "/posts",
    "/comments",
    "/albums",
])
def test_endpoints_return_data(endpoint):
    client = APIClient(JSONPLACEHOLDER_URL)
    response = client.get(endpoint)

    assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    data = response.json()

    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, "Response list is empty"

