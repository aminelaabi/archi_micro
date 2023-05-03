from pydantic import BaseModel


class UserControllerLoginType(BaseModel):
    username: str
    password: str


    class Config:
        orm_mode = True