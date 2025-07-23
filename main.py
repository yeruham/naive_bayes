import uvicorn
from fastapi import FastAPI
import json
from manager.manager import Manager

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "this api of a naive model, You can get the model results in the path data_classified"}


@app.get('/data_classified')
async def results():
    percent_classified = model.percent_classified
    data_by_classified = model.data_by_classified
    data_classified = {'percent_classified': percent_classified, 'data_by_classified': data_by_classified}
    return json.dumps(data_classified)





if __name__ == "__main__":
    # path = r'C:\python_data\naive_bayes\data\phishing.csv'
    path = 'data/phishing.csv'
    classified_column = "class"
    model = Manager(path, classified_column)
    model.run_trainer()
    model.run_validator()
    uvicorn.run(app, host= '0.0.0.0', port= 8001)
