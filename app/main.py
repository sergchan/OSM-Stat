from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from utils import json_to_dict_list
import os
from typing import Optional

import folium

from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/map", response_class=HTMLResponse)
def render_map(lat: float = 40.7128, lon: float = -74.0060):
    
    m = folium.Map(location=[lat, lon], zoom_start=12)
    
    
    folium.Marker(
        location=[lat, lon],
        popup="Selected Location",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)
    
    return m.get_root().render()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list

@app.get("/")
def home_page():
    return {"message": "hallow"}


path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database.json')