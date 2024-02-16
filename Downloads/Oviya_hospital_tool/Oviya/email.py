import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Define your email and password
email_address = 'oviyasrinivasan20@gmail.com'
email_password = 'oviya@05012004'

# Create an SMTP server connection
try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(email_address, email_password)
except Exception as e:
    print(f'Failed to connect to the SMTP server: {e}')
    exit()

# Create the email message
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = 'recipient_email@example.com'
msg['Subject'] = 'Prescription'

# Add text content to the email
message_text = 'Please find the prescription attached.'
msg.attach(MIMEText(message_text, 'plain'))

# Attach the prescription file (PDF, image, etc.)
with open('prescription.pdf', 'rb') as file:
    attachment = MIMEApplication(file.read(), _subtype="pdf")
    attachment.add_header('Content-Disposition', 'attachment', filename='prescription.pdf')
    msg.attach(attachment)

# Send the email
try:
    smtp_server.sendmail(email_address, 'recipient_email@example.com', msg.as_string())
    print('Email sent successfully')
except Exception as e:
    print(f'Failed to send email: {e}')

# Close the SMTP server connection
smtp_server.quit()
