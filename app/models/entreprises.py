from pydantic import BaseModel

class Entreprise(BaseModel):
    id: int | None = None
    nom: str
    adresse: str
    ville: str
    code_postal: str
    pays: str