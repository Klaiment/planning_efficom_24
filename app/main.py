from fastapi import FastAPI
from routers.users import router as user_router
from internal.database import query
app = FastAPI()
# Vérification de la connexion à la base de données
@app.get("/")
async def root():
    return query("SELECT * FROM user")

app.include_router(user_router, tags=["Users"])
