from twilio.rest import Client

from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = ''.join(['e be things!!:P\n' for i in range(20)])

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)


