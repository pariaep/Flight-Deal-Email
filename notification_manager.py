import smtplib

from twilio.rest import Client
import smtplib
T_SID = "AC02a1ccaaed24561bb0fad233c86eb10f"
T_AUTH_TOKEN = "54ae3602df514b21b70e287df66f756d"

class NotificationManager:
    def __init__(self):
        self.client = Client(T_SID, T_AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages.create(from_="+18773959116", to="+14158029880", body=message)
        print(message.sid)

    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="pariatest2023@yahoo.com", password="Mytest2023")
            for email in emails:
                connection.sendmail(from_addr="pariatest2023@yahoo.com", to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))
