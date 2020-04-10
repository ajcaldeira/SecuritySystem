#SOURCED FROM: https://realpython.com/python-send-email/
#ADDITIONAL INFORMATION: https://hostpresto.com/community/tutorials/how-to-send-email-from-the-command-line-with-msmtp-and-mutt/
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import env
def SetVars():
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
def SendEmailNotification(img_url,time_now):
    SetVars()
    # Create the plain-text and HTML version of your message
    text = f"""\
    Sent From PiSecurity at {time_now}"""
    html = f"""\
    <html>
    <body>
        <p>PiSecurity has taken a screenshot! <br>
        You can view or delete this in the app. <b4>
        <img src="{img_url}">
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

def SendEmailAlarm(time_now):
    SetVars()
    # Create the plain-text and HTML version of your message
    text = f"""\
    Sent From PiSecurity at {time_now}"""
    html = f"""\
    <html>
    <body>
        <p>PiSecurity detected that someone or something has gotten too close!
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