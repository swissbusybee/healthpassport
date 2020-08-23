# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC2030a23f808d2e9586da6434102832aa'
auth_token = '34750cfe925f5ed85f9da3108237212e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12513069978',
                     to='+41799329709'
                 )

print(message.sid)
