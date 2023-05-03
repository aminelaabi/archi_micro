from ..types.user_repository import UserRepositoryType
from ..types.user_use_case_get_current_user import UserUseCaseGetCurrentUserType

def convert(user: UserRepositoryType) -> UserUseCaseGetCurrentUserType:
    if isinstance(user, list):
        user = user[0]
    return UserUseCaseGetCurrentUserType(
        id=user.id,
        username=user.username,
        email=user.email
    )