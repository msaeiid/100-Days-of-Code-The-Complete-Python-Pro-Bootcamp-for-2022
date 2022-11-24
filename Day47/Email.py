import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_ADDRESS = "smtp.mail.yahoo.com"
PORT = "465"
SENDER_ADDRESS = "karbaschian_saeed@yahoo.com"
SENDER_PASSWORD = "77002783Sas"
RECEIVER_ADDRESS = "karbaschian_saeed@yahoo.com"


class Email:
    def __init__(self):
        self.sender_address = SENDER_ADDRESS
        self.sender_pass = SENDER_PASSWORD
        self.receiver_address = RECEIVER_ADDRESS
        self.message = MIMEMultipart()
        self.message['From'] = self.sender_address
        self.message['To'] = self.receiver_address

    def send(self, title: str, price: float, url: str):
        print('Try to send email')
        self.message['Subject'] = title
        mail_content = f'''
        Hello,
        {title} price is below {price}
        here is the product url: {url}
        '''
        self.message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP(SMTP_ADDRESS, PORT)
        session.starttls()
        session.login(self.sender_address, self.sender_pass)
        text = self.message.as_string()
        session.sendmail(self.sender_address, self.receiver_address, text)
        session.quit()
        print(f"Mail Sent")
