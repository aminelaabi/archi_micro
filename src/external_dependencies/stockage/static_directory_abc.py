from abc import ABC, abstractmethod

class StaticDirectoryABC(ABC):

    @abstractmethod
    def get_path(self) -> str:
        ...