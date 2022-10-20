import requests
import datetime as dt

# response = requests.get('http://api.open-notify.org/iss-now.json')
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

MY_LAT = 35.752127
MY_LONG = 51.573121

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
# To remove T from time
sunrise_hour = sunrise.split("T")[1].split(':')[0]
sunset_hour = sunset.split("T")[1].split(':')[0]
print(sunrise_hour)
print(sunset_hour)
time_now = dt.datetime.now()
print(time_now.hour)
