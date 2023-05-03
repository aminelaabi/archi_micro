from ..types.blurfacesusecasetype import BlurFacesUseCaseType
from ..types.blurfacesrepositorytype import BlurFacesRepositoryType

def convert(blurfaces_repository: BlurFacesRepositoryType) -> BlurFacesUseCaseType:
    return BlurFacesUseCaseType(blurfaces_repository.url
                                , blurfaces_repository.file_content)