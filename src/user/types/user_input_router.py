from pydantic import BaseModel


class UserInputRouterType(BaseModel):
    username: str
    password: str
    email: str


    class Config:
        orm_mode = True