import pandas as pd
from naive_bayesian.naive_calc import Naive_calc


class Exam_naive_model:

    def __init__(self, data_frame, classified_column , naive_calc: Naive_calc):
        self._df = data_frame
        self._classified_column = classified_column
        self._naive_calc = naive_calc


    def run_test(self):

        matching_percentage = 0
        num_rows = self._df.shape[0]
        for index, row in self._df.iterrows():

            classified = row.pop(self._classified_column)
            answer = self._naive_calc.calc_answer(row)
            print(self._naive_calc.full_data_of_calc(row))
            if answer == classified:
                matching_percentage += 1

        return matching_percentage / num_rows





