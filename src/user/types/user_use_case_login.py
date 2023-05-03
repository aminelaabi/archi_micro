from pydantic import BaseModel

class UserUseCaseLoginType(BaseModel):
    username: str
    email: str
    hashed_password: str

    class Config:
        orm_mode = True
