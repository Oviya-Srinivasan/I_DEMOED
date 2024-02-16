import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define your email and password
email_address = 'rvvarsha2003@gmail.com'
email_password = 'varsharavi03'

# Create an SMTP server connection
try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(email_address, email_password)
except Exception as e:
    print(f'Failed to connect to the SMTP server: {e}')
    exit()

# Define email content with placeholders for personalization
customer_name = 'John Doe'
prescribed_medicines = ['Medicine A', 'Medicine B']
remaining_medicines = ['Medicine C', 'Medicine D']

subject = 'Medication Purchase Reminder'
message_text = f"Dear {customer_name}, please complete your medication purchase for {', '.join(prescribed_medicines)} and consider adding {', '.join(remaining_medicines)} to your order. Visit our website for more details."

# Create a MIMEText object to represent the email
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = 'customer_email@example.com'
msg['Subject'] = subject

# Attach the email message
msg.attach(MIMEText(message_text, 'plain'))

# Send the email
try:
    smtp_server.sendmail(email_address, 'preethabalaji2905@gmail.com', msg.as_string())
    print('Email sent successfully')
except Exception as e:
    print(f'Failed to send email: {e}')

# Close the SMTP server connection
smtp_server.quit()
