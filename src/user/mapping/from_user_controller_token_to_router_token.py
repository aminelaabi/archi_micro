from ..types.user_token_router import Token
from ..types.user_controller_token import UserControllerTokenType


def convert_one(user_controller_token: UserControllerTokenType) -> Token:
    return Token(
        access_token = user_controller_token.access_token,
        token_type = user_controller_token.token_type
    )

def convert(user_controller_token: UserControllerTokenType) -> Token:
    return convert_one(user_controller_token)