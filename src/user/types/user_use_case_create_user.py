from pydantic import BaseModel


class UserUseCaseCreateUserType(BaseModel):
    username: str
    password: str
    email: str


    class Config:
        orm_mode = True