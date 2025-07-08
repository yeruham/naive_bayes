import pandas as pd


class Naive_bayesian_model:

    def __init__(self, data_frame, classified_column):
        self._df = data_frame
        self._classified_column = classified_column
        self._data_by_classified = {}

    def _create_percent_classified_in_dict(self):

        series_classified = self._df[self._classified_column]

        for unique_values in series_classified.unique():
            num_values = series_classified[series_classified == unique_values].count()
            percent = num_values / len(series_classified)

            self._data_by_classified[unique_values] = [float(percent), {}]

        return self._data_by_classified

    def _create_percent_columns_in_dict(self):

        for classified in self._data_by_classified:
            print(classified)

            for column in self._df.columns:
                data = {}

                if column != self._classified_column:
                    current_series = self._df[column]
                    for values in current_series.unique():
                        num_values = current_series[(current_series == values) & (self._df[self._classified_column] == classified)].count()
                        print((self._df[self._classified_column] == classified).sum())
                        data[values] = float(num_values / (self._df[self._classified_column] == classified).sum())

                    self._data_by_classified[classified][1][column] = data

        return self._data_by_classified

df = pd.read_csv('data/buy_computer_data.csv')
df = df.drop('id', axis=1)

n = Naive_bayesian_model(df, 'Buy_Computer')
print(n._create_percent_classified_in_dict())
print(n._create_percent_columns_in_dict())
