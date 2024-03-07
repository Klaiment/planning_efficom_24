from pydantic import BaseModel


class Notification(BaseModel):
    id: int | None = None
    planning_id: int
    user_id: int
    detail: str
    title: str
