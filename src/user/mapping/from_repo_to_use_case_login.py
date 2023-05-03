from ..types.user_repository import UserRepositoryType
from ..types.user_use_case_login import UserUseCaseLoginType
from typing import List


def convert_one(user: UserRepositoryType) -> UserUseCaseLoginType:
    if isinstance(user, list):
        if len(user) == 0:
            return None
        else:
            user = user[0]
    return UserUseCaseLoginType(
        id=user.id,
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password
    )


def convert(user: UserRepositoryType) -> List[UserUseCaseLoginType]:
    return convert_one(user)