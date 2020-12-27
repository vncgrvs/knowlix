import pymongo
from pymongo import MongoClient
import os
from passlib.context import CryptContext
from jose import JWTError, jwt
import config
from passlib.context import CryptContext

MONGODB = os.getenv("MONGODB")
client = MongoClient(MONGODB)
users = client["users"]["users"]
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_existence(sections, db):
    exists_already = False
    no_sections = len(sections)
    query = {"kwargs.sections": {"$size": no_sections, "$all": sections}}

    hits = db.count_documents(query)

    if hits > 0:
        exists_already = True

    return exists_already


def authenticate_user(db=users, username: str, password: str):
    user=get_user(username=username)
    hashed_pw = user["password"]

    
    if not user:
        return False

    if not verify_pw(password,hashed_pw):
        return False
    
    


def create_user(db=users, username: str, password: str):
    user_count = db.count_documents({"email": username})
    hashed_pw = pwd_context.hash(password)
    error = None
    created = False

    if user_count == 0:
        db.insert_one({"username": username, "password": hashed_pw})
        created = True
    else:
        error = "User exists already!"

    return {"created": created, "error": error}


def get_user(db=users, username:str):
    user_count = db.find_one({"email": username})

    return user

def verify_pw(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)