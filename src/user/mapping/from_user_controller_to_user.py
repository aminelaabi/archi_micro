from ..types.user import User
from ..types.user_controller_get_current_active_user import UserControllerGetCurrentActiveUserType

def convert(user: UserControllerGetCurrentActiveUserType) -> User:
    return User(
        username=user.username
        ,email=user.email
    )