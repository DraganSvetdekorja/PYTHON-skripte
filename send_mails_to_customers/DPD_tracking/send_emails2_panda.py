import pandas as pd
from jinja2 import Environment, FileSystemLoader
import yagmail



cols = ['DATUM', 'SIFRA_KUPCA', 'TIP_PAKETA', 'TEZA', 'ODKUPNINA', 'IME', 'PRIIMEK', 'NASLOV1', 'POSTA', 'KRAJ', 'TELEFON', 'EMAIL', 'PL_STEVILKA', 'NASLOV2']
# Read CSV file
#df = pd.read_csv('DPD_IZVOZ.csv', header=None, names=cols)
#df = pd.read_csv('DPD_IZVOZ.csv', header=None, names=cols, usecols=[1,4,5,6,7,8,9,10,11,12])
df = pd.read_csv('DPD_IZVOZ2.csv', header=None, usecols=[1,4,5,6,7,8,9,10,11,12])

# DATUM	SIFRA_KUPCA	TIP_PAKETA	TEZA	ODKUPNINA	IME	PRIIMEK	NASLOV1	POSTA	KRAJ	TELEFON	EMAIL	PL_STEVILKA	NASLOV2

print(df)

# Load the email template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('email_template2.html')

# SMTP settings for your email provider
email_sender = 'dragan@svetdekorja.si'
smtp_server = 'sh4.neoserv.si'
smtp_port = 465
smtp_username = 'dragan@svetdekorja.si'
smtp_password = '@IcFW@v-ZD94'

# # Iterate over each row in the CSV
# for _, row in df.iterrows():
    # name = row['name']
    # email = row['email']
    # tracking_number = 'ABC123'  # Replace with actual tracking number
    # tracking_link = 'https://example.com/tracking'  # Replace with actual tracking URL

    # # Render the email template with customer-specific data
    # email_body = template.render(name=name, tracking_number=tracking_number, tracking_link=tracking_link)

    # # Send the email
    # yag = yagmail.SMTP(smtp_username, smtp_password, smtp_server, smtp_port)
    # yag.send(to=email, subject='Order Shipment', contents=email_body, headers={'X-Priority': '1'})
    # yag.close()

for _, row in df.iterrows():	
	name = row[5]
	email = row[11]
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


		# email_body = template.render(name=name, tracking_number=tracking_number, tracking_link=tracking_link)

	# Send the email

	email_body = template.render(name=name, email=email, naslov1=naslov1, posta=posta, kraj=kraj, telefon=telefon, tracking_number=tracking_number, tracking_link=tracking_link)
	yag = yagmail.SMTP(smtp_username, smtp_password, smtp_server, smtp_port)
	yag.send(to=email, subject='Svetdekorja.si - Vaše spletno naročilo je bilo odposlano', contents=email_body, headers={'X-Priority': '1'})
	yag.close()
