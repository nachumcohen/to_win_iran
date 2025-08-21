from fastapi import FastAPI
from app.manager import return_df_json

app = FastAPI()

@app.get("/data")
def return_data():
    return return_df_json()

