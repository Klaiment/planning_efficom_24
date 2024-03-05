from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Entreprise(BaseModel):
    id: int
    nom: str
    adresse: str
    ville: str
    code_postal: str
    pays: str
class User(BaseModel):
    id: int
    nom: str
    prenom: str
    email: str
    password: str
    role: str
    entreprise_id: int
class Planning(BaseModel):
    id: int
    date_start: str
    date_end: str
    nom: str
    entreprise_id: int
class UserPlanning(BaseModel):
    id: int
    user_id: int
    planning_id: int
class Notification(BaseModel):
    id: int
    id_user: int
    id_planning: int
    title: str
    details: str
class NotificationVue(BaseModel):
    id: int
    user_id: int
    notif_id: int
    date: str
@app.get("/")
async def root():
    return {"message": "Hello World"}

