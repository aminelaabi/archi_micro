from ..types.blurfaces_controller import BlurFacesControllerType
from ..repository.image_upload_file_repository import ImageUploadFileRepository


from ..mapping import from_blurfacescontroller_to_blurfacesusecase
from ..mapping import from_blurfacesrepository_to_blurfacesusecase





class BlurFacesUseCase:
    def __init__(self, image_repository: ImageUploadFileRepository):
        self.image_repository = image_repository

    
    def blur(self, blurfaces_controller: BlurFacesControllerType):
        blurfaces_use_case = from_blurfacescontroller_to_blurfacesusecase.convert(blurfaces_controller)
        blurfaces_repository = self.image_repository.blur(blurfaces_use_case)
        return from_blurfacesrepository_to_blurfacesusecase.convert(blurfaces_repository)
