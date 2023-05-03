from ..types.blurfaces_controller import BlurFacesControllerType
from ..types.blurfacesusecasetype import BlurFacesUseCaseType


def convert(blurfaces_controller: BlurFacesControllerType) -> BlurFacesUseCaseType:
    return BlurFacesUseCaseType(blurfaces_controller.url)