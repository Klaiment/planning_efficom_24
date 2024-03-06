from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.planning import Planning
from internal.database import query, execute
from internal.auth import get_decoded_token
from typing import Annotated


router = APIRouter()

# Afficher tous les plannings
@router.get("/plannings")
async def get_plannings(connected_user_email: Annotated[str, Depends(get_decoded_token)]):
    plannings = query("SELECT * FROM planning")
    return {"plannings": plannings}

# Créer un planning
@router.post("/plannings/")
async def create_planning(planning: Planning, connected_user_email: str = Depends(get_decoded_token)):
    req = f'INSERT INTO planning (entreprise_id, nom) VALUES ("{planning.entreprise_id}","{planning.nom}")'
    execute(req)
    return {"message": "Planning created"}

# Afficher un planning
@router.get("/plannings/{planning_id}")
async def get_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], planning_id: int):
    planning = query(f"SELECT * FROM planning WHERE id={planning_id}")
    if len(planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    return {"planning": planning}

# Mettre à jour un planning
@router.put("/plannings/{planning_id}")
async def update_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], planning_id: int, planning: Planning):
    check_planning = query(f"SELECT * FROM planning WHERE id={planning_id}")
    if len(check_planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    req = f'UPDATE planning SET entreprise_id="{planning.entreprise_id}", nom="{planning.nom}" WHERE id={planning_id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Planning updated"}

# Supprimer un planning
@router.delete("/plannings/{planning_id}")
async def delete_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], planning_id: int):
    check_planning = query(f"SELECT * FROM planning WHERE id={planning_id}")
    if len(check_planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    req = f'DELETE FROM planning WHERE id={planning_id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Planning deleted"}

# Afficher les plannings d'une entreprise
@router.get("/plannings/entreprise/{entreprise_id}")
async def get_plannings_by_entreprise(connected_user_email: Annotated[str, Depends(get_decoded_token)], entreprise_id: int):
    plannings = query(f"SELECT * FROM planning WHERE entreprise_id={entreprise_id}")
    return {"plannings": plannings}

# Afficher les plannings d'un utilisateur
@router.get("/plannings/user/{user_id}")
async def get_plannings_by_user(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int):
    plannings = query(f"SELECT * FROM planning WHERE id IN (SELECT planning_id FROM user_planning WHERE user_id={user_id})")
    return {"plannings": plannings}