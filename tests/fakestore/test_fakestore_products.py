import pytest
from utils.api_client import APIClient
from config.settings import FAKESTORE_URL


@pytest.mark.api
@pytest.mark.regression
def test_get_all_products():
    client = APIClient(FAKESTORE_URL)
    response = client.get("/products")

    assert response.status_code == 200, "Expected status code 200"

    data = response.json()

    assert isinstance(data, list), "Products response should be a list"
    assert len(data) > 0, "Products list should not be empty"

    first_product = data[0]

    assert "id" in first_product, "Product should contain id"
    assert "title" in first_product, "Product should contain title"
    assert "price" in first_product, "Product should contain price"
