from abc import ABC, abstractmethod


class BlurModelABC(ABC):

    @abstractmethod
    def blur(self, img_content: bytes) -> bytes:
        ...
