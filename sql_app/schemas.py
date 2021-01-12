from typing import Optional
from pydantic import BaseModel


class UsersBase(BaseModel):
    username: str
    email: str
    fullname: Optional[str] = None
    telp: Optional[str] = None


class UsersCreate(UsersBase):
    password: str


class Users(UsersBase):
    id: str

    class Config:
        orm_mode = True
