from twilio.rest import Client

# api security keys from twilio
# no spaces
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

call = client.messages.create(
    # number you wish to text
    to="",
    # your twilio number
    from_="",
    # message you wish to send
    body=""
)

# check the README for more details
