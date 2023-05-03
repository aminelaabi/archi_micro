from ..types.uploadfilerepositorytype import UploadFileRepositoryType
from ..types.uploadfileusecasetype import UploadFileUseCaseType

def convert(upload_file_repository_type: UploadFileRepositoryType) -> UploadFileUseCaseType:
    return UploadFileUseCaseType(file_content=None
                                 , url=upload_file_repository_type.url)