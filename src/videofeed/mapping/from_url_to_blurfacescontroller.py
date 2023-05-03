from ..types.url import Url
from ..types.blurfaces_controller import BlurFacesControllerType


def convert(url: Url) -> BlurFacesControllerType:
    return BlurFacesControllerType(url.url)