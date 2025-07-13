import uvicorn
from fastapi import FastAPI
from manager.manager import Manager

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "this api of a naive model, enter values of data with points between them and get an answer"}


@app.get('/buy_computer/{values}')
async def get_answer_by_classified(values):
    params = values.split('.')
    dict_data = receiving_data(params)
    answer = model.calc_new_data_by_classified(dict_data)
    return {"message": f"The estimated by {dict_data} is {answer}."}


def receiving_data(params: list):

    columns = [col for col in model._df.columns if col != model._classified_column]
    num_params = len(params) if len(params) <= len(columns) else len(columns)
    dict_data = {}

    for i in range(num_params):
        possible_values = model._df[columns[i]].unique()
        column_type = model._df[columns[i]].dtype
        if params[i].isdigit():
            params[i] = column_type.type(params[i])
        if params[i] in possible_values:
            dict_data[columns[i]] = params[i]

    return dict_data


if __name__ == "__main__":
    model = Manager()
    model.run_model()
    uvicorn.run(app, host= '127.0.0.1', port= 8000)