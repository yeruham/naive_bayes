from naive_bayesian.naive_bayesian_model import Naive_bayesian_model


class Naive_calc:

    def __init__(self, percent_classified: dict, data_by_classified: dict):
        self._percent_classified = percent_classified
        self._data_by_classified = data_by_classified


    def calc_answer(self, dict_data: dict):

        result = self.calc_percent_by_classified(dict_data)

        high_percentage = 0
        answer = ""
        for classified, percent in result.items():
            if percent > high_percentage:
                high_percentage = percent
                answer = classified

        return answer


    def calc_percent_by_classified(self, dict_data: dict):
        result = {}

        for classified, columns in self._data_by_classified.items():
            result[classified] = 1

            for k, v in dict_data.items():
                try:
                    result[classified] *= columns[k][v]
                except:
                    pass

        return result

    def full_data_of_calc(self, dict_data: dict):

        result = self.calc_percent_by_classified(dict_data)
        information = f"data: {dict(dict_data)}\nresult: {result}\n"

        return information
