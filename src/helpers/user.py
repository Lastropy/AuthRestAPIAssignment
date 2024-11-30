from fastapi import HTTPException
from passlib.context import CryptContext
from src.helpers.database import read_json
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        print("Error in verify_password", repr(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

def hash_password(password):
    try:
        return pwd_context.hash(password)
    except Exception as e:
        print("Error in hash_password", repr(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

def is_token_revoked(payload):
    try:
        json_content = read_json(os.environ["TOKEN_BLACKLIST_DB"])
        blacklist = json_content.get("tokens", [])
        tokenInBlackList = False
        for token in blacklist:
            if token["sub"] == payload["sub"] and token["exp"] == payload["exp"]:
                tokenInBlackList = True
                break
        return tokenInBlackList
    except Exception as e:
        print("Error in is_token_revoked", repr(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")