from ..types.user_controller import UserControllerType
from ..types.user_controller_token import UserControllerTokenType
from ..types.user_use_case_login import UserUseCaseLoginType
from ..types.user_input_router import UserInputRouterType
from ..types.user_controller_get_current_active_user import UserControllerGetCurrentActiveUserType

from ..use_case.get_user import UserUseCaseGetUser
from ..use_case.login_user import UserUseCaseLogin
from ..use_case.create_user import UserUseCaseCreateUser
from ..use_case.get_current_user import UserUseCaseGetCurrentUser

from ..mapping import from_use_case_get_user_to_user_controller
from ..mapping import from_use_case_login_token_to_controller_token
from ..mapping import from_form_data_to_id_pass
from ..mapping import from_user_input_router_to_user_controller
from ..mapping import from_use_case_get_current_user_to_user_controller

from fastapi import HTTPException
from ...exceptions.user_not_found_exception import UserNotFoundException
from ...exceptions.incorrect_password_exception import IncorrectPasswordException
from ...exceptions.user_already_exists_exception import UserAlreadyExistsException
from ...exceptions.email_already_exists_exception import EmailAlreadyExistsException
from ...exceptions.password_too_short_exception import PasswordTooShortException
from ...exceptions.could_not_validate_credentials_exception import CouldNotValidateCredentialsException

from ...soluce_contournement import oauth2_scheme

from fastapi import Depends

from loguru import logger



class UserController:

    def __init__(self
                 , use_case_get_user: UserUseCaseGetUser
                 , use_case_login: UserUseCaseLogin
                 , user_case_create_user: UserUseCaseCreateUser
                 , user_use_case_get_current_user: UserUseCaseGetCurrentUser) -> None:
        
        self.use_case_get_user = use_case_get_user
        self.use_case_login= use_case_login
        self.user_case_create_user = user_case_create_user
        self.user_use_case_get_current_user = user_use_case_get_current_user





    async def getUser(self, id: str) -> UserControllerType:
        try:
            user_use_case = await self.use_case_get_user.getUser(id)
        except UserNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
        user_use_controller = from_use_case_get_user_to_user_controller.convert(user_use_case)
        return user_use_controller
    

    async def _checkPasswordForUser(self, username: str, password: str) -> UserUseCaseLoginType:
        try:
            user_use_case = await self.use_case_login.checkPasswordForUser(username, password)
        except UserNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except IncorrectPasswordException as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
        return user_use_case
    
    async def generateTokenForUser(self, username: str, password: str) -> UserControllerTokenType:
        user_use_case_login = await self._checkPasswordForUser(username, password)
        try:
            token = await self.use_case_login.generateTokenForUser(user_use_case_login)

        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        user_use_case_login_token = from_use_case_login_token_to_controller_token.convert(token)
        return user_use_case_login_token
    
    async def login(self, form_data):
        user_controller_login = from_form_data_to_id_pass.convert(form_data)
        token = await self.generateTokenForUser(
            username=user_controller_login.username
            , password=user_controller_login.password)
        return token
    

    async def create_user(self, user_input_router: UserInputRouterType):
        user_controller_password = from_user_input_router_to_user_controller.convert(user_input_router)
        try:
            await self.user_case_create_user.create_user(user_controller_password)
        except (EmailAlreadyExistsException, UserAlreadyExistsException) as e:
            raise HTTPException(status_code=409, detail=str(e))
        except PasswordTooShortException as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
    

    async def get_current_active_user(self, token:str = Depends(oauth2_scheme)) -> UserControllerGetCurrentActiveUserType:
        try:
            user_uc = await self.user_use_case_get_current_user.get_current_active_user(token)
            return from_use_case_get_current_user_to_user_controller.convert(user_uc) 
        except CouldNotValidateCredentialsException as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
