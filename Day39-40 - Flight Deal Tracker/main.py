# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
gsheet = DataManager()
notification_manager = NotificationManager()

gsheet.printData()
data = gsheet.getData()["prices"]
message = "Your cheap flight list is as follows: "

for row in data:
    if row['iataCode'] == "":
        row["iataCode"] = flight_search.get_iata_values(row["city"])
        gsheet.writeData(row["id"], row)

    search_result = flight_search.search_flights(row["iataCode"], row["lowestPrice"])
    print(search_result)
    try:
        search_result["data"][0]
    except:
        pass
    else:
        message += f"*Only {search_result['data'][0]['price']} euros to fly from {search_result['data'][0]['cityFrom']}-{search_result['data'][0]['cityCodeFrom']} to {search_result['data'][0]['cityTo']}-{search_result['data'][0]['cityCodeTo']}, from {search_result['data'][0]['route'][0]['local_departure'].split('T')[0]} to {search_result['data'][0]['route'][1]['local_departure'].split('T')[0]}. \nq"

notification_manager.send_email(str(message.encode('utf-8')))
