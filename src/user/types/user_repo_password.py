from pydantic import BaseModel


class UserRepositoryPasswordType(BaseModel):
    username: str
    hashed_password: str
    email: str


    class Config:
        orm_mode = True