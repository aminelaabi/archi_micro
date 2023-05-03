from ..use_case.index_response_use_case import IndexResponseUseCase
from ..use_case.video_feed_use_case import VideoFeedUseCase

from fastapi.responses import HTMLResponse
from fastapi import WebSocket

from fastapi import HTTPException

class VideoController:

    def __init__(self
                 ,index_response_use_case: IndexResponseUseCase
                 ,video_feed_use_case: VideoFeedUseCase) -> None:
        self.index_response_use_case = index_response_use_case
        self.video_feed_use_case = video_feed_use_case


    async def index(self)-> HTMLResponse:
        try:
            return await self.index_response_use_case.index()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
        
    async def video(self, data: bytes) -> str:
        try:
            return await self.video_feed_use_case.video(data)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")