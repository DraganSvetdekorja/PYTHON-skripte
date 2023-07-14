# import the necessary components first
import pandas as pd
from jinja2 import Environment, FileSystemLoader

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465 
smtp_server = "sh4.neoserv.si'"
login = "dragan@svetdekorja.si" # paste your login generated by Mailtrap
password = "@IcFW@v-ZD94" # paste your password generated by Mailtrap

sender_email = "dragan@svetdekorja.si"
#





cols = ['DATUM', 'SIFRA_KUPCA', 'TIP_PAKETA', 'TEZA', 'ODKUPNINA', 'IME', 'PRIIMEK', 'NASLOV1', 'POSTA', 'KRAJ', 'TELEFON', 'EMAIL', 'PL_STEVILKA', 'NASLOV2']
# Read CSV file
#df = pd.read_csv('DPD_IZVOZ.csv', header=None, names=cols)
#df = pd.read_csv('DPD_IZVOZ.csv', header=None, names=cols, usecols=[1,4,5,6,7,8,9,10,11,12])
df = pd.read_csv('DPD_IZVOZ2.csv', header=None, usecols=[1,4,5,6,7,8,9,10,11,12])

# DATUM	SIFRA_KUPCA	TIP_PAKETA	TEZA	ODKUPNINA	IME	PRIIMEK	NASLOV1	POSTA	KRAJ	TELEFON	EMAIL	PL_STEVILKA	NASLOV2

print(df)

# Load the email template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('email_body4.html')

# write the text/plain part
text = """\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!"""

# write the HTML part
html = """\
<html>
  <body>
    <p>Hi,<br>
       Check out the new post on the Mailtrap blog:</p>
    <p><a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p>
    <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p>
  </body>
</html>
"""

# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# send your email
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

print('Sent')






for _, row in df.iterrows():	
	name = row[5]
	receiver_email = row[11]
	#naslov = row[8] + ' ' + row[9] + ' ' +  row[10] + ' ' +row[11]

	naslov1 = str(row[7])
	posta = str(row[8])
	kraj = str(row[9])
	telefon = str(row[10])
	#telefon = row[11]
	#naslov = naslov1 + ' ' + posta + '' + kraj + telefon)


	tracking_number = str(row[12])  # Replace with actual tracking number
	tracking_link = 'https://www.dpdgroup.com/si/mydpd/my-parcels/incoming?parcelNumber='  # Replace with actual tracking URL

	# print(str(name))
	# print(email)
	# print(tracking_number)
	# print(naslov1)
	# print(posta)
	# print(kraj)
	# print(telefon)	
	# print(naslov)	
	# print()


	 #email_body = template.render(name=name, tracking_number=tracking_number, tracking_link=tracking_link)

	# Send the email

	email_body = template.render(name=name, email=email, naslov1=naslov1, posta=posta, kraj=kraj, telefon=telefon, tracking_number=tracking_number, tracking_link=tracking_link)
	
	
	message = MIMEMultipart("alternative")
	message["Subject"] = "Svetdekorja.si - Vaše naročilo je bilo odposlano. Sledite vašo pošiljko"
	message["From"] = sender_email
	message["To"] = receiver_email
	
	
	part1 = MIMEText(text, "plain")
	part2 = MIMEText(email_body, "html")
	message.attach(part1)
	message.attach(part2)
	
	
	with smtplib.SMTP(smtp_server, 465) as server:
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
	
	
	yag = yagmail.SMTP(smtp_username, smtp_password, smtp_server, smtp_port)
	yag.send(to=email, subject='Svetdekorja.si - Vaše naročilo je bilo odposlano. Sledite vašo pošiljko', contents=email_body, headers={'X-Priority': '1'})
	yag.close()
