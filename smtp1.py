import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password="ezrmyoswbfdlkgac"
me='onkar.kolekar14@gmail.com'
you=''
with open('focus.txt','r') as fp:
    data=fp.readlines()
    for i in data:
        you=i
        emai_body="""
        <html><body><p>
        Hello All,
        Virus Injected successfully
        </p></body></html>
            """
        message = MIMEMultipart('alternative', None,[MIMEText (emai_body, 'html')])
        message['Subject'] = 'Test email send'
        message['From'] = me
        message['To'] = you
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(me, password)
            server.sendmail(me, you, message.as_string())
            server.quit()
            print(f'Email sent Successfully to all recipients')
        except Exception as e:
            print(f'Error in sending email: {e}')
