from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostSchema(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str


class UserOutSchema(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True