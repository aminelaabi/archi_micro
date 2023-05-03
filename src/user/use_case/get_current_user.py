from ...external_dependencies.securite.crypto_context import CryptoContextJWTManager
from ...external_dependencies.securite.oauth_password_bearer import Oauth2PasswordBearer

from ..repository.user_repository import UserRepository

from ..mapping import from_userrepo_to_get_current_user

from ...exceptions.could_not_validate_credentials_exception import CouldNotValidateCredentialsException


from loguru import logger


class UserUseCaseGetCurrentUser:

    def __init__(self
                 , repository: UserRepository
                 , crypto_context: CryptoContextJWTManager
                 , oauth2_scheme: Oauth2PasswordBearer) -> None:

        self.repository = repository
        self.crypto_context = crypto_context
        self.oauth2_scheme = oauth2_scheme



    async def get_current_active_user(self, token: str):
        username = self.crypto_context.decode_token(token)
        if username is None:
            raise CouldNotValidateCredentialsException("User not authentificaded")
        else:
            user_repository = await self.repository.getUserByUserName(username)
            if user_repository is None:
                raise CouldNotValidateCredentialsException("User don't exist")
            return from_userrepo_to_get_current_user.convert(user_repository)  
