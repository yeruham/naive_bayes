import pandas as pd


class Loader:

    @staticmethod
    def load_csv(url):
        df = pd.read_csv(url)
        return df



