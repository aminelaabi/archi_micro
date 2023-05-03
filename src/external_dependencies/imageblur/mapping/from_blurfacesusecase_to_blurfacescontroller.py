from ..types.blurfaces_controller import BlurFacesControllerType
from ..types.blurfacesusecasetype import BlurFacesUseCaseType


def convert(blurfaces_controller: BlurFacesUseCaseType) -> BlurFacesControllerType:
    return BlurFacesControllerType(url=blurfaces_controller.url
                                   , file_content=blurfaces_controller.file_content)