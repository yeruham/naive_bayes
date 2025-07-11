import pandas as pd


class Naive_bayesian_model:

    def __init__(self, data_frame: pd.DataFrame, classified_column):
        self._validate_inputs(data_frame, classified_column)
        self._df = data_frame
        self._classified_column = classified_column
        self._percent_classified = {}
        self._data_by_classified = {}


    def _validate_inputs(self, data_frame, classified_column):
        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError("data_frame must be a pandas DataFrame")
        if classified_column not in data_frame.columns:
            raise ValueError(f"Column '{classified_column}' does not exist in the DataFrame")


    def _create_percent_classified(self):

        series_classified = self._df[self._classified_column]
        self._percent_classified = series_classified.value_counts(normalize=True).to_dict()


    def get_percent_classified(self):

        if not self._percent_classified:
            self._create_percent_classified()

        return self._percent_classified


    def __add_classified_to_data(self):

        series_classified = self._df[self._classified_column]

        for unique_values in series_classified.unique():
            self._data_by_classified[unique_values] = {}


    def __add_column_to_data(self, data_frame, column, classified):

        current_series = data_frame[column]
        data_percent = current_series.value_counts(normalize=True).to_dict()
        self._data_by_classified[classified][column] = data_percent


    def __laplace_smoothing_by_column(self, data_frame, column, classified):
        data = {}
        current_series = data_frame[column]

        for value in self._df[column].unique():
            num_values = current_series[(current_series == value)].count() + 1
            percent = num_values / (len(current_series) + self._df[column].nunique())
            data[value] = float(percent)

        self._data_by_classified[classified][column] = data


    def __create_data_by_classified(self):

        self.__add_classified_to_data()

        for classified in self._data_by_classified:

            data_frame = self._df[self._df[self._classified_column] == classified]
            data_frame = data_frame.drop(self._classified_column, axis= 1)

            for column in data_frame.columns:

                if data_frame[column].nunique() < self._df[column].nunique():
                    self.__laplace_smoothing_by_column(data_frame, column, classified)
                else:
                    self.__add_column_to_data(data_frame, column, classified)



    def get_data_by_classified(self):

        if not self._data_by_classified :
            self.__create_data_by_classified()

        return self._data_by_classified