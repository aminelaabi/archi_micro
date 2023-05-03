from fastapi import UploadFile
from ..types.uploadfilecontrollertype import UploadFileControllerType


def convert(uploadfile: UploadFile) -> UploadFileControllerType:
    return UploadFileControllerType(uploadfile.file.read())