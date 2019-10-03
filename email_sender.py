

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Your Name Here'
email['to'] = 'InsertAEmailAddressHere'
email['subject'] = 'Insert subject message here'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Insert your email address here', 'enter your passord here')
    smtp.send_message(email)
    print('all good')