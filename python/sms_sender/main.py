from twilio.rest import Client

account_sid = 'AC0dc1a615c920504c8b47fd656d7046c9'
auth_token = 'a6d4bef07f040ae73aff0681d65876a8'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12567332345',
    body='Python doing it!',
    to='+79161217440'
)

print(message.sid)
