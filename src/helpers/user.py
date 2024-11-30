from passlib.context import CryptContext
from src.helpers.database import read_json
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def is_token_revoked(payload):
    json_content = read_json(os.environ["TOKEN_BLACKLIST_DB"])
    blacklist = json_content.get("tokens", [])
    tokenInBlackList = False
    for token in blacklist:
        if token["sub"] == payload["sub"] and token["exp"] == payload["exp"]:
            tokenInBlackList = True
            break
    return tokenInBlackList