import smtplib

from twilio.rest import Client
import smtplib
T_SID = "YOUR-SID"
T_AUTH_TOKEN = "YOUR-TOKEN"

class NotificationManager:
    def __init__(self):
        self.client = Client(T_SID, T_AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages.create(from_="+18773959116", to="YOUR_NUMBER", body=message)
        print(message.sid)

    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="YOUR_EMAIL", password="YOUR_PASS")
            for email in emails:
                connection.sendmail(from_addr="YOUR_EMAIL", to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))
