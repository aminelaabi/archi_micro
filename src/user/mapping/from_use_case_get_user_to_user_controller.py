from ..types.user_use_case_get_user import UserUseCaseGetUserType
from ..types.user_controller import UserControllerType
from typing import List


def convert_one(user: UserUseCaseGetUserType) -> UserControllerType:
    return UserControllerType(
        id=user.id,
        name=user.username,
        email=user.email
    )

def convert(users: List[UserUseCaseGetUserType]) -> List[UserControllerType]:
    return [convert_one(user) for user in users]