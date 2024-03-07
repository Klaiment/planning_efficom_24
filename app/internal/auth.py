# System libs imports
from typing import Annotated
from datetime import timedelta, datetime, timezone

# Libs imports
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from hashlib import sha256

# local imports
from models.users import User
from internal.database import query, execute
from cryptography.fernet import Fernet

def password_hash(password: str):
    return sha256(password.encode()).hexdigest()

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours
SECRET_KEY = '=+ByyTL_Ct:rfi)0?z/_xbae7Zou$jS"]9+::y)ZlW#*8lF(~|V"|5Tj]bjLG4$'
ALGORITHM = "HS256"


async def get_decoded_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return (payload.get("sub"))
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token",
                            headers={"WWW-Authenticate": "Bearer"}) from e


@router.post("/login")
async def login(credentials: Annotated[OAuth2PasswordRequestForm, Depends()]):
    if credentials.username is not None and credentials.password is not None:
        username = credentials.username
        check_user = query(f"SELECT * FROM user")
        password = credentials.password
        password = password_hash(password)
        for unitUser in check_user:
            chipher_check = Fernet(unitUser[7])
            email_dechiffre = chipher_check.decrypt(unitUser[3]).decode()
            if email_dechiffre == credentials.username:
                if unitUser[4] == password:
                    print(password)
                    print(unitUser[4])
                    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                    jwt_creation_time = datetime.now(timezone.utc)
                    expire = jwt_creation_time + access_token_expires
                    to_encode = {
                        "sub": credentials.username,
                        "exp": expire,
                        "iat": jwt_creation_time
                    }

                    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
                    return {"access_token": encoded_jwt, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")