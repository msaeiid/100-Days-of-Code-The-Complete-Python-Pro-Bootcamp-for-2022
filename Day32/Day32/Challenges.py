import smtplib
import datetime as dt
import pandas as pd
import random as rd

sender = "sender"
receiver = "receiver"
password = "password"
smtp_address = "smtp.gmail.com"
quote = ""


def send_email():
    try:
        with smtplib.SMTP(smtp_address, 587) as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            message = f"Subject:Monday Motivation\n\n{quote}"
            connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
    except smtplib.SMTPServerDisconnected as e:
        print(f'An error happened: {e}')
    else:
        print('The positivity email sent')


def check_day():
    today = dt.datetime.now()
    weekday = today.weekday()
    return weekday == 2  # Wednesday is 2


def get_positivity_sentence():
    with open('quotes.txt', mode='r') as quote_file:
        all_quotes = quote_file.read().split('\n')
        global quote
        quote = rd.choice(all_quotes)


if check_day():
    get_positivity_sentence()
    send_email()
