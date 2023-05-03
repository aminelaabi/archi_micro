from ..types.user_use_case_create_user import UserUseCaseCreateUserType
from ..types.user_repo_password import UserRepositoryPasswordType


def convert_one(user: UserUseCaseCreateUserType) -> UserRepositoryPasswordType:
    return UserRepositoryPasswordType(
        username=user.username,
        hashed_password=user.password,
        email=user.email
    )


def convert(user: UserUseCaseCreateUserType) -> UserRepositoryPasswordType:
    return convert_one(user)