def validate_product_schema(product: dict):
    required_fields = [
        "id",
        "title",
        "price",
        "description",
        "category",
        "image",
        "rating",
    ]

    for field in required_fields:
        assert field in product, f"Missing field: {field}"

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
