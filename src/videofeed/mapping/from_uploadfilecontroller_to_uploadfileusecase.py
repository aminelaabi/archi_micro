from ..types.uploadfilecontrollertype import UploadFileControllerType
from ..types.uploadfileusecasetype import UploadFileUseCaseType

def convert(upload_file_controller_type: UploadFileControllerType) -> UploadFileUseCaseType:
    return UploadFileUseCaseType(upload_file_controller_type.file_content)