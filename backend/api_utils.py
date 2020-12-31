import pymongo
from pymongo import MongoClient
from fastapi import FastAPI, HTTPException, Depends, status, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os
from passlib.context import CryptContext
from jose import JWTError, jwt
import config
from passlib.context import CryptContext
from datetime import timedelta, datetime

from typing import Optional, List
import config
from pydantic import BaseModel

MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
users = client["users"]["users"]
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/token")


def check_existence(sections, db):
    exists_already = False
    no_sections = len(sections)
    query = {"kwargs.sections": {"$size": no_sections, "$all": sections}}

    hits = db.count_documents(query)

    if hits > 0:
        exists_already = True

    return exists_already


def authenticate_user(username: str, password: str, db=users):
    user = get_user(username=username, include_pw=True, include_id=True)
    hashed_pw = user["password"]

    if not user:
        return False

    if not verify_pw(password, hashed_pw):
        return False

    return user


def create_user(username: str, password: str, first_name: str, last_name: str,
                role: str, db=users):
    user_count = db.count_documents({"username": username})
    hashed_pw = pwd_context.hash(password)
    error = None
    created = False

    if user_count == 0:
        query = {"username": username,
                 "password": hashed_pw,
                 "first_name": first_name,
                 "last_name": last_name,
                 "role": role}
        db.insert_one(query)
        created = True
    else:
        error = "User exists already!"

    return {"created": created, "error": error}


def create_refresh_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expires = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expires})
    refresh_token = jwt.encode(
        to_encode, config.REFRESH_KEY, algorithm=config.ALGORITHM)
    return refresh_token


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


def get_user(username: str, include_pw=True, include_id=True, db=users):

    if include_pw:
        user = db.find_one({"username": username}, {
            "_id": 1,
            "username": 1,
            "password": 1,
            "first_name": 1,
            "last_name": 1,
            "role": 1
        })
        
        user.update({"_id": str(user["_id"])})

    elif include_id:
        user = db.find_one({"username": username}, {
            "_id": 1,
            "username": 1,
            "password": 1,
            "first_name": 1,
            "last_name": 1,
            "role": 1
        })
        user.update({"_id": str(user["_id"])})

    elif (include_pw and include_id):
        user = db.find_one({"username": username}, {
            "_id": 1,
            "username": 1,
            "password": 1,
            "first_name": 1,
            "last_name": 1,
            "role": 1
        })
        user.update({"_id": str(user["_id"])})

    elif (not include_pw and include_id):
        user = db.find_one({"username": username}, {
            "_id": 1,
            "username": 1,
            "password": 1,
            "first_name": 1,
            "last_name": 1,
            "role": 1
        })
        user.update({"_id": str(user["_id"])})

    elif (include_pw and not include_id):
        user = db.find_one({"username": username}, {
            "_id": 0,
            "username": 1,
            "password": 1,
            "first_name": 1,
            "last_name": 1,
            "role": 1
        })
        

    else:
        user = db.find_one({"username": username}, {
            "_id": 0,
            "username": 1,
            "password": 1,
            "first_name": 1,
            "last_name": 1,
            "role": 1
        })
        

    return user


def verify_pw(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def is_access_token_valid(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Access Token invalid",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY,
                             algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return True
    except JWTError:
        raise credentials_exception
        return False


async def is_refresh_token_valid(token: str = Depends(oauth2_scheme)):
    access_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="ACCESS_TOKEN_INVALID",
        headers={"WWW-Authenticate": "Bearer"},
    )

    refresh_token_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="REFRESH_TOKEN_INVALID",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        access_payload = jwt.decode(token, config.SECRET_KEY,
                                    algorithms=[config.ALGORITHM])

        refresh_token: str = access_payload.get("refresh_token")
        username: str = access_payload.get("sub")

        try:
            refresh_token_payload = jwt.decode(refresh_token, config.REFRESH_KEY,
                                               algorithms=[config.ALGORITHM])

            user = get_user(username=username,
                            include_id=True, include_pw=False)

            return user

        except JWTError:
            raise refresh_token_exception

    except JWTError: #specify errors better

        raise access_exception


async def get_current_tokenuser(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="USER_CREDENTIALS_INVALID",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY,
                             algorithms=[config.ALGORITHM])

        username: str = payload.get("sub")
        user = get_user(username=username, include_pw=False)

        if user is None:
            raise credentials_exception
        return user

    except JWTError:
        raise credentials_exception


def get_header(header: Optional[List[str]] = Header(None)):
    return header
