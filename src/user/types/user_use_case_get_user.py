from pydantic import BaseModel

class UserUseCaseGetUserType(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str

    class Config:
        orm_mode = True

