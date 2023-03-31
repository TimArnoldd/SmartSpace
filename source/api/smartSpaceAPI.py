from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
async def root():
    with open('..\data\parkingInformation.json', 'r') as openfile:
        json_object = json.load(openfile)
    return json_object