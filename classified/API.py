import uvicorn
from fastapi import FastAPI

from df.cleaner import Cleaner
from requests_classified import Requests_data
import naive_calc
import pandas as pd

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "this api of classified naive model, enter values of data with points between them and get an answer"}


@app.get('/{values}')
async def get_answer_by_classified(values):
    params = values.split('.')
    dict_data = receiving_data(params)
    answer = classified.calc_answer(dict_data)
    return {"message": f"The estimated by {dict_data} is {answer}."}

def receiving_data(params: list):

    df = pd.read_csv(r'C:\python_data\naive_bayes\data\phishing.csv')
    df = Cleaner.clean_df(df)
    classified_column = "class"
    columns = [col for col in df.columns if col != classified_column]
    num_params = len(params) if len(params) <= len(columns) else len(columns)
    dict_data = {}

    for i in range(num_params):
        possible_values = df[columns[i]].unique()
        column_type = df[columns[i]].dtype
        if is_number(params[i]):
            params[i] = column_type.type(params[i])
        if params[i] in possible_values:
            dict_data[columns[i]] = params[i]

    return dict_data


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    url = 'http://127.0.0.1:8001/results'
    request = Requests_data(url)
    percent_classified = request.get_percent_classified()
    data_by_classified = request.get_data_by_classified()
    classified = naive_calc.Naive_calc(percent_classified, data_by_classified)
    uvicorn.run(app, host='127.0.0.1', port=8002)