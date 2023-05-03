from pydantic import BaseModel


class UserControllerPasswordType(BaseModel):
    username: str
    password: str
    email: str


    class Config:
        orm_mode = True