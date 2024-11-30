from src.helpers.token import (create_new_access_token)
from src.models.main import (User, Token)
from src.controllers.users import (create_new_user, find_if_user_with_password_exists)
from src.main import app

@app.post("/signup")
def signup(userDetails: User):
    create_new_user(userDetails)
    return {"message": f"User {userDetails.username} registered successfully"}

@app.post("/signin", response_model=Token)
def signin(userDetails: User):
    find_if_user_with_password_exists(userDetails)
    return create_new_access_token({"sub": userDetails.username})