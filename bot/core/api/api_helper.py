from typing import Any, Dict

from core.config import settings

from .api_abstract import ApiClient
from .api_implementation import RequestsApiClient

class UserRepository:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client: ApiClient = api_client

    def get_all_users(self, params: Dict[str, Any] = None) -> Dict[str, Any]:
        return self.api_client.get(endpoint="/users", params=params)

    def create_user(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return self.api_client.post(endpoint="/users", data=data)

api_client = RequestsApiClient(
    base_url=settings.api.base_url
)

user_repository = UserRepository(api_client=api_client)