from fastapi import APIRouter, Path, Query
from db.models import User
from typing import List

router = APIRouter()

users = []


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return users


@router.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of user you want to retrieve"),
                   q: str = Query(None, max_length=5)):
    return {"user": users[id], "query": q}
