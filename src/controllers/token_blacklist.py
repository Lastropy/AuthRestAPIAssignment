from src.models.main import Token
from src.helpers.database import (read_json, write_json)
import os

def create_new_token_blacklist(token: Token):
    token_blacklist_file = os.environ["TOKEN_BLACKLIST_DB"]
    db = read_json(token_blacklist_file)
    db.setdefault("tokens", []).append(token)
    write_json(token_blacklist_file, db)