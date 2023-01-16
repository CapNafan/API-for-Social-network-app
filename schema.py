from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str

    # class Config:
    #     orm_mode = True
