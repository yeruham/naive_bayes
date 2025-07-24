import pandas as pd


class Cleaner:

    @staticmethod
    def clean_df(data_frame: pd.DataFrame):
        for col in data_frame.columns:
            if data_frame[col].is_unique:
                data_frame = data_frame.drop(columns=[col])

        return data_frame

    @staticmethod
    def convert_to_string(data_frame: pd.DataFrame):
        data_frame = data_frame.astype(str)
        return data_frame
