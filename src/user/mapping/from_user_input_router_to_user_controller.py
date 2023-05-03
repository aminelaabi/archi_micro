from ..types.user_input_router import UserInputRouterType
from ..types.user_controller_password import UserControllerPasswordType


def convert_one(user_input_router: UserInputRouterType) -> UserControllerPasswordType:
    return UserControllerPasswordType(
        username=user_input_router.username,
        password=user_input_router.password,
        email=user_input_router.email
    )


def convert(user_input_router: UserInputRouterType) -> UserControllerPasswordType:
    return convert_one(user_input_router)