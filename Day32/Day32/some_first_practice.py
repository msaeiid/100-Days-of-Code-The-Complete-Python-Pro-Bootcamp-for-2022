# import smtplib
#
# sender = "XXX"
# password = "XXX"
# receiver = "XXX"
# message = "Subject:this is an email from python\n\nThis is the body of the email."
#
# try:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()  # to secure connection
#         connection.login(user=sender, password=password)
#         connection.sendmail(from_addr=sender,
#                             to_addrs=receiver,
#                             msg=message)
# except smtplib.SMTPException as e:
#     print(e)
# else:
#     print("message successfully sent")

import datetime as dt

now = dt.datetime.now()
print(now.weekday())
birthday = dt.datetime(year=1987, month=3, day=21, hour=22, minute=23, second=45)
print(birthday)
