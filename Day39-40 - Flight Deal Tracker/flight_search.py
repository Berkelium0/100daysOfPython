import os
from datetime import datetime, timedelta

import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com"
        self.header = {"apikey": os.getenv("TEQUILA_API_KEY")}

    def get_iata_values(self, city_name):
        params = {"term": city_name}
        return requests.get(url=f"{self.url}/locations/query", params=params,
                            headers=self.header).json()["locations"][0]["code"]

    def search_flights(self, city_iata, lowest_price):
        tomorrow_datetime = datetime.now() + timedelta(days=1)
        six_month_datetime = datetime.now() + timedelta(days=180)
        params = {
            "fly_from": "NUE",
            "fly_to": city_iata,
            "date_from": tomorrow_datetime.strftime("%d/%m/%Y"),
            "date_to": six_month_datetime.strftime("%d/%m/%Y"),
            "curr": "EUR",
            "price_to": lowest_price,
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 1,
            "limit": 1,
        }
        return requests.get(url=f"{self.url}/v2/search", params=params,
                            headers=self.header).json()
