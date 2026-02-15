from utils.api_client import APIClient
from config.settings import BASE_URL

def test_get_posts():
    client = APIClient(BASE_URL)
    response = client.get("/posts")

    assert response.status_code == 200
    assert len(response.json()) > 0
