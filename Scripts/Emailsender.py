from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'meghshamjambhulkar@gmail.com'
password = 'nobiyyykqndegvif'
email_receiver = 'meghshamjambhulkar01@gmail.com'

subject = 'Test Email'
body = """
Jai Ganesh Email
"""
em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver 
em['Subject'] =subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',587,context=context) as smtp :
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email Sent Successfully")

