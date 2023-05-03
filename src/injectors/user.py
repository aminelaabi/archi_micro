from ..config.external_dependencies import ExternalDependencies

from ..user.repository.user_repository import UserRepository

from ..user.use_case.get_user import UserUseCaseGetUser
from ..user.use_case.login_user import UserUseCaseLogin
from ..user.use_case.create_user import UserUseCaseCreateUser
from ..user.use_case.get_current_user import UserUseCaseGetCurrentUser

from ..user.controller.user_controller import UserController

from ..routers.user import user_routes




def user_injector(ext_dependencies: ExternalDependencies):
    
    user_repository = UserRepository(ext_dependencies.database)
    user_use_case_get_user = UserUseCaseGetUser(user_repository)
    user_use_case_login = UserUseCaseLogin(user_repository, ext_dependencies.crypto_context)
    user_use_case_create_user = UserUseCaseCreateUser(user_repository, ext_dependencies.crypto_context)
    user_use_case_get_current_user = UserUseCaseGetCurrentUser(user_repository
                                                               , ext_dependencies.crypto_context
                                                               , ext_dependencies.oauth2_scheme)


    
    user_controller = UserController(user_use_case_get_user
                                     , user_use_case_login
                                     , user_use_case_create_user
                                     , user_use_case_get_current_user)
    
    return user_routes(user_controller), user_controller