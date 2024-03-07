from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.users import User
from internal.database import query, execute
from hashlib import sha256
from internal.auth import get_decoded_token
from cryptography.fernet import Fernet

def password_hash(password: str):
    return sha256(password.encode()).hexdigest()

router = APIRouter()
# Routes users
@router.get("/users")
async def get_users(connected_user_email: Annotated[str, Depends(get_decoded_token)]):
    users = query("SELECT * FROM user")
    return {"users": users}
@router.post("/utilisateur/")
async def create_user(user: User):
    check_user = query(f"SELECT * FROM user")
    for unitUser in check_user:
        chipher_check = Fernet(unitUser[7])
        email_dechiffre = chipher_check.decrypt(unitUser[3]).decode()
        if email_dechiffre == user.email:
            raise HTTPException(status_code=409, detail="User already exists")
    password = password_hash(user.password)
    secret = Fernet.generate_key()
    cipher_suite = Fernet(secret)
    nom = cipher_suite.encrypt(user.nom.encode())
    prenom = cipher_suite.encrypt(user.prenom.encode())
    email = cipher_suite.encrypt(user.email.encode())
    nom_hex = nom.decode()
    prenom_hex = prenom.decode()
    email_hex = email.decode()
    req = f'INSERT INTO user (nom, prenom, email, password, role, entreprise_id, secret) VALUES ("{nom_hex}","{prenom_hex}","{email_hex}","{password}","{user.role}","{user.entreprise_id}", "{secret.decode()}")'
    execute(req)
    return {"message": "Create user"}


@router.get("/users/{user_id}")
async def get_user(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int):
    check_user = query(f"SELECT * FROM user WHERE id={user_id}")
    if len(check_user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    crypt_user = check_user[0]
    chipher_check = Fernet(crypt_user[7])
    nom_dechiffre = chipher_check.decrypt(crypt_user[1]).decode()
    prenom_dechiffre = chipher_check.decrypt(crypt_user[2]).decode()
    email_dechiffre = chipher_check.decrypt(crypt_user[3]).decode()

    return {"user": {"nom": nom_dechiffre, "prenom": prenom_dechiffre, "email": email_dechiffre}}


@router.put("/users/{user_id}")
async def update_user(connected_user_email: Annotated[str, Depends(get_decoded_token)], user: User):
    check_user = query(f"SELECT * FROM user WHERE id={user.id}")
    if len(check_user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    check_entreprise = query(f"SELECT * FROM entreprise WHERE id={user.entreprise_id}")
    if len(check_entreprise) == 0:
        raise HTTPException(status_code=404, detail="Entreprise not found")
    req = f'UPDATE user SET nom="{user.nom}", prenom="{user.prenom}", email="{user.email}", role="{user.role}", entreprise_id="{user.entreprise_id}" WHERE id={user.id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": user}
@router.delete("/users/{user_id}")
async def delete_user(connected_user_email: Annotated[str, Depends(get_decoded_token)],user_id: int):
    check_user = query(f"SELECT * FROM user WHERE id={user_id}")
    if len(check_user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    req = f'DELETE FROM user WHERE id={user_id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Delete user"}
