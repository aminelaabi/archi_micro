from ..types.user_repository import UserRepositoryType
from ..types.user_raw import UserRawType
from typing import List


def convert_one(user: UserRawType) -> UserRepositoryType:
    return UserRepositoryType(
        id=user.id,
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password
    )

def convert(users: List[UserRawType]) -> List[UserRepositoryType]:
    return [convert_one(user) for user in users]