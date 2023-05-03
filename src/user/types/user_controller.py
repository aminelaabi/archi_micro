from pydantic import BaseModel

class UserControllerType(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

