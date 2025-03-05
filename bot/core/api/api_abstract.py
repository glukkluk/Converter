from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


# Абстракція (інтерфейс) для взаємодії з API
class ApiClient(ABC):
    """
    Описує методи які будуть використовувати для взаємодії з API
    """

    @abstractmethod
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    def patch(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    def delete(self, endpoint: str) -> Dict[str, Any]:
        pass