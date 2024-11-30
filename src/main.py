from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def base_path():
    return {"message": "This is the Auth REST API", "status": "OK"}
from src.api import (users, token)

from dotenv import load_dotenv
load_dotenv("./src/config/.env.development")