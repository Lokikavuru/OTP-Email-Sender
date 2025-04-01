import smtplib
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Generate a secure OTP with letters, numbers, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# List of recipients
recipients = input("Enter comma-separated email IDs: ").split(',')

otps = {}

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("lokeshkumarkavuru@gmail.com", "rfnq ihuw wlky hipr")

for recipient in recipients:
    otp = ''.join(random.choice(characters) for _ in range(8))
    otps[recipient.strip()] = otp
    
    body = f"Your OTP for Verification is: {otp}"
    msg = MIMEMultipart()
    msg["From"] = "saivardhan@codegnan.com"
    msg["To"] = recipient.strip()
    msg["Subject"] = "OTP For Validation"
    msg.attach(MIMEText(body, 'plain'))
    
    server.send_message(msg)
    print(f"OTP sent to {recipient.strip()}")

server.quit()

# Verification process
for recipient in recipients:
    cotp = input(f"Enter OTP received for {recipient.strip()}: ")
    if otps[recipient.strip()] == cotp:
        print(f"OTP Verification Success for {recipient.strip()}")
    else:
        print(f"Invalid OTP for {recipient.strip()}")
