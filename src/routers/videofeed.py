from ..videofeed.controller.videoscontroller import VideoController



def video_routes(video_controller: VideoController):


    import socketio
    from loguru import logger


    sio = socketio.AsyncServer(async_mode='asgi')
    app_sio = socketio.ASGIApp(sio, static_files={
        '/': './public/index.html',
        '/index.js': './public/index.js'
    })

    @sio.event
    async def connect(sid, environ):
        logger.info(f'Client {sid} connected')

    @sio.event
    async def disconnect(sid):
        logger.info(f'Client {sid} disconnected')


    @sio.event
    async def video(sid, data: bytes):
        await sio.emit('video', await video_controller.video(data["video"]), to=sid)
    

    return app_sio