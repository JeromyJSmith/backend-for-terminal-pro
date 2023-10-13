import os
import json
import requests
import time
import json

import mindsdb_sdk

# https://mindsdb.com/blog/introduction-to-python-sdk-interact-with-mindsdb-directly-from-python


server = mindsdb_sdk.connect(login='xxx', password='xxxx')


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

### Configure CORS
origins = [
    "http://localhost",
    "http://localhost:5050",
    "https://pro.openbb.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Endpoints
@app.get("/")
def read_root():
    return {"Info": "Backend Template for the OpenBB Terminal Pro"}


@app.get("/widgets.json")
def get_widgets():
    """Widgets configuration file for the OpenBB Terminal Pro"""
    file_path = "widgets.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    return JSONResponse(content=data)


@app.get("/home_rentals_prediction")
def get_home_rentals_prediction():
    """Return MindsDB data"""

    try:
        database = server.get_database('example_db')
        table = database.get_table('demo_data.home_rentals')
        project = server.get_project('mindsdb')
        model = project.get_model('home_rentals_model')
        predictions = model.predict(table)

        predictions = predictions.drop("rental_price_explain", axis=1)

        data_dict = predictions.to_dict(orient="records")

        for i, data in enumerate(data_dict, start=1):
            data['id'] = i

    except Exception as err:
        print(f"Programming Error: {err}")

    return data_dict