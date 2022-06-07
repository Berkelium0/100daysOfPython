import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 39.933365  # Your latitude
MY_LONG = 32.859741  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.


def iss_in_range():
    return MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and iss_latitude >= MY_LAT - 5 <= iss_latitude <= MY_LAT + 5


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


# If the ISS is close to my current position
# and it is currently dark

def is_dark():
    return sunset <= time_now and time_now >= sunrise


while True:
    time.sleep(60)
    if iss_in_range() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("dgko31@gmail.com", "vkomkcdthltoqtpr")
            server.sendmail(from_addr="dgko31@gmail.com", to_addrs="berkeebrus@gmail.com",
                            msg=f"Subject:Look up!\n\nThe International Space Station is somewhere above you! The ISS' latitude is: {iss_latitude} and its longitute is: {iss_longitude}.")
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
