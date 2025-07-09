import naive_bayesian.naive_bayesian_model as naive_m
import naive_bayesian.naive_calc as naive_c
import naive_bayesian.exam_naive_model as naive_e
from sklearn.model_selection import train_test_split

class Naive_manager:

    def __init__(self, data_frame, classified_column):

        self._df_train, self.df_test = train_test_split(data_frame, test_size=0.3, random_state=42)
        self._classified_column = classified_column
        self._naive_model = None
        self._naive_calc = None
        self._naive_exam = None
        self._percent_classified = None
        self._data_by_classified = None


    def create_model(self):
        self._naive_model = naive_m.Naive_bayesian_model(self._df_train, self._classified_column)
        self._percent_classified = self._naive_model.get_percent_classified()
        self._data_by_classified = self._naive_model.get_data_by_classified()

    def __create_naive_calc(self):
        if self._percent_classified is not None and self._data_by_classified is not None:
            self._naive_calc = naive_c.Naive_calc(self._percent_classified, self._data_by_classified)

    def exam_model(self):
        if self._naive_calc is None:
            self.__create_naive_calc()

        if self._naive_calc is not None:
            self._naive_exam = naive_e.Exam_naive_model(self.df_test, self._classified_column, self._naive_calc)
            results = self._naive_exam.run_test()
            return results


    def calc_new_data_by_classified(self, dict_data: dict):
        if self._naive_calc is None:
            self.__create_naive_calc()

        if self._naive_calc is not None:
            answer = self._naive_calc.calc_answer(dict_data)
            return answer
