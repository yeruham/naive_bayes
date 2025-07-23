from df.loader import Loader
from df.cleaner import Cleaner
import naive_bayesian.naive_bayesian_model as naive_model
import naive_bayesian.exam_naive_model as naive_exam
import naive_bayesian.naive_calc as naive_calc
from sklearn.model_selection import train_test_split


class Manager:

    def __init__(self, path, classified_column):
        self.df = Loader.load_csv(path)
        self.df = Cleaner.clean_df(self.df)
        self.df_train, self.df_test = train_test_split(self.df, test_size=0.3, random_state=42)
        self.classified_column = classified_column
        self.classified = None

    def run_trainer(self):
        trainer = naive_model.Naive_bayesian_model(self.df_train, self.classified_column)
        self.percent_classified = trainer.get_percent_classified()
        self.data_by_classified = trainer.get_data_by_classified()

    def create_classified(self):
        self.classified = naive_calc.Naive_calc(self.percent_classified, self.data_by_classified)

    def run_validator(self):
        if self.classified is None:
            self.create_classified()

        validator = naive_exam.Exam_naive_model(self.df_test, self.classified_column, self.classified)
        results = validator.run_test()
        print(f"The accuracy of the model is {results}.\n")

    def calc_new_data_by_classified(self, dict_data: dict):
        if self.classified is None:
            self.create_classified()

        if self.classified is not None:
            answer = self.classified.calc_answer(dict_data)
            return answer
