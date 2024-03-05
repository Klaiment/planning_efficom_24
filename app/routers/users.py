from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.users import User

router= APIRouter()
# Routes users
@router.get("/users")
async def get_users():
    return {"message": "Get users"}
@router.post("/utilisateur/")
async def create_user(user: User):

    return {"message": "Create user"}
@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {"message": "Update user"}
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": "Delete user"}