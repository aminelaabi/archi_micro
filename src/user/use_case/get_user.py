from ..types.user_use_case_get_user import UserUseCaseGetUserType

from ..repository.user_repository import UserRepository
from ..mapping import from_repo_to_use_case_get_user

from ...exceptions.user_not_found_exception import UserNotFoundException



class UserUseCaseGetUser:

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository


    async def getUser(self, username: str) -> UserUseCaseGetUserType:
        user_repository = await self.repository.getUser(username)
        user_use_case = from_repo_to_use_case_get_user.convert(user_repository)
        if user_use_case:
            return user_use_case
        else:
            raise UserNotFoundException("User Not Found")