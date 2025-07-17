import pandas as pd
import os


import naive_bayesian.naive_manager as naive_m


class Manager:

    def __init__(self):
        self._csv_path = None
        self._df = None
        self._classified_column = None
        self._naive_manager = None


    def run_program(self):

        self.run_model()
        keep_running = True

        while(keep_running):
            user_choice = self._repeat_menu()
            if user_choice == '1':
                data = self.receiving_data()
                self.calc_new_data_by_classified(data)
            elif user_choice == '2':
                keep_running = False
            else:
                pass


    def run_model(self):
        self.file_received()
        self._create_model()
        self._exam_model()


    def file_received(self):

        file_received = False
        while(not file_received):
            self._csv_path = input("Insert scv file path:\n")
            self._classified_column = input("Enter name of classified column:\n")
            file_received = self._create_df()
        print("The file has been received. The model is currently being produced.\n")


    def _create_df(self):
        if self._csv_path is not None and self._classified_column is not None:

            if os.path.exists(self._csv_path):
                self._df = pd.read_csv(self._csv_path)
                for col in self._df.columns:
                    if self._df[col].is_unique:
                        self._df = self._df.drop(columns=[col])

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


    def _repeat_menu(self):
        menu = input("To check data enter 1.\n"
                "To exit enter 2:\n")
        return menu

    def receiving_data(self):

        if isinstance(self._df, pd.DataFrame):
            data = {}
            columns = [col for col in self._df.columns if col != self._classified_column]

            for column in columns:
                    possible_values = self._df[column].unique()
                    column_type = self._df[column].dtype
                    value = input(f"Enter value for {column} column:\n")
                    if Manager.is_number(value):
                        print(column, value)
                        value = column_type.type(value)
                    if value in possible_values:
                        data[column] = value
            return data

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