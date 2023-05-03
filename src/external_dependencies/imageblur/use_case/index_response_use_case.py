from fastapi.responses import HTMLResponse
from ..repository.htmlresponses_repository import HTMLResponsesRepository
from loguru import logger

class IndexResponseUseCase:
    def __init__(self, response_repository: HTMLResponsesRepository):
        self.response_repository = response_repository

    async def index(self) -> HTMLResponse:
        try:
            return await self.response_repository.index()
        except Exception as e:
            logger.exception(e)
            raise e
        