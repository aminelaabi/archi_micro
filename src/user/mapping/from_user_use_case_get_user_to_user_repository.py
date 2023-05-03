from ..types.user_use_case_get_user import UserUseCaseGetUserType
from ..types.user_repository import UserRepositoryType

def convert_one(user: UserUseCaseGetUserType) -> UserRepositoryType:
    return UserRepositoryType(
        username=user.username,
        email=user.email
    )

def convert(user: UserUseCaseGetUserType) -> UserRepositoryType:
    return convert_one(user)