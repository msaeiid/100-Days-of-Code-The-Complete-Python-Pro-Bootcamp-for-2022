# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# FlightSearch(fly_from="FRA", date_from="11/01/2022", date_to="05/01/2023")
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

# Fetch data from sheety
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

#
# flight_search = FlightSearch(fly_from="FRA", date_from="11/01/2022", date_to="05/01/2023")
# flight_search.get_destination_code()
# pprint(flight_search.response)


## unfinished because my ip address blocked and this error {'errors': [{'detail': 'Monthly quota has been reached. Please upgrade to continue making requests.'}]}
