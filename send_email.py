import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 456
    context = ssl.create_default_context()
    username = "asmindbingol@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "asmindbingol@hotmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

