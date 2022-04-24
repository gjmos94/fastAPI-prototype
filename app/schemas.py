from pydantic import BaseModel, EmailStr # schema library
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # add value so it defaults if user does not provide it


class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True

class UpdatePost(BaseModel):
    title: str
    content: str
    published: bool

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class  UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:   # used to convert SQLalchemy model into a pydantic model
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:   # used to convert SQLalchemy model into a pydantic model
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)