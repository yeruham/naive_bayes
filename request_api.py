import requests

URL = " http://127.0.0.1:8000/buy_computer/youth/medium/None/fair"

response = requests.get(url=URL)
print(response.json())