import logging
import time

from fastapi import FastAPI
from routers.users import router as user_router
import mariadb
import sys

app = FastAPI()
print("database_maria")

try:

    print("hw!")
    connection = mariadb.connect(
        user="usertest",
        password="mysecurepassword",
        host="database_maria",
        port=3306,
        database="planning"
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user')
    result = cursor.fetchall()
    print(result)
except mariadb.Error as err:
    print(f"Erreur lors de la connexion à la base de données : {err}")

# Vérification de la connexion à la base de données
app.include_router(user_router, tags=["Users"])
