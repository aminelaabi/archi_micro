from pydantic import BaseModel

class UserRepositoryType(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str

    class Config:
        orm_mode = True

