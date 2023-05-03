from fastapi import WebSocket



class VideoFeedRepository:

    async def accept(self, websocket: WebSocket):
        await websocket.accept()

    async def receive_bytes(self, websocket: WebSocket):
        return await websocket.receive_bytes()
    
    async def send_bytes(self, websocket: WebSocket, jpeg_frame: bytes):
        await websocket.send_bytes(jpeg_frame.tobytes())

    async def receive_text(self, websocket: WebSocket):
        return await websocket.receive_text()