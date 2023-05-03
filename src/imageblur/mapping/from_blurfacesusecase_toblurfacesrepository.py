from ..types.blurfacesusecasetype import BlurFacesUseCaseType
from ..types.blurfacesrepositorytype import BlurFacesRepositoryType

def convert(blurfaces_use_case: BlurFacesUseCaseType) -> BlurFacesRepositoryType:
    return BlurFacesRepositoryType(blurfaces_use_case.url)