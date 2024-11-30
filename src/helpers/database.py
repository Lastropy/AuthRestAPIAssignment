from fastapi import HTTPException
import json

# Utility functions for JSON handling
def read_json(file_path):
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
            return content
    except Exception as e:
        print("Error in read_json", repr(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

def write_json(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error in write_json", repr(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")