from pydantic import BaseModel

class UserControllerGetUserType(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True