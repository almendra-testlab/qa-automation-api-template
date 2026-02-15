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


@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("product_id", [1, 2, 3, 4, 5])
def test_get_single_product_by_id(product_id):
    client = APIClient(FAKESTORE_URL)
    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200, f"Product {product_id} not found"

    product = response.json()

    assert isinstance(product, dict), "Single product should be an object"
    assert product["id"] == product_id, "Returned product ID mismatch"

    validate_product_schema(product)
