from ..repository.user_repository import UserRepository
from ...external_dependencies.securite.crypto_context import CryptoContextJWTManager

from ..types.user_controller_password import UserControllerPasswordType

from ..mapping import from_user_controller_password_to_user_use_case_create_user

from ...exceptions.password_too_short_exception import PasswordTooShortException
from ...exceptions.unknown_database_exception import UnknownDatabaseException
from ...exceptions.user_already_exists_exception import UserAlreadyExistsException
from ...exceptions.email_already_exists_exception import EmailAlreadyExistsException

from loguru import logger


class UserUseCaseCreateUser:

    def __init__(self
                 , repository: UserRepository
                 , crypto_context: CryptoContextJWTManager) -> None:

        self.repository = repository
        self.crypto_context = crypto_context

    def _validate_password(self, password: str) -> bool:
        pass_min_length = self.crypto_context.password_size if self.crypto_context.password_size > 8 else 8
        if len(password) < pass_min_length:
            raise PasswordTooShortException(f"Password must be at least {pass_min_length} characters long")
        # Can add other conditions here
        return True


    async def create_user(self, user: UserControllerPasswordType) -> None:
        user_use_case_create_user = from_user_controller_password_to_user_use_case_create_user.convert(user)
        self._validate_password(user_use_case_create_user.password)
        hashed_password = self.crypto_context.get_password_hash(user_use_case_create_user.password)
        user.password = hashed_password
        try:
            await self.repository.createUser(user)
        except UserAlreadyExistsException as e:
            raise e
        except EmailAlreadyExistsException as e:
            raise e
        except Exception as e:
            logger.exception(e)
            raise UnknownDatabaseException("Unknown database error")



