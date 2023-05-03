from .static_directory_abc import StaticDirectoryABC

class StaticDirectory(StaticDirectoryABC):

    def __init__(self, path: str):
        self.path = path

    def get_path(self) -> str:
        return self.path