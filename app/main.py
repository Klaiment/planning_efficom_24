from fastapi import FastAPI
from routers.users import router as user_router
from internal.auth import router as auth_router
from internal.database import query
app = FastAPI()
# Vérification de la connexion à la base de données
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_router, tags=["Users"])
app.include_router(auth_router, tags=["Users"])
