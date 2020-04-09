#SOURCED FROM: https://realpython.com/python-send-email/
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import env

def SendEmailNotification(img_url):
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = EMAIL_USER
    receiver_email = "angelo.josey@gmail.com" #pull this from the db later
    password = EMAIL_PASS
    message = MIMEMultipart("alternative")
    message["Subject"] = "PiSecurity"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = f"""\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="https://puu.sh/Fvs83/9d9c6852b1.png">Real Python</a>
        <img src="{img_url}">
        has many great tutorials.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

if __name__== "__main__":
    SendEmailNotification("https://puu.sh/Fvs83/9d9c6852b1.png")