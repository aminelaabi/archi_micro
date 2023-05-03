from .imageblur import image_routes
from .videofeed import video_routes

from ..injectors.image_injector import image_injector
from ..injectors.video_injector import video_injector
from ..injectors.user import user_injector

from ..config.external_dependencies import ExternalDependencies

def get_all_routes(ext_dependencies: ExternalDependencies):

    user_route, user_controller = user_injector(ext_dependencies)
    image_route = image_injector(ext_dependencies, user_controller)
    video_route = video_injector(ext_dependencies)

    return [user_route,
            image_route,
            video_route]
