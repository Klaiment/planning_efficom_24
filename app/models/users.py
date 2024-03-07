from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    nom: str
    prenom: str
    email: str
    password: str
    role: str
    entreprise_id: int
    secret : str | None = None