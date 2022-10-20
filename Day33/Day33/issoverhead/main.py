import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 22.6570  # Your latitude
MY_LONG = -35.8739  # Your longitude
MY_EMAIL = "email"
MY_PASSWORD = "password"


# If the ISS is close to my current position
def is_iis_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)


# and it is currently dark
def is_night():
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
    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour <= sunrise


# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(5)
    if is_iis_over_head() and is_night():
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                    msg="Subject:LOOK UP\n\n The ISS is above you in the sky!")
        except:
            print('LOOK UP SKY!\n I tried to send you email but it was not successful!')
