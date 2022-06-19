import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "berkelium"
TOKEN = "mytokenforpixela31"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "German Studying Graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = dt.datetime.now().strftime("%Y%m%d")

update_params = {
    "date": today,
    "quantity": input("How many minutes did you study German? ")
}

response = requests.post(graph_add_pixel_endpoint, json=update_params, headers=headers)
print(response.text)

# response = requests.delete(f"{graph_add_pixel_endpoint}/{today}", headers=headers)
# print(response.text)
