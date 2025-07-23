import uvicorn
from fastapi import FastAPI
from manager.manager import Manager

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "this api of a naive model, enter values of data with points between them and get an answer"}


@app.get('/{values}')
async def get_answer_by_classified(values):
    params = values.split('.')
    dict_data = receiving_data(params)
    answer = model.calc_new_data_by_classified(dict_data)
    return {"message": f"The estimated by {dict_data} is {answer}."}


def receiving_data(params: list):

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
    # path = r'C:\python_data\naive_bayes\data\phishing.csv'
    path = 'data/phishing.csv'
    classified_column = "class"
    model = Manager(path, classified_column)
    df = model.df
    model.run_trainer()
    model.run_validator()
    uvicorn.run(app, host= '127.0.0.1', port= 8001)