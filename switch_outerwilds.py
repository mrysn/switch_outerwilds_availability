import requests

from bs4 import BeautifulSoup
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time
from pathlib import Path
now = datetime.datetime.now()
epoch = time.time()
content = ""

url = "https://www.nintendo.com/games/detail/outer-wilds-switch/"
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

product = soup.find('h1', class_="h2 game-title").get_text()
availability = soup.find('div', class_="availability").get_text()

status = "TBD"

if availability != None and status in availability:
    print(product.strip(), "on Switch - status: sad times, still TBD")
    content = "Outer Wilds is still TBD, I will recheck tomorrow"
else:
    print(product.strip(), "on Switch - status: OMFDAYS IT IS AVAILABLE!")
    content = "Outer Wilds is now available to buy! GO GO GO!"

print('Composing email...')

SERVER = Path('./.secret.server').read_text()
PORT = 587
FROM = Path('./.secret.from').read_text()
TO = Path('./.secret.to').read_text()
PASS = Path('./.secret.pass').read_text()

msg = MIMEMultipart()

msg['Subject'] = 'OUTER WILDS on NINTENDO SWITCH' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' [' + str(epoch) + ']'
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent.')

server.quit()

print("All done. Bye.")