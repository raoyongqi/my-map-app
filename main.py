from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import aiofiles

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

geojson_file_path = 'geojson/tibet.geojson'
if not os.path.exists(geojson_file_path):
    raise HTTPException(status_code=404, detail="GeoJSON file not found")


@app.get("/geojson")
async def get_geojson():
    try:
        async with aiofiles.open(geojson_file_path, mode='r') as f:
            contents = await f.read()
            geojson_data = json.loads(contents)
        
        # 提取并转换坐标
        coordinates = geojson_data['features'][0]['geometry']['coordinates'][0]
        converted_coordinates = [[coord[1], coord[0]] for coord in coordinates]
        
        return {"coordinates": converted_coordinates}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading GeoJSON file: {str(e)}")
