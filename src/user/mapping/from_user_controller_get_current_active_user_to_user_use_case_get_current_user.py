from ..types.user_controller_get_current_active_user import UserControllerGetCurrentActiveUserType
from ..types.user_use_case_get_current_user import UserUseCaseGetCurrentUserType


def convert_one(user: UserControllerGetCurrentActiveUserType) -> UserUseCaseGetCurrentUserType:
    return UserUseCaseGetCurrentUserType(
        username=user.username,
        email=user.email
    )

def convert(user: UserControllerGetCurrentActiveUserType) -> UserUseCaseGetCurrentUserType:
    return convert_one(user)