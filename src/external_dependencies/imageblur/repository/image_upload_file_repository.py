from ...stockage.simple_storage import SimpleStorage
from ...blurmodel.blurmodel import BlurModel

from ..types.uploadfileusecasetype import UploadFileUseCaseType
from ..types.uploadfilerepositorytype import UploadFileRepositoryType

from ..types.blurfacesusecasetype import BlurFacesUseCaseType
from ..types.blurfacesrepositorytype import BlurFacesRepositoryType

from ..mapping import from_uploadfileusecase_to_uploadfilerepository
from ..mapping import from_blurfacesusecase_toblurfacesrepository

class ImageUploadFileRepository:
    def __init__(self
                 , simple_storage: SimpleStorage
                 , blur_model: BlurModel):
        self.simple_storage = simple_storage
        self.blur_model = blur_model

    def upload(self, uploadfile_use_case: UploadFileUseCaseType) -> UploadFileRepositoryType:
        uploadfile_repositroy = from_uploadfileusecase_to_uploadfilerepository.convert(uploadfile_use_case)
        url = self.simple_storage.upload(uploadfile_repositroy.file_content)
        uploadfile_repositroy.url = url
        return uploadfile_repositroy
    
    def blur(self, blurfaces_use_case: BlurFacesUseCaseType) -> BlurFacesRepositoryType:
        blurfaces_repository = from_blurfacesusecase_toblurfacesrepository.convert(blurfaces_use_case)
        img_content = self.simple_storage.download(blurfaces_repository.url)
        blurred_img = self.blur_model.blur(img_content)
        blurfaces_repository.file_content = blurred_img
        return blurfaces_repository
         


        