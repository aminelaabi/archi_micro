from fastapi import FastAPI

from src.config.config import Config
from src.config.external_dependencies import ExternalDependencies

from src.external_dependencies.database.relational_database import RelationalDatabase
from src.external_dependencies.securite.crypto_context import CryptoContextJWTManager
from src.soluce_contournement import oauth2_scheme
from src.external_dependencies.stockage.static_directory import StaticDirectory
from src.external_dependencies.stockage.simple_storage import SimpleStorage
from src.external_dependencies.blurmodel.blurmodel import BlurModel

from src.routers.all_routers import get_all_routes


app = FastAPI()

external_dependencies = ExternalDependencies(
    database = RelationalDatabase(config = Config)
    ,crypto_context = CryptoContextJWTManager(config = Config)
    ,oauth2_scheme = oauth2_scheme
    ,static_directory = StaticDirectory(Config.INDEX_HTML)
    ,simple_storage = SimpleStorage()
    ,blur_model = BlurModel(cascade_file_path=Config.CASCADE)
)

for router in get_all_routes(external_dependencies):
    try:
        app.include_router(router)
    except AttributeError as e:
        app.mount("/", router)
