import smtplib
import keys
from string import Template
from pathlib import Path

from email.message import EmailMessage

html = Template(Path('./mail.html').read_text())
email = EmailMessage()
name = 'Butters'

email['from'] = ' runs'
email['to'] = 'anexpor@bk.ru'
email['subject'] = 'This is python sended email for myself'
email.set_content(html.substitute(name=name), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com', f'{keys.key}')
    smtp.send_message(email)
    print('Message sent')
