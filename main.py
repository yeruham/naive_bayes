import uvicorn
from fastapi import FastAPI
from manager.manager import Manager


app = FastAPI()


@app.get('/')
async def root():
    return {"message": "this api of a naive model"}


@app.get('buy_computer/{age}/{income}/{student}/{credit_rating}')
async def get_answer_by_classified(age, income, student, credit_rating):
    params = [age, income, student, credit_rating]
    dict_data = {"age": age, "income": income, "student": student, "credit_rating": credit_rating}
    answer = manager_model.calc_new_data_by_classified(dict_data)
    return {"message": f"The estimated by {dict_data} is {answer}."}



if __name__ == "__main__":
    manager_model = Manager()
    manager_model.run_program()
    uvicorn.run(app,  host="127.0.0.1", port=8000)
