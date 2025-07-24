import requests
import json


class Requests_data:


    def __init__(self, url):
        self.url = url
        self.data_classified = {}
        self.sub_request()


    def sub_request(self):
        response = requests.get(self.url)
        data_classified = response.json()
        self.data_classified = data_classified


    def get_percent_classified(self):
        percent_classified = self.data_classified["percent_classified"]
        return percent_classified


    def get_data_by_classified(self):
        data_by_classified = self.data_classified["data_by_classified"]
        return data_by_classified

