import os
from datetime import datetime
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETS_API = "https://api.sheety.co/f38d9fbf42fb4565608233e1ce994b28/myWorkouts/workouts"
GENDER = "male"
WEIGHT_KG = "63"
HEIGHT_CM = "173"
AGE = "23"

headers = {
    "x-app-id": os.getenv("NUTRITIONIX_API_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY")
}

params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_URL, json=params,
                         headers=headers)
print(response.json())

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheets_response = requests.post(url=SHEETS_API, json=sheet_inputs,
                                headers={"Authorization": os.getenv("AUTHORIZATION")})
print(sheets_response.json())
