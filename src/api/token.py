
from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from src.controllers.token_blacklist import create_new_token_blacklist
from src.helpers.token import create_new_access_token, decode_token
from src.helpers.user import is_token_revoked
from src.models.main import Token
from src.main import app

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")

@app.get("/authorization")
def secure_endpoint(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if is_token_revoked(payload):
        raise HTTPException(status_code=401, detail="Token revoked")
    return {"message": "Secure data", "user": payload["sub"]}

@app.post("/signout")
def logout(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    print(payload)
    if is_token_revoked(payload):
        print("token already revoked")
        raise HTTPException(status_code=401, detail="Token revoked")
    print("token not revoked")
    create_new_token_blacklist(payload)
    return {"message": "Token revoked successfully"}

@app.post("/refresh-token", response_model=Token)
def refresh_token(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if is_token_revoked(payload):
        raise HTTPException(status_code=401, detail="Token revoked")
    return create_new_access_token({"sub": payload["sub"]})