from datetime import datetime

from fastapi import FastAPI


from pydantic import BaseModel, Field, EmailStr, validator
from uuid import UUID


class UserBase(BaseModel):
    id: UUID
    f_name: str
    l_name: str
    username: str | None = Field(title='username', min_length=3, max_length=30)
    email: EmailStr
    phone: int
    created_at: datetime | None
    updated_at: datetime | None = None
class Category(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
class Comment(UserBase):
    text: str
    count: int
    views: int

class Post(UserBase):
    title: str
    description: str
    slug: str
    content: str
class Tag(UserBase):
    name: str
    description: str


