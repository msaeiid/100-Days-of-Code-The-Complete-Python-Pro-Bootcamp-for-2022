import requests
import os

os.environ["apikey"] = "uTeesCZ-flDA7FMm4f0U1f6Q0h0XIZVZ"
os.environ["endpoint"] = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    def __init__(self):
        self.endpoint = os.environ.get("endpoint")
        # self.headers = {
        #     "apikey": "uTeesCZ-flDA7FMm4f0U1f6Q0h0XIZVZ",  # os.environ.get("API_KEY"),
        #     "Content-Type": "application/json"
        # }
        # self.query = {
        #     "fly_from": fly_from,
        #     "date_from": date_from,
        #     "date_to": date_to
        # }
        # self.response = None

    def get_destination_code(self, city_name):
        # self.response = requests.get(url=self.endpoint, headers=self.headers, params=self.query).json()
        code = ""
        return code
