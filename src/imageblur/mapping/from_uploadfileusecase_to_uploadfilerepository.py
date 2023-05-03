from ..types.uploadfileusecasetype import UploadFileUseCaseType
from ..types.uploadfilerepositorytype import UploadFileRepositoryType

def convert(uploadfile_use_case: UploadFileUseCaseType) -> UploadFileRepositoryType:
    return UploadFileRepositoryType(uploadfile_use_case.file_content)