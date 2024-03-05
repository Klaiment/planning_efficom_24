from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.users import User
from internal.database import query, execute
router = APIRouter()
# Routes users
@router.get("/users")
async def get_users():
    users = query("SELECT * FROM user")
    return {"users": users}
@router.post("/utilisateur/")
async def create_user(user: User):
    req = f'INSERT INTO user (nom, prenom, email, password, role, entreprise_id) VALUES ("{user.nom}","{user.prenom}","{user.email}","{user.password}","{user.role}","{user.entreprise_id}")'
    execute(req)
    return {"message": "Create user"}

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {"message": "Update user"}
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": "Delete user"}
