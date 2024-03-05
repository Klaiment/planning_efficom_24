from pydantic import BaseModel

class User(BaseModel):
    id: int
    nom: str
    prenom: str
    email: str
    password: str
    role: str
    entreprise_id: int