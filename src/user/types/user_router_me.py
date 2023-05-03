from pydantic import BaseModel


class UserRouterMeType(BaseModel):
    username: str
    email: str


    class Config:
        orm_mode = True