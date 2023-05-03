from ..types.user_controller_login import UserControllerLoginType
from fastapi.security import OAuth2PasswordRequestForm

def convert_one(form_data: OAuth2PasswordRequestForm) -> UserControllerLoginType:
    return UserControllerLoginType(
        username = form_data.username,
        password = form_data.password
    )

def convert(form_data: OAuth2PasswordRequestForm) -> UserControllerLoginType:
    return convert_one(form_data)