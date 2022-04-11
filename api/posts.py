from fastapi import APIRouter, Path, Query
from db.models import Post
from typing import List

router = APIRouter()

posts = []


@router.get("/posts", response_model=List[Post])
async def get_posts():
    return posts


@router.post("/posts")
async def create_post(post: Post):
    posts.append(post)
    return posts


@router.get("/posts/{id}")
async def get_post(id: int = Path(..., description="The ID of post you want to retrieve"),
                   q: str = Query(None, max_length=5)):
    return {"post": posts[id], "query": q}
