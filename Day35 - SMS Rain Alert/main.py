import requests
import os
from twilio.rest import Client

account_sid = 'AC8fe855147f98243b60c131449a3245eb'
auth_token = '8ec04f87127cfb7dc70985f44b8657ac'

parameters = {"key": "c3aea67e4ad244a8a16122601221006", "q": "Ankara", "days": 1, "aqi": "no", "alerts": "no"}
response = requests.get("http://api.weatherapi.com/v1/forecast.json", params=parameters)
conditions = ["rain", "drizzle", "sleet", "pellets", "snow","sunny"]
will_rain = False

for x in range(0, 12):
    if any(word in response.json()["forecast"]["forecastday"][0]["hour"][x]["condition"]["text"].lower() for word in
           conditions):
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its rainy today, Dont forget your umbrella!☂",
        from_="+19124937864",
        to="+905357992024"
    )
    print(message.status)
