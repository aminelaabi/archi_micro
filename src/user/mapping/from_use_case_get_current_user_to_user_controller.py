from ..types.user_use_case_get_current_user import UserUseCaseGetCurrentUserType
from ..types.user_controller_get_current_active_user import UserControllerGetCurrentActiveUserType


def convert(user: UserUseCaseGetCurrentUserType) -> UserControllerGetCurrentActiveUserType:
    return UserControllerGetCurrentActiveUserType(
        username=user.username
        ,email=user.email
    )