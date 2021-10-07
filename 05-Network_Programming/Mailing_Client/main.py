# used to send mails from existing mailing account

import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# create or overwrite datafile with password
dataFile = open("05-Network_Programming/Mailing_Client/data.txt", "w")

email = input('Enter Your Email: ')
data = input('Enter Email Password: ')

dataFile.write(data)

dataFile.close()

# 25 = PORT
# smtp.gmail.com = Gmail SMTP for outgoing email
server = smtplib.SMTP('smtp.gmail.com', 25)

# start the server
server.ehlo()

with open('data.txt', 'r') as f:
    password = f.read

server.login(email, password)

msg = MIMEMultipart()
msg['From'] = 'Sam Oberg'
msg['To'] = 'samueloberg@hotmail.com'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# sending an image file
filename = 'me.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application' 'octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(p)

text = msg.as_string()
server.sendmail(email, 'samueloberg@hotmail.com', text)