import requests
import os

os.environ["SHEETY_ENDPOINT"] = "https://api.sheety.co/dcb9fe8d3777fe4163a80cbba2455531/flightDeals/prices"
os.environ["Authorization"] = "Basic ZGFzZnNkZmRzZjpkZmRzdmdkc2Zz"


class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
        self.Authorization = os.environ.get("Authorization")
        self.headers = {
            "Authorization": self.Authorization
        }
        self.data = None
        self.destination_data = None

    def get_destination_data(self):
        self.data = requests.get(url=self.SHEETY_ENDPOINT, headers=self.headers).json()
        print(self.data)
        self.destination_data = self.data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            resource = requests.put(
                url=f"{self.SHEETY_ENDPOINT}/{city['id']}",
                json=new_data)
