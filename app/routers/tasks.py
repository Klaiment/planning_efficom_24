# System libs imports
from typing import Annotated

# Libs imports
from fastapi import APIRouter, HTTPException, status, Depends

# local imports
from internal.database import query, execute
from internal.auth import get_decoded_token
from models.tasks import Task

router = APIRouter()

# Routes tasks

@router.get("/tasks")
async def get_tasks(connected_user_email: Annotated[str, Depends(get_decoded_token)]):
    """
    Endpoint to return all tasks
    """
    tasks = query("SELECT * FROM task")
    return {"tasks": tasks}

@router.get("/task/{task_id}")
async def get_task(connected_user_email: Annotated[str, Depends(get_decoded_token)], task_id: int):
    """
    Endpoint to return task by id 
    """
    task = query(f"SELECT * FROM task WHERE id={task_id}")
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"task": task}

@router.post("/task/")
async def create_task(connected_user_email: Annotated[str, Depends(get_decoded_token)], task: Task):
    """
    Endpoint to create a task 
    """
    if task.planning_id is not None:
        existing_planning_id = query(f'SELECT id FROM planning WHERE id="{task.planning_id}"')
        if not existing_planning_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Planning_id not found")
    createTask = f'INSERT INTO task (nom, description, date_start, date_end, planning_id) VALUES ("{task.nom}","{task.description}","{task.date_start}","{task.date_end}",{task.planning_id})'
    execute(createTask)
    return {"message": "Task created"}

@router.put("/task/{task_id}")
async def update_task(connected_user_email: Annotated[str, Depends(get_decoded_token)], task_id: int, task: Task):
    """
    Endpoint to update a task 
    """
    check_task = query(f"SELECT * FROM task WHERE id={task_id}")
    if len(check_task) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    updateTask = f'UPDATE task SET nom="{task.nom}", description="{task.description}", date_start="{task.date_start}", date_end="{task.date_end}", planning_id={task.planning_id} WHERE id={task_id}'
    result = execute(updateTask)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    return {"message": "Task updated"}

@router.delete("/task/{task_id}")
async def delete_task(connected_user_email: Annotated[str, Depends(get_decoded_token)], task_id: int):
    """
    Endpoint to delete a task 
    """
    check_task = query(f"SELECT * FROM task WHERE id={task_id}")
    if len(check_task) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    deleteTask = f'DELETE FROM task WHERE id={task_id}'
    result = execute(deleteTask)
    if result == 0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    return {"message": "Task deleted"}

