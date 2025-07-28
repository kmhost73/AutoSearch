import smtplib
import os
from email.message import EmailMessage

def send_email_alert(listing_count):
    msg = EmailMessage()
    msg["Subject"] = f"New Listings Found: {listing_count}"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("EMAIL_TO")
    msg.set_content(f"{listing_count} new listings have been added to your spreadsheet.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)

def test_smtp_email():
    msg = EmailMessage()
    msg["Subject"] = "Test Email from AutoSearch"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("EMAIL_TO")
    msg.set_content("This is a test email to verify SMTP configuration.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)
