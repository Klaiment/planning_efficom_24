from pydantic import BaseModel


class Planning(BaseModel):
    id: int | None = None
    entreprise_id: int
    nom: str

