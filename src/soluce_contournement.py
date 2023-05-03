from src.external_dependencies.securite.oauth_password_bearer import Oauth2PasswordBearer
from src.config.config import Config



oauth2_scheme = Oauth2PasswordBearer(config = Config)