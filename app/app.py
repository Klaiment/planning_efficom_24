# System libs imports
from typing import Annotated
from datetime import timedelta, datetime, timezone

# Libs imports
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt

#local imports

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

ACCESS_TOKEN_EXPIRE_MINUTES= 60*24 # 24 hours
SECRET_KEY = "c60655a4fb84f0883c0ee1d2510eb332769029bc23ecd5796c53010ab01ba6f7"
ALGORITHM = "HS256"