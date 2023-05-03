from abc import ABC, abstractmethod
from datetime import timedelta

from ...config.config import Config

class CryptoContextJWTManagerABC(ABC):
    @abstractmethod
    def __init__(self, config: Config):
        ...

    @abstractmethod
    def verify_password(self, plain_password, hashed_password):
        ...

    @abstractmethod
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        ...