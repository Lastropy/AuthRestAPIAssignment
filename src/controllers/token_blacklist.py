from fastapi import HTTPException
from src.models.main import Token
from src.helpers.database import (read_json, write_json)
import os

def create_new_token_blacklist(token: Token):
    try:
        token_blacklist_file = os.environ["TOKEN_BLACKLIST_DB"]
        db = read_json(token_blacklist_file)
        db.setdefault("tokens", []).append(token)
        write_json(token_blacklist_file, db)
    except Exception as e:
        print("Error in create_new_token_blacklist", repr(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")