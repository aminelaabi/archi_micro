from ..user.controller.user_controller import UserController
from ..user.types.user_token_router import Token
from ..user.types.user_input_router import UserInputRouterType
from ..user.types.user import User
from ..user.types.user_controller_get_current_active_user import UserControllerGetCurrentActiveUserType

from ..user.mapping import from_user_controller_to_user
from ..user.mapping import from_user_controller_token_to_router_token

from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import Depends


def user_routes(user_controller: UserController):
    
    from fastapi import APIRouter

    router = APIRouter(
        prefix="/user",
        tags=["user"],
        dependencies=[],
        responses={404: {"description": "Not found"}}
    )


    @router.get("/{id}")
    async def get_user(id: int):
        user = await user_controller.getUser(id)
        return user
    
    @router.post("/login", response_model=Token)
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ):
        user_controller_token = await user_controller.login(form_data)
        return from_user_controller_token_to_router_token.convert(user_controller_token)
    

    @router.put("/create", status_code=201)
    async def create_user(user: UserInputRouterType):
        await user_controller.create_user(user_input_router=user)
        return user
    
    @router.post("/me", response_model=User)
    async def read_users_me(
        current_user: UserControllerGetCurrentActiveUserType = Depends(user_controller.get_current_active_user)
    ):
        return from_user_controller_to_user.convert(current_user)
        
        

    return router
