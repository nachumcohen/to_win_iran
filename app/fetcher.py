import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class MongoConnector:
    def __init__(self , conn:str = "MONGO_CONN" , dbname:str = "IranMalDB"):

        conn_str = os.getenv(conn)

        self.client = MongoClient(conn_str)
        self.db = self.client[dbname]

    def get_all(self, collection_name: str = "tweets"):

        collection = self.db[collection_name]
        data = collection.find({})
        df = pd.DataFrame(data)

        return df
