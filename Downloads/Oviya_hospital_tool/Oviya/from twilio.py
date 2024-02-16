from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = 'AC4dbad9d9f67f0d5db9cb72f77f502673'
auth_token = '24a1ad64de9caf0daa1027a9c3e8b959'

# Create a Twilio client
client = Client( "AC4dbad9d9f67f0d5db9cb72f77f502673" , "24a1ad64de9caf0daa1027a9c3e8b959" )

# Recipient phone number (in E.164 format)
to_phone_number = '+919363077356'  # Replace with the recipient's phone number

# Sender phone number (must be a Twilio phone number)
from_phone_number = '+12562865679'

# Message content
message_body = 'Medicines to be packed are'

# Send the SMS message
message = client.messages.create(
    to= +919363077356,
    from_=+12562865679,
    body=message_body
)

print(f"Message sent with SID: {message.sid}")
