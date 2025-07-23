import uvicorn
from fastapi import FastAPI
import os
from requests_classified import Requests_data
import naive_calc


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "This api of classified naive model, enter values of data with points between them and get an answer"}


@app.get('/{values}')
async def get_answer_by_classified(values):
    params = values.split('.')
    try:
        dict_data = receiving_data(params)
        answer = classified.calc_answer(dict_data)
        return {"message": f"The estimated by {dict_data} is {answer}."}
    except:
        return {"message": "Error: No data was received from the model."}


def receiving_data(params: list):

    df_information = get_df_information()
    columns = [col for col in df_information]
    num_params = len(params) if len(params) <= len(columns) else len(columns)
    dict_data = {}

    for i in range(num_params):
        possible_values = df_information[columns[i]].keys()
        if params[i] in possible_values:
            dict_data[columns[i]] = params[i]

    return dict_data

def get_df_information():
    keys = list(data_by_classified.keys())
    data = data_by_classified[keys[0]]
    return data



if __name__ == "__main__":
    db_host = os.getenv("DB_HOST", "localhost")
    url = f'http://{db_host}:8001/data_classified'
    try:
        request = Requests_data(url)
        percent_classified = request.get_percent_classified()
        data_by_classified = request.get_data_by_classified()
        classified = naive_calc.Naive_calc(percent_classified, data_by_classified)
    except:
        pass

    uvicorn.run(app, host='0.0.0.0', port=8002)