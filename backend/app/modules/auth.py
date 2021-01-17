from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import app.utils.auth as utils
import app.utils.config as config

from app.utils.stat_collector import log_user_login
from pydantic import BaseModel
from typing import List, Optional
from datetime import timedelta
from pymongo import MongoClient
import pymongo

### CONFIG ###

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
router = APIRouter(
    prefix="/v1/auth",
    tags=["auth"],
)

##############

class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    user_id: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str




@router.post("/token", response_model=Token, tags=["auth"])
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = utils.authenticate_user(username=form_data.username,
                                   password=form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="USER_CREDENTIALS_INVALID",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    data_refresh_token = {"sub": user["username"],
                          "role": user["role"],
                          "first_name": user["first_name"],
                          }
    refresh_token_expires = timedelta(
        minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = utils.create_refresh_token(
        data=data_refresh_token, expires_delta=refresh_token_expires)

    data_access_token = {"sub": user["username"],
                         "role": user["role"],
                         "first_name": user["first_name"],
                         "user_id":user["_id"],
                         "refresh_token": refresh_token}

    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.create_access_token(
        data=data_access_token, expires_delta=access_token_expires
    )

    log_user_login(user=user['first_name'],bucket="user-data")

    return {"access_token": access_token}


@router.post("/register", tags=["auth"])
async def register_user(user: User):
    username = user.username
    password = user.password
    first_name = user.first_name
    last_name = user.last_name
    role = "VIEWER"

    res = utils.create_user(username=username, password=password)

    return JSONResponse(res)


@router.get("/me", tags=["auth"])
async def read_users(current_user: User = Depends(utils.get_current_tokenuser)):
    return current_user


@router.post("/refreshToken",response_model=Token, tags=["auth"])
async def refresh_token(user: User = Depends(utils.is_refresh_token_valid)):
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="USER_CREDENTIALS_INVALID",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data_refresh_token = {"sub": user["username"],
                          "role": user["role"],
                          "first_name": user["first_name"]}

    refresh_token_expires = timedelta(
        minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = utils.create_refresh_token(
        data=data_refresh_token, expires_delta=refresh_token_expires)

    data_access_token = {"sub": user["username"],
                         "role": user["role"],
                         "first_name": user["first_name"],
                         "user_id":user["_id"],
                         "refresh_token": refresh_token}

    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.create_access_token(
        data=data_access_token, expires_delta=access_token_expires
    )

    return {"access_token": access_token}

