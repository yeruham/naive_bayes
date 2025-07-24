import uvicorn
from fastapi import FastAPI
import json
import os
from manager.manager import Manager

app = FastAPI()

# Application-level variables: default data path, model instance, file name, and target column
app.state.path = 'data/'
app.state.model = None
app.state.file_name = None
app.state.classified_column = None


@app.get('/')
async def root():
    # Basic route that describes the purpose of the API
    return {"message": "this api of a naive model, You can get the model results. "
            "in the path /data_classified with params: file_name= and classified_column="}


@app.get('/data_classified')
async def results(file_name: str, classified_column: str):
    """
    Runs the naive model on a CSV file based on a given classified column.
    If the model has already been created for the given file and column, the existing model is reused.

    Parameters:
    - file_name (str): Name of the CSV file (without extension) located in the /data directory.
    - classified_column (str): The name of the column to classify by.

    Returns:
    - JSON string with training results:
      {
        'percent_classified': dict,
        'data_by_classified': dict
      }
    """
    path = f"{app.state.path}{file_name}.csv"

    if not os.path.exists(path):
        return {"message": "Error: The file name does not exist."}
    else:
        # If the file exists, use existing model or train a new one with the given file and column.
        model = get_or_create_model(file_name, classified_column)
        percent_classified = model.percent_classified
        data_by_classified = model.data_by_classified
        data_classified = {'percent_classified': percent_classified, 'data_by_classified': data_by_classified}
        return data_classified



def get_or_create_model(file_name: str, classified_column: str):
    """
      Returns the cached naive model if already created with the same file and column.
      Otherwise, creates a new Manager instance, trains and validates the model.

      Parameters:
      - file_name (str): Name of the CSV file (without extension), located in the data directory.
      - classified_column (str): The name of the column to classify by.

      Returns:
      - Manager: Manager object containing the trained model and results.
      """
    path = f"{app.state.path}{file_name}.csv"
    if (app.state.model is None
            or app.state.file_name != file_name
            or app.state.classified_column != classified_column):

        app.state.file_name = file_name
        app.state.classified_column = classified_column
        app.state.model = Manager(path, classified_column)
        app.state.model.run_trainer()
        app.state.model.run_validator()

    return app.state.model




if __name__ == "__main__":
    uvicorn.run(app, host= '0.0.0.0', port= 8001)
