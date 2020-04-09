#SOURCED FROM: https://realpython.com/python-send-email/
import smtplib, ssl
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
    message = """\
    Subject: Snapshot taken!

    PiSecurity has taken a snapshot!
    You can delete this from the app if you wish.

    <img src='https://puu.sh/Fvs83/9d9c6852b1.png'>
    
    """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__== "__main__":
    SendEmailNotification("https://puu.sh/Fvs83/9d9c6852b1.png".encode('utf-8'))