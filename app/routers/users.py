from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.users import User
from internal.database import query
router = APIRouter()
# Routes users
@router.get("/users")
async def get_users():
    users = query("SELECT * FROM user")
    return {"users": users}
@router.post("/utilisateur/")
async def create_user(user: User):
    req = "INSERT INTO user (nom, prenom, email, password, role, entreprise_id) VALUES (:nom, :prenom, :email, :password, :role, :entreprise_id)"

    query()
    return {"message": "Utilisateur créé avec succès."}
@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {"message": "Update user"}
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": "Delete user"}
