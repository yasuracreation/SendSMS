# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC2cb8fc1ee8dfd1e6a70a1a8dfde65326'
auth_token = 'ed3bfe00a74926d61833473b19bc2f93'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13132652861',
                     to='+94711526716'
                 )

print(message.sid)