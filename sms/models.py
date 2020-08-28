import os
from django.db import models
from twilio.rest import Client

# Create your models here.
class NotifyUser(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure

    # example
        if self.result < 70:

            account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
            auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
            to_number = os.environ.get('MY_PHONE_NUMBER')

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                        body="Current result is bad",
                        # temp number works with temp sid
                        from_='+12513069978',
                        to_number='MY_PHONE_NUMBER'
                )

            print(message.sid)
        return super().save(*args, **kwargs)