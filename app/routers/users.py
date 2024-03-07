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
async def get_users(connected_user_email: Annotated[str, Depends(get_decoded_token)]):
    users = query("SELECT * FROM user")
    if len(users) == 0:
        raise HTTPException(status_code=404, detail="No users found")
    return {"users": users}

@router.post("/user/")
async def create_user(user: User):
    check_user = query(f"SELECT * FROM user WHERE email='{user.email}'")
    if len(check_user) != 0:
        raise HTTPException(status_code=400, detail="User already exists")
    check_entreprise = query(f"SELECT * FROM entreprise WHERE id={user.entreprise_id}")
    if len(check_entreprise) == 0:
        raise HTTPException(status_code=404, detail="Entreprise not found")
    password = password_hash(user.password)
    req = f'INSERT INTO user (nom, prenom, email, password, role, entreprise_id) VALUES ("{user.nom}","{user.prenom}","{user.email}","{password}","{user.role}","{user.entreprise_id}")'
    execute(req)
    return {"message": "Create user"}

@router.get("/user/{user_id}")
async def get_user(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int):
    user = query(f"SELECT * FROM user WHERE id={user_id}")
    if len(user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
@router.put("/user/{user_id}")
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
@router.delete("/user/{user_id}")
async def delete_user(connected_user_email: Annotated[str, Depends(get_decoded_token)],user_id: int):
    check_user = query(f"SELECT * FROM user WHERE id={user_id}")
    if len(check_user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    req = f'DELETE FROM user WHERE id={user_id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Delete user"}

# Routes planning
@router.get("/user/{user_id}/usertask", tags=["Users/plannings"])
async def get_plannings(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int):
    plannings = query(f"SELECT * FROM user_task WHERE user_id={user_id}")
    if len(plannings) == 0:
        raise HTTPException(status_code=404, detail="No plannings found for this user")
    json = []
    for planning in plannings:
        json.append({
            "id": planning[0],
            "user_id": planning[1],
            "task_id": planning[2]
        })
    return {"plannings": json}
@router.get("/user/{user_id}/usertask/{user_task}", tags=["Users/plannings"], description="jaime les moches")
async def get_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int, user_task: int):
    planning = query(f"SELECT * FROM user_task WHERE id={user_task} AND user_id={user_id}")
    if len(planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    return {"planning": planning}
@router.post("/user/{user_id}/planning/{task_id}", tags=["Users/plannings"])
async def create_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int, task_id: int):
    check_user = query(f"SELECT * FROM user WHERE id={user_id}")
    if len(check_user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    check_task = query(f"SELECT * FROM task WHERE id={task_id}")
    if len(check_task) == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    if len(query(f"SELECT * FROM user_task WHERE user_id={user_id} AND task_id={task_id}")) != 0:
        raise HTTPException(status_code=400, detail="Planning already exists")
    req = f'INSERT INTO user_task (user_id, task_id) VALUES ("{user_id}","{task_id}")'
    execute(req)
    return {"message": "Create planning"}
@router.delete("/user/{user_id}/planning/{task_id}", tags=["Users/plannings"])
async def delete_planning(connected_user_email: Annotated[str, Depends(get_decoded_token)], user_id: int, task_id: int):
    check_user = query(f"SELECT * FROM user WHERE id={user_id}")
    if len(check_user) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    check_planning = query(f"SELECT * FROM user_task WHERE task_id={task_id} AND user_id={user_id}")
    if len(check_planning) == 0:
        raise HTTPException(status_code=404, detail="Planning not found")
    planning_id = check_planning[0][0]
    req = f'DELETE FROM user_task WHERE id={planning_id}'
    result = execute(req)
    if result == 0:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Delete planning"}
