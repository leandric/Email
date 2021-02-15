import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

email_from = 'bhetamed@gmail.com'
email_pass = ''
email_smtp_server = 'smtp.gmail.com'

destination = ['leandro@chemist.com']


text = open('texto.html').read()

subject = 'teste'

msg = MIMEMultipart()
msg['From'] = email_from
msg['subject'] = subject
msg_text = MIMEText(text, 'html')
msg.attach(msg_text)
print(msg.as_string())

try:
    smtp = smtplib.SMTP(email_smtp_server, 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_from, email_pass)
    smtp.sendmail(email_from, ','.join(destination), msg.as_string())
    smtp.quit()
    print('email enviado')
except Exception as Error:
    print(f'Falha ao enviar: {Error}')
