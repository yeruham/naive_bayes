FROM python:3.10

workdir /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY data/ ./data/

COPY naive_bayesian/ ./naive_bayesian/

COPY server/naive_API.py ./main.py

COPY manager/ ./manager/

EXPOSE 8001

CMD ["python", "main.py"]