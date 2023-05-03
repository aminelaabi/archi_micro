from abc import ABC, abstractmethod


class SimpleStorageABC(ABC):
    @abstractmethod
    def upload(self, file_content: bytes):
        ...

    @abstractmethod
    def download(self, url: str, path: str):
        ...
