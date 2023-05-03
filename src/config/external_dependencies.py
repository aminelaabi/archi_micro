from ..external_dependencies.stockage.static_directory import StaticDirectory
from ..external_dependencies.stockage.simple_storage import SimpleStorage
from ..external_dependencies.blurmodel.blurmodel import BlurModel
from ..external_dependencies.database.relational_database import RelationalDatabase
from ..external_dependencies.securite.crypto_context import CryptoContextJWTManager
from ..external_dependencies.securite.oauth_password_bearer import Oauth2PasswordBearer




class ExternalDependencies:

    def __init__(self
                 , static_directory: StaticDirectory
                 , simple_storage: SimpleStorage
                 , blur_model: BlurModel, database: RelationalDatabase
                 , crypto_context: CryptoContextJWTManager
                 , oauth2_scheme: Oauth2PasswordBearer) -> None:
        
        self.database = database
        self.crypto_context = crypto_context
        self.oauth2_scheme = oauth2_scheme
        self.static_directory = static_directory
        self.simple_storage = simple_storage
        self.blur_model = blur_model
