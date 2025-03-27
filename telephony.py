from twilio.rest import Client

account_sid = "twilio_sid"
auth_token = "twilio_auth_token"
twilio_client = Client(account_sid, auth_token)

call = twilio_client.calls.create(
    url="http://yourserver.com/voice-response",  # Handle call flow
    to="my_phone_number",
    from_="twilio_phone_number"
)
print("Call initiated:", call.sid)
