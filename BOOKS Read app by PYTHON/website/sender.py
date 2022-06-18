import smtplib
import os
from email.message import EmailMessage

def sender(e):
     EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
     EMAIL_PASSWORD = os.environ.get('PASSWORD')

     email = EmailMessage()
     email['Subject'] = "Welcome to the books club"
     email['From'] = EMAIL_ADDRESS
     email['To'] = e
     email.set_content("You have now joined the Fraternity book club")

     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

          smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
          smtp.send_message(email)

