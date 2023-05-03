from ..types.user_controller_password import UserControllerPasswordType
from ..types.user_use_case_create_user import UserUseCaseCreateUserType


def convert_one(user: UserControllerPasswordType) -> UserUseCaseCreateUserType:
    return UserUseCaseCreateUserType(
        username=user.username,
        password=user.password,
        email=user.email
    )


def convert(user: UserControllerPasswordType) -> UserUseCaseCreateUserType:
    return convert_one(user)