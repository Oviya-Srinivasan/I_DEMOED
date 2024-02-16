from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = 'AC4dbad9d9f67f0d5db9cb72f77f502673'
auth_token = '24a1ad64de9caf0daa1027a9c3e8b959'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Recipient's WhatsApp number (in E.164 format)
to_phone_number = 'whatsapp:+917338788505'

# Sender's Twilio WhatsApp number
from_phone_number = 'whatsapp:+12562865679'

# URL to the PDF file
pdf_url = 'C:\\Users\\Oviya Srinivasan\\Downloads\\Doctor Medicine Generation'

# Compose the message with the PDF link
message_body = f'Here is the PDF: {pdf_url}'

# Send the WhatsApp message
message = client.messages.create(
    to=to_phone_number,
    from_=from_phone_number,
    body=message_body
)

print(f"Message sent with SID: {message.sid}")
