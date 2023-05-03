from ..config.external_dependencies import ExternalDependencies

from ..videofeed.repository.htmlresponses_repository import HTMLResponsesRepository
from ..videofeed.repository.image_upload_file_repository import ImageUploadFileRepository
from ..videofeed.repository.videofeed_repository import VideoFeedRepository

from ..videofeed.use_case.video_feed_use_case import VideoFeedUseCase
from ..videofeed.use_case.index_response_use_case import IndexResponseUseCase

from ..videofeed.controller.videoscontroller import VideoController

from ..routers.videofeed import video_routes



def video_injector(external_dependencies: ExternalDependencies):

    static_directory = external_dependencies.static_directory
    simple_storage = external_dependencies.simple_storage
    blur_model = external_dependencies.blur_model

    upload_image_repository = ImageUploadFileRepository(simple_storage
                                                        , blur_model)
    video_feed_repository = VideoFeedRepository()
    html_responses_repository = HTMLResponsesRepository(static_directory)

    index_response_use_case = IndexResponseUseCase(html_responses_repository)
    video_feed_use_case = VideoFeedUseCase(video_feed_repository
                                           ,upload_image_repository)
    

    video_controller = VideoController(index_response_use_case
                                       ,video_feed_use_case)

    return video_routes(video_controller)
