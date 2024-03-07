from pydantic import BaseModel

class Task(BaseModel):
    id: int | None = None
    nom: str
    description: str
    date_start: str
    date_end: str
    planning_id: int    