from src.helpers.database import (read_json, write_json)
from src.helpers.user import (hash_password, verify_password)
from src.models.main import User
import os
from fastapi import HTTPException

def create_new_user(userDetails: User): 
    username = userDetails.username
    password = userDetails.password
    user_db_file = os.environ["USER_DB"]
    db = read_json(user_db_file)
    if any(u["username"] == username for u in db.get("users", [])):
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(password)
    new_user = {"username": username, "hashed_password": hashed_password}
    db.setdefault("users", []).append(new_user)
    write_json(user_db_file, db)

def find_if_user_with_password_exists(userDetails: User):
    username = userDetails.username
    password = userDetails.password
    users = read_json(os.environ["USER_DB"]).get("users", [])
    user = next((u for u in users if u["username"] == username), None)
    if not (user and verify_password(password, user["hashed_password"])):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
def remove_user_if_exists(username: str):
    user_db_file = os.environ["USER_DB"]
    db = read_json(user_db_file)
    idx = -1
    for user, i in db.get("users", []):
        if user["username"] == username:
            idx = i
            break
    if idx != -1: 
        db["users"].pop(idx)
        write_json(user_db_file, db)
    else: 
        raise HTTPException(status_code=400, detail="Username does not exist")