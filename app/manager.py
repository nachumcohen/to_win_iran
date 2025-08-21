from app.fetcher import MongoConnector
from app.processor import Processor


mongoConnector = MongoConnector()
get_all = mongoConnector.get_all()
processor = Processor(get_all)
processor.add_rarest_word()
processor.finding_the_emotion_of_the_text()
processor.black_list()

df = processor.return_df()
df.to_csv("../data/mongodb.csv", index=False, encoding="utf-8")


