from fastapi.security import OAuth2PasswordBearer

from ...config.config import Config

class Oauth2PasswordBearer(OAuth2PasswordBearer):

    def __init__(self, config: Config):
        super().__init__(tokenUrl = config.token_url)