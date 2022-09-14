import requests
import pprint
import os

headers = {"Authorization": os.getenv("SHEETLY_AUTHORIZATION")}


class DataManager:

    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SHEETS_API = 'https://api.sheety.co/f38d9fbf42fb4565608233e1ce994b28/flightDeals/prices'

    def callData(self):
        return requests.get(url=self.SHEETS_API, headers=headers)

    def printData(self):
        pprint.pprint(self.callData().json())

    def getData(self):
        return self.callData().json()

    def writeData(self, row_id, data):
        update_data = {"price": data}
        requests.put(url=f"{self.SHEETS_API}/{row_id}", json=update_data, headers=headers)
