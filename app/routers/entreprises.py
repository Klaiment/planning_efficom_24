from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.entreprises import Entreprise
from internal.database import query, execute

router = APIRouter()

# Routes entreprises

@router.get("/entreprise")
async def get_entreprise():
    entreprises = query("SELECT * FROM entreprise")
    return {"entreprise": entreprises}

@router.get("/entreprise/{entreprise_id}", response_model=Entreprise)
async def get_entreprise(entreprise_id: int):
    entreprises = query("SELECT * FROM entreprise WHERE id=%s")
    if Entreprise is None:
        raise HTTPException(status_code=404, detail="Entreprise not found")
    return {"entreprise": entreprises}

@router.post("/entreprise/")
async def create_entreprise(entreprise: Entreprise):
    req = f'INSERT INTO entreprise (nom, adresse, ville, code_postal, pays) VALUES ("{entreprise.nom}","{entreprise.adresse}","{entreprise.ville}","{entreprise.code_postal}","{entreprise.pays}")'
    execute(req)
    return {"message": "Create Entreprise"}


