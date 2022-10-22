import requests
from twilio.rest import Client

account_sid = "AC799ca80647325c715a9cc65b4edc0f31"
auth_token = "bd8c418fe486fdd2d70c16b6c502b05b"

my_api_key = "4e3114a915eca031af22c456acba4138"
parameters = {
    "lat": 35.6892523,
    "lon": 51.3896004,
    "appid": my_api_key,
    "exclude": "current,minutely,daily"}
response = requests.get(
    "https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]
condition_code = [True for hour_data in weather_data if int(hour_data['weather'][0]['id']) < 700]
if len(condition_code) > 0:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+15017122661',
        to='+989190911812'
    )
    print(message.status)
