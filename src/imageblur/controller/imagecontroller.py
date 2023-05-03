from ..use_case.image_upload_file_use_case import ImageUploadFileUseCase

from fastapi import UploadFile
from fastapi.responses import Response

from ..types.url import Url
from ..types.uploadfilecontrollertype import UploadFileControllerType
from ..use_case.blur_faces_use_case import BlurFacesUseCase


from ..mapping import from_uploadfile_to_uploadfilecontroller
from ..mapping import from_uploadusecase_to_uploadfilecontroller
from ..mapping import from_url_to_blurfacescontroller
from ..mapping import from_blurfacesusecase_to_blurfacescontroller

from loguru import logger

from fastapi import HTTPException



class ImageController:


    def __init__(self,
                 image_upload_file_use_case: ImageUploadFileUseCase,
                 blur_faces_use_case: BlurFacesUseCase) -> None:
        self.blur_faces_use_case = blur_faces_use_case
        self.image_upload_file_use_case = image_upload_file_use_case



    def upload_image(self, file: UploadFile) -> dict:
        uploadfile_controller = from_uploadfile_to_uploadfilecontroller.convert(file)
        try:
            uploadfile_use_case = self.image_upload_file_use_case.upload(uploadfile_controller)
        except Exception as e:
            logger.exception("An error occured while uploading the file")
            return HTTPException(status_code=500, detail="Internal server error")
        uploadfile_controller = from_uploadusecase_to_uploadfilecontroller.convert(uploadfile_use_case)
        return {"message": "Image uploaded successfully",
                "url": uploadfile_controller.url}
    

    def blue_faces(self, url: Url, save_cloud: bool) -> None:
        blurfaces_controller = from_url_to_blurfacescontroller.convert(url)
        try:
            blurfaces_usecase = self.blur_faces_use_case.blur(blurfaces_controller)
        except Exception as e:
            logger.error(e, exc_info=True)
            return HTTPException(status_code=500, detail="Internal server error")
        blurfaces_controller = from_blurfacesusecase_to_blurfacescontroller.convert(blurfaces_usecase)
        if save_cloud:
            try:
                uploadfile_use_case = self.image_upload_file_use_case.upload(UploadFileControllerType(
                    file_content=blurfaces_controller.file_content
                ))
            except Exception as e:
                logger.exception("An error occured bluuring the face")
                return HTTPException(status_code=500, detail="Internal server error")
            uploadfile_controller = from_uploadusecase_to_uploadfilecontroller.convert(uploadfile_use_case)
            return {"message": "Image uploaded successfully",
                    "url": uploadfile_controller.url}
        else:
            media_type = f"image/{url.url.split('_')[-1]}"
            return Response(content=blurfaces_controller.file_content, media_type=media_type)
            

        
        


