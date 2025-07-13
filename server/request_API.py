import requests

URL = " http://127.0.0.1:8000/buy_computer/1.2.1.-1.1.1.1.1.0.0.0"

response = requests.get(url=URL)
print(response.json())