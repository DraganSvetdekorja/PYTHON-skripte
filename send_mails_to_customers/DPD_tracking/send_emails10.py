import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, body):
	# Set up the SMTP server
	smtp_server = 'sh4.neoserv.si'
	smtp_port = 465
	smtp_username = sender_email
	smtp_password = sender_password

	server = smtplib.SMTP(smtp_server, smtp_port)
	server.starttls()
	server.login(smtp_username, smtp_password)

	# Create a multipart message
	message = MIMEMultipart()
	message['From'] = sender_email
	message['To'] = receiver_email
	message['Subject'] = subject

	# Add HTML body to the message
	message.attach(MIMEText(body, 'html'))

	# Send the email
	server.send_message(message)
	server.quit()

def generate_message_body(template_file, placeholders):
	with open(template_file, 'r') as file:
		template = file.read()

	# Replace placeholders in the template with corresponding values
	message_body = template.format(**placeholders)
	return message_body

# Read the CSV file
csv_file = 'DPD_IZVOZ2.csv'

with open(csv_file, 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		# Extract fields from the CSV row
		customer_name = row[5]
		customer_email = row[11]
		customer_address = str(row[7])
		customer_post = str(row[8])
		customer_city = str(row[9])
		customer_telephon = str(row[10])
		customer_tracking_number = str(row[12])  # Replace with actual tracking number
		tracking_link = 'https://www.dpdgroup.com/si/mydpd/my-parcels/incoming?parcelNumber='  # Replace with actual tracking URL
		# ... map other fields as needed

		# Define the placeholders and their values for the HTML template
		placeholders = {
			'customer_name': customer_name,
			'customer_email': customer_email,
			'customer_address': customer_address,
			'customer_post': customer_post,
			'customer_city': customer_city,
			'customer_telephon': customer_telephon,
			'customer_tracking_number': customer_tracking_number,
			'tracking_link': tracking_link,
																		
			# ... add other placeholders and their values
		}

		# Generate the HTML message body using the template
		template_file = 'email_body5.html'
		message_body = generate_message_body(template_file, placeholders)

		# Send the email
		sender_email = 'dragan@svetdekorja.si'
		sender_password = '@IcFW@v-ZD94'
		subject = 'Svetdekorja.si - Vaše naročilo je bilo odposlano. Sledite vašo pošiljko'
		send_email(sender_email, sender_password, customer_email, subject, message_body)
