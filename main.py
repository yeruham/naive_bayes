import uvicorn
from fastapi import FastAPI
import json
import os
from manager.manager import Manager

app = FastAPI()

app.state.path = 'data/'
app.state.model = None
app.state.file_name = None

@app.get('/')
async def root():
    return {"message": "this api of a naive model, You can get the model results in the path data_classified"}


@app.get('/data_classified')
async def results(file_name, classified_column):
    path = f"{app.state.path}{file_name}.csv"
    if os.path.exists(path):
        if app.state.model is None or app.state.file_name != file_name:
            app.state.file_name = file_name
            app.state.model = create_model(path, classified_column)

        percent_classified = app.state.model.percent_classified
        data_by_classified = app.state.model.data_by_classified
        data_classified = {'percent_classified': percent_classified, 'data_by_classified': data_by_classified}
        return json.dumps(data_classified)
    else:
        return {"message": "Error: The file name does not exist."}



def create_model(path, classified_column):
    model = Manager(path, classified_column)
    model.run_trainer()
    model.run_validator()
    return model



if __name__ == "__main__":
    uvicorn.run(app, host= '0.0.0.0', port= 8001)
