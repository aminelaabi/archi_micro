from ..types.user_controller_token import UserControllerTokenType
from ..types.user_use_case_login_token import UserUseCaseLoginTokenType
from typing import List


def convert_one(token: UserUseCaseLoginTokenType) -> UserControllerTokenType:
    return UserControllerTokenType(
        token_type=token.token_type
        , access_token=token.access_token
    )

def convert(token :UserUseCaseLoginTokenType) -> List[UserControllerTokenType]:
    return convert_one(token)