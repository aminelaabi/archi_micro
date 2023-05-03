from fastapi import HTTPException
from fastapi import WebSocket

import base64
import cv2
import numpy as np

from ..repository.videofeed_repository import VideoFeedRepository
from ..repository.image_upload_file_repository import ImageUploadFileRepository
from starlette.websockets import WebSocketDisconnect

from loguru import logger



class VideoFeedUseCase:

    def __init__(self
                 ,video_feed_repository: VideoFeedRepository
                 , image_upload_file_repository: ImageUploadFileRepository) -> None:
        self.video_feed_repository = video_feed_repository
        self.image_upload_file_repository =image_upload_file_repository

    async def video(self, data: bytes) -> str:
        frame = base64.b64decode(data)
        array_frame = np.frombuffer(frame, np.uint8)
        blured_frame = self.image_upload_file_repository.blur_model.blur_frame(array_frame)
        frame_res = base64.b64encode(blured_frame)
        return str(frame_res)[2: -1]

    
    async def video_feed(self, websocket: WebSocket):
        await self.video_feed_repository.accept(websocket)
        while True:
            try:
                try:
                    logger.debug("Video feed websocket accepted")
                    frame_bytes = await self.video_feed_repository.receive_bytes(websocket)
                    logger.info(frame_bytes.__len__())
                    frame = np.frombuffer(frame_bytes, dtype=np.uint8).reshape((480, 640, 4))

                    #cv2.imwrite("temp.jpg", f)
                    #image = Image.fromarray(f, 'RGBA')
                    #image.save("tmp2.png", format='PNG')
                    #logger.info("temp.jpg written")
                    #logger.info(f.shape)
                    #logger.info(f)

                    #logger.info(frame)
                    #logger.info(frame.all(0))

                    

                    # write to a temporary file with cv2.imwrite
                    #_, jpeg_frame = cv2.imencode(".jpg", frame)
                    #cv2.imwrite("temp.jpg", jpeg_frame)

                    #img = cv2.imdecode(frame, cv2.IMREAD_UNCHANGED)
                    #cv2.imwrite("temp.jpg", frame)

                    logger.info(frame.shape)
                except WebSocketDisconnect:
                    logger.info("WebSocket disconnected")

                processed_frame = await self.image_upload_file_repository.blur_model.blur_frame(frame)
                _, jpeg_frame = cv2.imencode(".jpg", processed_frame)

                try:
                    await self.video_feed_repository.send_bytes(websocket, jpeg_frame)
                except WebSocketDisconnect:
                    logger.info("WebSocket disconnected")

            except Exception as e:
                logger.exception(e)
                break