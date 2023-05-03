from ..types.user_repository import UserRepositoryType
from ..types.user_raw import UserRawType
from ..types.user_use_case_create_user import UserUseCaseCreateUserType
from ..types.user_controller_get_current_active_user import UserControllerGetCurrentActiveUserType


from ...external_dependencies.database.relational_database import RelationalDatabase
from sqlalchemy import select

import sqlalchemy.exc
import psycopg2.errors

from ...exceptions.user_already_exists_exception import UserAlreadyExistsException
from ...exceptions.email_already_exists_exception import EmailAlreadyExistsException

from ..mapping import from_raw_to_repo
from ..mapping import from_user_use_case_create_user_to_user_repo_password


class UserRepository:

    def __init__(self, database: RelationalDatabase) -> None:
        self.database = database


    async def getUser(self, id: str) -> UserRepositoryType:
        users = self.database.session_local.execute(
            select(UserRawType).where(UserRawType.id == id)
        )
        return from_raw_to_repo.convert(users.scalars().all())
    
    
    async def getUserByUserName(self, username: str) -> UserRepositoryType:
        users = self.database.session_local.execute(
            select(UserRawType).where(UserRawType.username == username)
        )
        return from_raw_to_repo.convert(users.scalars().all())
    
    async def createUser(self, user: UserUseCaseCreateUserType) -> None:
        user_repository_password = from_user_use_case_create_user_to_user_repo_password.convert(user)
        try:
            self.database.session_local.add(UserRawType(
                username=user_repository_password.username
                , hashed_password=user_repository_password.hashed_password
                , email=user_repository_password.email
            ))
            self.database.session_local.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.database.session_local.rollback()
            if not isinstance(e.orig, psycopg2.errors.UniqueViolation):
                raise e
            if e.orig.diag.constraint_name == 'users_username_key':
                raise UserAlreadyExistsException("Username already exists")
            if e.orig.diag.constraint_name == 'users_email_key':
                raise EmailAlreadyExistsException("Email already exists")
        except Exception as e:
            self.database.session_local.rollback()
            raise e