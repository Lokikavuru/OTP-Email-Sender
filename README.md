# OTP Email Sender

This script sends OTPs (One-Time Passwords) to multiple recipients via email. The OTPs include letters, numbers, and symbols to enhance security.

## Features
- Sends OTPs to multiple recipients
- Generates secure OTPs with letters, numbers, and symbols
- Uses Gmail SMTP server for email delivery
- Verifies OTP entered by users

## Prerequisites
- Python installed on your system
- A valid Gmail account with **Less Secure Apps Access enabled** (if required)
- Required Python libraries: `smtplib`, `random`, `string`, `email`

## Installation
1. Clone or download this script.
2. Install Python if not already installed.
3. Modify the `server.login()` section with your email credentials.
4. Ensure the necessary Python libraries are installed.

## Usage
1. Run the script:
   ```bash
   python send_otp_multiple.py
   ```
2. Enter the email addresses (comma-separated) when prompted.
3. Each recipient will receive a unique OTP via email.
4. Enter the received OTP for verification.

## Security Notice
- Do **not** hardcode sensitive credentials in the script. Use environment variables or a config file instead.
- Enable **App Passwords** if Gmail blocks login due to security reasons.

## Author
Lokesh Kumar Kavuru

## License
This project is for educational purposes only.

