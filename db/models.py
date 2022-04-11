from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    password_hash: str
    user_image_path: str


class Post(BaseModel):
    id: str
    author_id: str
    title: str
    meta_title: str
    slug: int
    summary: int
    created_at: int
    updated_at: int
    description: str


class PostMeta(BaseModel):
    id: str
    post_id: str


class Tag(BaseModel):
    id: str
    title: str
    meta_title: str
    slug: str


class Category(BaseModel):
    id: str
    title: str
    meta_title: str
    slug: str
