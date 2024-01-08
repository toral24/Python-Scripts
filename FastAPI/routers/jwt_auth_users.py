
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import time, timedelta, datetime

router = APIRouter(
    prefix="/jau",
    tags=["jau"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "db1d03559760c75d0e5a80f5717d7bf499a67c9954fd22b24fba618cd6d8589d"

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db= {
    "mouredev":{
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disabled": False, 
        "password": "$2a$12$FeUYN9m6SJL0Tg.fV6Yp1.VnPkiFM6ZLkGTuOv6dJaEK6SyDceTqK" 

    },
    "toral":{
        "username": "toral",
        "full_name": "Sergio Toral",
        "email": "toral@sergio.com",
        "disabled": False, 
        "password": "$2a$12$YFuC2HTYDULHTFLbEblfy.kHg.RDUwSdCc8D8qiFQmD/rgnIRyXlm" 

    }
}


async def auth_user(token: str = Depends(oauth2)):

    excepcion = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="no tienes permiso",
            headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise excepcion

    except JWTError:
        raise excepcion
    
    return search_user(username)


'''async def current_user(user: str = Depends(auth_user)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="no tienes permiso",
            headers={"WWW-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )'''


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)

    access_token = {"sub": user.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return{"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(auth_user)):
    return user
