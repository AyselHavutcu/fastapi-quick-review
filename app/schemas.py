from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime




class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserOut(BaseModel):
    id:int | None = None
    email:str | None = None
    created_at:datetime | None = None

    class Config:
        from_attributes = True
 
class UserLogin(BaseModel):
    email:str 
    password:str

class PostBase(BaseModel):
    title:str
    content:str
    published:bool 


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut

    class Config:
        from_attributes = True



class Token(BaseModel):
    access_token: str
    token_type: str
 


class TokenData(BaseModel):
    id: Optional[str] = None
 