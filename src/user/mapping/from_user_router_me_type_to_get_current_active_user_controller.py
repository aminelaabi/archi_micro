from ..types.user_controller_get_current_active_user import UserControllerGetCurrentActiveUserType
from ..types.user_router_me import UserRouterMeType


def convert_one(user_router_me: UserRouterMeType) -> UserControllerGetCurrentActiveUserType:
    return UserControllerGetCurrentActiveUserType(
        username=user_router_me.username,
        email=user_router_me.email,
    )


def convert(user_router_me: UserRouterMeType) -> UserControllerGetCurrentActiveUserType:
    return convert_one(user_router_me)

