class UploadFileRepositoryType:

    def __init__(self, file_content: bytes, url: str = None) -> None:
        self.file_content = file_content
        self.url = url