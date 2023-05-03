from pydantic import BaseModel


class UserUseCaseLoginTokenType(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True