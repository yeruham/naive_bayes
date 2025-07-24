import uvicorn
from fastapi import FastAPI
import os
from requests_classified import Requests_data
import naive_calc


app = FastAPI()

app.state.file_name = None
app.state.classified_column = None
app.state.db_host = os.getenv("DB_HOST", "localhost")
app.state.url = f'http://{app.state.db_host}:8001/data_classified/'
app.state.percent_classified = None
app.state.data_by_classified = None
app.state.classified = None


@app.get('/')
async def root():
    return {"message": "This api of classified naive model, enter values of data with points between them and get an answer"}


@app.get('/{file_name}/{classified_column}/{values}')
async def get_answer_by_classified(file_name, classified_column, values):
    params = values.split('.')
    try:
        classified = get_classified(file_name, classified_column)
    except:
        return {"message": "Error: No data was received from the model."}

    dict_data = receiving_data(params)
    answer = classified.calc_answer(dict_data)
    return {"message": f"The estimated by {dict_data} is {answer}."}



def get_classified(file_name, classified_column):
    url = f"{app.state.url}?file_name={file_name}&classified_column={classified_column}"
    if (app.state.percent_classified is None
            or app.state.data_by_classified is None
            or app.state.file_name != file_name
            or app.state.classified_column != classified_column):

        request = Requests_data(url)
        app.state.percent_classified = request.get_percent_classified()
        app.state.data_by_classified = request.get_data_by_classified()
        app.state.classified = naive_calc.Naive_calc(app.state.percent_classified, app.state.data_by_classified)
        app.state.file_name = file_name
        app.state.classified_column = classified_column

    return app.state.classified


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
    keys = list(app.state.data_by_classified.keys())
    data = app.state.data_by_classified[keys[0]]
    return data



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8002)