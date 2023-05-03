

class BlurFacesControllerType:

    def __init__(self
                 , url: str
                 , file_content: bytes = None) -> None:
        self.url = url
        self.file_content = file_content