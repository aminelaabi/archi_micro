from ..imageblur.controller.imagecontroller import ImageController

from ..imageblur.use_case.image_upload_file_use_case import ImageUploadFileUseCase
from ..imageblur.use_case.blur_faces_use_case import BlurFacesUseCase

from ..imageblur.repository.image_upload_file_repository import ImageUploadFileRepository

from ..routers.imageblur import image_routes

from ..config.external_dependencies import ExternalDependencies
from ..user.controller.user_controller import UserController


def image_injector(external_dependencies: ExternalDependencies
                   , user_controller: UserController):

    simple_storage = external_dependencies.simple_storage
    blur_model = external_dependencies.blur_model

    upload_image_repository = ImageUploadFileRepository(simple_storage
                                                        , blur_model)
    
    upload_image_use_case = ImageUploadFileUseCase(upload_image_repository)
    blur_faces_use_case = BlurFacesUseCase(upload_image_repository)
    
    upload_image_controller = ImageController(upload_image_use_case,
                                              blur_faces_use_case)


    return image_routes(upload_image_controller, user_controller)