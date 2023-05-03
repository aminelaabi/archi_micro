from abc import ABC, abstractmethod
from ...config.config import Config

class RelationalDatabaseABC(ABC):
    @abstractmethod
    def __init__(self, config: Config):
        ...

    @abstractmethod
    def _session_local(self):
        ...

    @abstractmethod
    def _base(self):
        ...