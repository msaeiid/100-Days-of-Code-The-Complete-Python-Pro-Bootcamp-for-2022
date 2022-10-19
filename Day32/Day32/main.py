##################### Extra Hard Starting Project ######################
import smtplib

import pandas as pd
import datetime as dt
import random as rd
import smtplib as s

# 1. Update the birthdays.csv
# DONE

# 2. Check if today matches a birthday in the birthdays.csv
today_birthday_list = []
MY_NAME = "Saeid"
sender = 'my_email@gmail.com'
receiver = 'receiver_email@gmail.com'
password = "password"
smtp_address = 'smtp.gmail.com'


def check_today_birthday():
    global today_birthday_list
    today = dt.datetime.now()
    today_tuple = (today.month, today.day)
    data = pd.read_csv('birthdays.csv')
    birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
    today_birthday_list = [value for key, value in birthday_dict.items() if key == today_tuple]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def create_birthday_template(name: str):
    random_template = rd.randint(1, 3)
    with open(f'letter_templates/letter_{random_template}.txt', mode='r') as template_file:
        template = template_file.read()
        return template.replace('[NAME]', name)


# 4. Send the letter generated in step 3 to that person's email address.
def send_email():
    with s.SMTP(smtp_address, 587) as connection:
        connection.starttls()
        try:
            connection.login(user=sender, password=password)
        except smtplib.SMTPAuthenticationError as e:
            print(f"An error happened {e}.")
            for person in today_birthday_list:
                template = create_birthday_template(person['name'])
                print(f"{template}\n{person['email']}")
                print('######################')
        else:
            for person in today_birthday_list:
                template = create_birthday_template(person['name'])
                connection.sendmail(from_addr=sender, to_addrs=receiver,
                                    msg=f"Subject:Happy birthday from {MY_NAME} to dear {person['name']}\n\n{template}")
        finally:
            print(f'today {len(today_birthday_list)} sent.')


check_today_birthday()
if len(today_birthday_list) > 0:
    send_email()
else:
    print("Today you don't need to send any email!")
