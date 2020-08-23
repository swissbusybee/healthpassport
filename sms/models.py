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
    # if self.result < 70:

        account_sid = 'AC2030a23f808d2e9586da6434102832aa'
        auth_token = '34750cfe925f5ed85f9da3108237212e'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="It is time for your vaccination",
                            from_='+12513069978',
                            to='+41799329709'
                        )

        print(message.sid)
        return super().save(*args, **kwargs)