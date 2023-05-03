from ..repository.image_upload_file_repository import ImageUploadFileRepository
from ..types.uploadfilecontrollertype import UploadFileControllerType
from ..types.uploadfileusecasetype import UploadFileUseCaseType

from ..mapping import from_uploadfilecontroller_to_uploadfileusecase
from ..mapping import from_uploadfilerepository_to_uploadfileusecase


from ...exceptions.uploadfileerror import UploadFileError
from loguru import logger


class ImageUploadFileUseCase:
    def __init__(self
                 , image_upload_file_repository: ImageUploadFileRepository):
        self.image_upload_file_repository = image_upload_file_repository

    def upload(self, upload_file_controller_type: UploadFileControllerType) -> UploadFileUseCaseType:
        upload_file_use_case_type = from_uploadfilecontroller_to_uploadfileusecase.convert(upload_file_controller_type)
        try:
            upload_file_repository_type = self.image_upload_file_repository.upload(upload_file_use_case_type)
        except Exception as e:
            logger.exeption("An error occured while uploading the file")
            # Une amélioration et d'énumérer les types d'erreurs
            raise UploadFileError("An error occured while uploading the file")
        return from_uploadfilerepository_to_uploadfileusecase.convert(upload_file_repository_type)
