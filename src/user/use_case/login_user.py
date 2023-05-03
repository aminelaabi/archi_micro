from ..types.user_use_case_login import UserUseCaseLoginType
from ..types.user_use_case_login_token import UserUseCaseLoginTokenType
from ...external_dependencies.securite.crypto_context import CryptoContextJWTManager

from ..repository.user_repository import UserRepository
from ..mapping import from_repo_to_use_case_login

from ...exceptions.user_not_found_exception import UserNotFoundException
from ...exceptions.incorrect_password_exception import IncorrectPasswordException

from datetime import timedelta


class UserUseCaseLogin:

    def __init__(self
                 , repository: UserRepository
                 , crypto_context: CryptoContextJWTManager) -> None:

        self.repository = repository
        self.crypto_context = crypto_context


    async def checkPasswordForUser(self, username: str, password: str) -> UserUseCaseLoginType:
        user_repository = await self.repository.getUserByUserName(username)
        user_use_case_check_password_for_user = from_repo_to_use_case_login.convert(user_repository)

        if user_use_case_check_password_for_user is not None:
            if self.crypto_context.verify_password(password, user_use_case_check_password_for_user.hashed_password):
                return user_use_case_check_password_for_user
            else:
                raise IncorrectPasswordException("Incorrect Password")
            
        else:
            raise UserNotFoundException("User Not Found")
    

    

    async def generateTokenForUser(self, user: UserUseCaseLoginType) -> str:
        access_token_expires = timedelta(self.crypto_context.access_token_expire_minutes)
        access_token = self.crypto_context.create_access_token(
            data={"sub": user.username}
            , expires_delta=access_token_expires
        )
        return UserUseCaseLoginTokenType(
            access_token=access_token
            , token_type="bearer"
        )
        

    