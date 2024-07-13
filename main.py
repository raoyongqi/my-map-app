# fastapi-backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/geojson")
def get_geojson():
    with open('geojson/tibet.json') as f:
        geojson_data = json.load(f)
    return geojson_data
