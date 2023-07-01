import smtplib
from smtplib import SMTP
sender = 'onkar.@gmail.com'
receivers = 'rppat302@gmail.com'

message = """From: From Person <onkar.klekar14@gmail.com.com>
To: To Person <rppatil302@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except smtplib.SMTPException as e:
   print("Error:",e)