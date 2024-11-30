# Create and decode tokens
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException
import os

def create_new_access_token(data: dict, expires_delta: timedelta = None):
    expireDuration = int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])
    expireTime = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=expireDuration))
    data.update({"exp": expireTime})
    access_token = jwt.encode(data, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"])
    return {"access_token": access_token, "token_type": "bearer"}

def decode_token(token: str):
    try:
        algorithm = os.environ["ALGORITHM"]
        return jwt.decode(token, os.environ["SECRET_KEY"], algorithms=algorithm)
    except JWTError as e:
        print("Error in decode_token", repr(e))
        raise HTTPException(status_code=401, detail="Invalid/Expired token")