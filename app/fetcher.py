import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

from data_clean import DataCleaner

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

        """--------------------------------------------------------------------------"""
        """clear text and save to csv"""
        text = df['Text']
        text2 = DataCleaner.clean_punctuation_marks(text)
        text3 = DataCleaner.convert_to_lower(text2)

        df['Text'] = text3
        df.to_csv("../data/mongodb.csv", index=False, encoding="utf-8")
        """--------------------------------------------------------------------------"""

        return df
