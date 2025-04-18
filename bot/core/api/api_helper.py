from typing import Any, Dict

from core.config import settings

from .api_abstract import ApiClient
from .api_implementation import RequestsApiClient


class UserRepository:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client: ApiClient = api_client

    def get_user(
        self, user_id: int, params: Dict[str, Any] = None
    ) -> Dict[str, Any] | None:

        return self.api_client.get(endpoint=f"/users/{user_id}", params=params)

    def get_all_users(self, params: Dict[str, Any] = None) -> Dict[str, Any]:
        return self.api_client.get(endpoint="/users", params=params)

    def create_user(self, data: Dict[str, Any]) -> Dict[str, Any]:
        user = self.get_user(user_id=data.get("user_id"))

        if user.get("user_id") is None:
            return self.api_client.post(endpoint="/users", data=data)

        return


api_client = RequestsApiClient(base_url=settings.api.base_url)

user_repository = UserRepository(api_client=api_client)
