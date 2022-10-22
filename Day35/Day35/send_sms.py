import requests
import os
import twilio.base.exceptions
from twilio.rest import Client

# account_sid = os.environ.get("OWM_API_KEY")
account_sid = "AC799ca80647325c715a9cc65b4edc0f31"
# auth_token = os.environ.get("AUTH_TOKEN")
auth_token = "bd8c418fe486fdd2d70c16b6c502b05b"
client = Client(account_sid, auth_token)

try:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+13608001587',
        to='+989190911812'
    )
    print(message.status)
except twilio.base.exceptions.TwilioException as e:
    print(e)
