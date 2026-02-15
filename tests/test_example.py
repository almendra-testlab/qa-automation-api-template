from utils.api_client import APIClient
from config.settings import BASE_URL


def test_get_posts():
    client = APIClient(BASE_URL)
    response = client.get("/posts")

    assert response.status_code == 200

    data = response.json()

    # validar que hay datos
    assert isinstance(data, list)
    assert len(data) > 0

    # validar estructura del primer post
    first_post = data[0]

    assert "userId" in first_post
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post

    # validar tipos
    assert isinstance(first_post["userId"], int)
    assert isinstance(first_post["id"], int)
    assert isinstance(first_post["title"], str)
    assert isinstance(first_post["body"], str)
