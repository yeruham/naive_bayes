import pandas as pd
import os
import naive_bayesian.naive_manager as naive_m
from cleaner import Cleaner


class Manager:

    def __init__(self):
        self._csv_path = None
        self._df = None
        self._classified_column = None
        self._naive_manager = None


    def run_model(self):
        self.file_received()
        self._create_model()
        self._exam_model()


    def file_received(self):

        file_received = False
        while(not file_received):
            self._csv_path = input("Insert csv file path:\n")
            self._classified_column = input("Enter name of classified column:\n")
            file_received = self._create_df()
        print("The file has been received. The model is currently being produced.\n")


    def _create_df(self):
        if self._csv_path is not None and self._classified_column is not None:

            if os.path.exists(self._csv_path):
                self._df = pd.read_csv(self._csv_path)
                self._df = Cleaner.clean_df(self._df)

                if self._classified_column in self._df.columns:
                    return True
        else:
            return False


    def _create_model(self):
        if self._df is not None:
            self._naive_manager = naive_m.Naive_manager(self._df, self._classified_column)
            self._naive_manager.create_model()
            print("The model was created successfully.\n"
                  "The model will then be tested and its accuracy percentage will be displayed.\n")


    def _exam_model(self):
        if self._naive_manager is not None:
            results = self._naive_manager.exam_model()
            print(f"The accuracy of the model is {results}.\n")



    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def calc_new_data_by_classified(self, dict_data: dict):
        if dict_data:
            answer = self._naive_manager.calc_new_data_by_classified(dict_data)
            print(f"\nThe {self._classified_column} estimated by {dict_data} is {answer}.\n")
            return answer
        else:
            print("The values entered do not exist in the model.\n")