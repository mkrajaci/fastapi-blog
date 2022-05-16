from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from typing import Optional, List


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = str
    user_image_path = str
    posts = relationship('Post', backpopulates='user')
    # todo: https://pypi.org/project/bcrypt/


class Post(Base):
    __tablename__ = 'posts'

    id: Column(Integer, primary_key=True, index=True)
    user_id: Column(Integer, ForeignKey('users.id'))
    user: relationship('User', backpopulates='posts')
    author_id: str
    title: str
    meta_title: str
    slug: int
    summary: int
    created_at: int
    updated_at: int
    description: str


class PostMeta(Base):
    __tablename__ = 'postmetas'

    id: Column(Integer, primary_key=True, index=True)
    post_id: str


class Tag(Base):
    __tablename__ = 'tags'

    id: Column(Integer, primary_key=True, index=True)
    title: str
    meta_title: str
    slug: str


class Category(Base):
    __tablename__ = 'categories'

    id: Column(Integer, primary_key=True, index=True)
    title: str
    meta_title: str
    slug: str
