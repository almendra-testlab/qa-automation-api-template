import pytest
from utils.api_client import APIClient
from config.settings import FAKESTORE_URL
from utils.validators import validate_product_schema


@pytest.mark.api
@pytest.mark.regression
def test_get_all_products_contract():
    client = APIClient(FAKESTORE_URL)
    response = client.get("/products")

    assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    products = response.json()

    assert isinstance(products, list), "Products response should be a list"
    assert len(products) > 0, "Products list should not be empty"

    product = products[0]
    validate_product_schema(product)
