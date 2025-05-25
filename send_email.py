import smtplib
from email.mime.text import MIMEText
import os

def send_email(subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    your_gmail = os.environ["GMAIL_ADDRESS"]
    your_gmail_app_password = os.environ["GMAIL_APP_PASSWORD"]

    to_email = your_gmail

    msg = MIMEText(body)
    msg["From"] = your_gmail
    msg["To"] = to_email
    msg["Subject"] = subject

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(your_gmail, your_gmail_app_password)
        server.sendmail(your_gmail, [to_email], msg.as_string())
