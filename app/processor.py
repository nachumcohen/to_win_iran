from collections import Counter
import pandas as pd
from pandas import DataFrame
from app.fetcher import MongoConnector

from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# nltk.download('vader_lexicon')

class Processor:

    def __init__(self, df:DataFrame , col:str = 'Text'):
        self.df = df
        self.col = col

    def add_rarest_word(self):

        rare_words =[]
        for text in self.df[self.col]:
            words = text.split()
            if not words:
                rare_words.append("")
                continue

            counts = Counter(words)
            min_count = min(counts.values())

            rare_word = next(word for word, cnt in counts.items() if cnt == min_count)
            rare_words.append(rare_word)

        self.df['rarest_word'] = rare_words

    def finding_the_emotion_of_the_text(self):

        df_text = self.df[self.col]
        self.df['sentiment'] = df_text.apply(
            lambda text: (
                "positive" if (score := SentimentIntensityAnalyzer().polarity_scores(text)['compound']) >= 0.5 else
                "negative" if score <= -0.5 else
                "neutral"
            ) if pd.notna(text) and text.strip() != "" else ""
        )


    def black_list(self):

        with open("../data/weapons.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        df_text = self.df[self.col]
        self.df['sentiment'] = df_text.apply(
            lambda text: next(
                (weapon for weapon in lines if weapon in text),
                ""
            ) if pd.notna(text) and text.strip() != "" else ""
        )

    def return_df(self):
        return self.df
