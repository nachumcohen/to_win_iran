class DataCleaner:


    @staticmethod
    def clean_punctuation_marks(column):
        data_clean = column.str.replace(r"[^\w\s]", "", regex=True)
        return data_clean

    @staticmethod
    def convert_to_lower(column):
        df_text = column.str.lower()
        return df_text