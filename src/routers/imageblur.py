from ..imageblur.controller.imagecontroller import ImageController
from ..user.controller.user_controller import UserController

from ..imageblur.types.url import Url



from loguru import logger
from fastapi import Depends



def image_routes(image_controller: ImageController
                 , user_controller: UserController):


    from fastapi import APIRouter, UploadFile

    router = APIRouter(
        prefix="/image",
    )




    @router.post("/upload", tags=["image"])
    async def upload_image(file: UploadFile
                           , current_user = Depends(user_controller.get_current_active_user)):
        return image_controller.upload_image(file)
    

    @router.get("/blurfaces", tags=["image"])
    async def download_image(url: str
                             , save_cloud: bool = False
                             , current_user = Depends(user_controller.get_current_active_user)):
        return image_controller.blue_faces(Url(url=url)
                                           , save_cloud=save_cloud)

    



    return router