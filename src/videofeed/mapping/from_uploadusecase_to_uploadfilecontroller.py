from ..types.uploadfileusecasetype import UploadFileUseCaseType
from ..types.uploadfilecontrollertype import UploadFileControllerType

def convert(upload_file_controller_type: UploadFileControllerType) -> UploadFileUseCaseType:
    return UploadFileUseCaseType(
        file_content=None,
        url=upload_file_controller_type.url
    )