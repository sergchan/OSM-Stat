from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

from pydantic import BaseModel, Field


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)

@app.get("/")
def home_page():
    return {"message": "hallow"}


path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database.json')