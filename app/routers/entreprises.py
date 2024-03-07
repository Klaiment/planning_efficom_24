from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.entreprises import Entreprise
from internal.database import query, execute
from hashlib import sha256
from internal.auth import get_decoded_token


def password_hash(password: str):
    return sha256(password.encode()).hexdigest()

router = APIRouter()

# Routes entreprises

@router.get("/entreprises")
async def get_entreprise(connected_user_email: Annotated[str, Depends(get_decoded_token)]):
    """
    Endpoint to return all companies
    """
    entreprises = query("SELECT * FROM entreprise")
    return {"entreprise": entreprises}

@router.get("/entreprise/{entreprise_id}")
async def get_entreprise(connected_user_email: Annotated[str, Depends(get_decoded_token)], entreprise_id: int):
    """
    Endpoint to return company by id 
    """
    entreprise = query(f"SELECT * FROM entreprise WHERE id={entreprise_id}")
    if entreprise is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return {"entreprise": entreprise}

@router.post("/entreprise/")
async def create_entreprise(connected_user_email: Annotated[str, Depends(get_decoded_token)], entreprise: Entreprise):
    """
    Endpoint to create a company 
    """
    createEntreprise = f'INSERT INTO entreprise (nom, adresse, ville, code_postal, pays) VALUES ("{entreprise.nom}","{entreprise.adresse}","{entreprise.ville}","{entreprise.code_postal}","{entreprise.pays}")'
    execute(createEntreprise)
    return {"message": "Company create"}

@router.put("/entreprise/{entreprise_id}")
async def update_entreprise(connected_user_email: Annotated[str, Depends(get_decoded_token)], entreprise: Entreprise):
    """
    Endpoint to update a company 
    """
    check_entreprise = query(f"SELECT * FROM entreprise WHERE id={entreprise.id}")
    if len(check_entreprise) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    updateEntreprise = f'UPDATE entreprise SET nom="{entreprise.nom}", adresse="{entreprise.adresse}", ville="{entreprise.ville}", code_postal="{entreprise.code_postal}", pays="{entreprise.pays}" WHERE id={entreprise.id}'
    result = execute(updateEntreprise)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    return {"message": entreprise}

@router.delete("/entreprise/{entreprise_id}")
async def delete_entreprise(connected_user_email: Annotated[str, Depends(get_decoded_token)], entreprise_id: int):
    """
    Endpoint to delete a company 
    """
    check_entreprise = query(f"SELECT * FROM entreprise WHERE id={entreprise_id}")
    if len(check_entreprise) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entreprise not found")
    deleteEntreprise = f'DELETE FROM entreprise WHERE id={entreprise_id}'
    result = execute(deleteEntreprise)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    return {"message": "Company Delete"}