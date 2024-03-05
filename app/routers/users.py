from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.users import User
from internal.database import query, execute
from hashlib import sha256
from internal.auth import get_decoded_token


def password_hash(password: str):
    return sha256(password.encode()).hexdigest()

router = APIRouter()
# Routes users
@router.get("/users")
async def get_users():
    users = query("SELECT * FROM user")
    return {"users": users}
@router.post("/utilisateur/")
async def create_user(user: User):
    password = password_hash(user.password)
    req = f'INSERT INTO user (nom, prenom, email, password, role, entreprise_id) VALUES ("{user.nom}","{user.prenom}","{user.email}","{password}","{user.role}","{user.entreprise_id}")'
    execute(req)
    return {"message": "Create user"}

@router.get("/users/{user_id}")
async def get_user(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int):
    user = query(f"SELECT * FROM user WHERE id={user_id}")
    if len(user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
@router.put("/users/{user_id}")
async def update_user(user: User):

    return {"message": "Update user"}
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": "Delete user"}
