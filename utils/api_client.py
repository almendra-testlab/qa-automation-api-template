import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET request to: {url}")

        response = requests.get(url)

        logger.info(f"Response status: {response.status_code}")

        return response

