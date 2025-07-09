from naive_bayesian.naive_bayesian_model import Naive_bayesian_model


class Naive_calc:

    def __init__(self, percent_classified, data_by_classified):
        self._percent_classified = percent_classified
        self._data_by_classified = data_by_classified


    def naive_calc_by_column(self, dict_data: dict):

        result = self.percent_by_column(dict_data)

        high_percentage = 0
        answer = ""
        for classified, percent in result.items():
            if percent > high_percentage:
                high_percentage = percent
                answer = classified

        return answer


    def percent_by_column(self, dict_data: dict):
        result = {}

        for classified, columns in self._data_by_classified.items():
            result[classified] = 1

            for k, percent in dict_data.items():
                result[classified] *= columns[k][percent]


        return result


