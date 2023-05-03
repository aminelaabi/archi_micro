from .crypto_context_abc import CryptoContextJWTManagerABC
from ...config.config import Config

from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt, JWTError

from ...exceptions.could_not_validate_credentials_exception import CouldNotValidateCredentialsException

class CryptoContextJWTManager(CryptoContextJWTManagerABC):
    def __init__(self, config: Config):
        self.pwd_context = CryptContext(schemes=config.securite_schemes,
                                        deprecated=config.deprecated)
        
        self.access_token_expire_minutes = config.access_token_expire_minutes
        self.secret_key = config.secret_key
        self.algorithm = config.algorithm

        self.password_size = config.password_size

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username: str = payload.get("sub")
        except JWTError:
            raise CouldNotValidateCredentialsException()
        return username

    

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)