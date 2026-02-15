import pytest
from utils.api_client import APIClient
from config.settings import FAKESTORE_URL


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

    # required fields
    required_fields = ["id", "title", "price", "description", "category", "image", "rating"]

    for field in required_fields:
        assert field in product, f"Missing field: {field}"

    # type validations
    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], (int, float))
    assert isinstance(product["description"], str)
    assert isinstance(product["category"], str)
    assert isinstance(product["image"], str)
    assert isinstance(product["rating"], dict)

    rating = product["rating"]
    assert "rate" in rating and "count" in rating
    assert isinstance(rating["rate"], (int, float))
    assert isinstance(rating["count"], int)
