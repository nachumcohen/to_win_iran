from app.fetcher import MongoConnector
from app.processor import Processor



def return_df_json():

    mongo_connector = MongoConnector()
    get_all = mongo_connector.get_all()
    processor = Processor(get_all)
    processor.add_rarest_word()
    processor.finding_the_emotion_of_the_text()
    processor.black_list()

    df = processor.return_df()

    df_dict = df.to_dict(orient="records")
    for row in df_dict:
        if "_id" in row:
            row["_id"] = str(row["_id"])

    return df_dict


