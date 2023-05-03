from pydantic import BaseModel


class UserUseCaseGetCurrentUserType(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True