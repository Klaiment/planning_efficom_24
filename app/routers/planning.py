# System libs imports
from typing import Annotated

# Libs imports
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

# local imports
from models.planning import Planning
from internal.database import query, execute
from internal.auth import get_decoded_token

router = APIRouter()

@router.get("/plannings")
async def get_plannings(connected_user_email: Annotated[str, Depends(get_decoded_token)]):
    """
    Endpoint to return all plannings
    """
    plannings = query("SELECT * FROM planning")
    return {"plannings": plannings}

@router.post("/plannings/")
async def create_planning(planning: Planning, connected_user_email: str = Depends(get_decoded_token)):
    """
    Endpoint to create a new planning
    """
    req = f'INSERT INTO planning (entreprise_id, nom) VALUES ("{planning.entreprise_id}","{planning.nom}")'
    execute(req)
    return {"message": "Planning created"}

@router.get("/plannings/{planning_id}")
async def get_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], planning_id: int):
    """
    Endpoint to return a specific planning by ID
    """
    planning = query(f"SELECT * FROM planning WHERE id={planning_id}")
    if len(planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    return {"planning": planning}

@router.put("/plannings/{planning_id}")
async def update_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], planning_id: int, planning: Planning):
    """
    Endpoint to update a specific planning by ID
    """
    check_planning = query(f"SELECT * FROM planning WHERE id={planning_id}")
    if len(check_planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    req = f'UPDATE planning SET entreprise_id="{planning.entreprise_id}", nom="{planning.nom}" WHERE id={planning_id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Planning updated"}

@router.delete("/plannings/{planning_id}")
async def delete_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], planning_id: int):
    """
    Endpoint to delete a specific planning by ID
    """
    check_planning = query(f"SELECT * FROM planning WHERE id={planning_id}")
    if len(check_planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    req = f'DELETE FROM planning WHERE id={planning_id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Planning deleted"}

@router.get("/plannings/entreprise/{entreprise_id}")
async def get_plannings_by_entreprise(connected_user_email: Annotated[str, Depends(get_decoded_token)], entreprise_id: int):
    """
    Endpoint to return all plannings for a specific entreprise
    """
    plannings = query(f"SELECT * FROM planning WHERE entreprise_id={entreprise_id}")
    return {"plannings": plannings}