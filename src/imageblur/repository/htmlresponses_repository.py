from fastapi.responses import HTMLResponse

from ..stockage.static_directory import StaticDirectory



class HTMLResponsesRepository:
    def __init__(self, static_directory: StaticDirectory):
        self.static_directory = static_directory

    async def index(self):
        with open(self.static_directory.get_path()) as f:
            html = f.read()
            return HTMLResponse(content=html
                                , status_code=200)