from ..types.user_repository import UserRepositoryType
from ..types.user_use_case_get_user import UserUseCaseGetUserType
from typing import List


def convert_one(user: UserRepositoryType) -> UserUseCaseGetUserType:
    return UserUseCaseGetUserType(
        id=user.id,
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password
    )


def convert(users: List[UserRepositoryType]) -> List[UserUseCaseGetUserType]:
    return [convert_one(user) for user in users]