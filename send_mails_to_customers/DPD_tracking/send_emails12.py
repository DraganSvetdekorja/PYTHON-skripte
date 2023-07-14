import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the SMTP server
    smtp_server = 'svetdekorja.si'
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


def send_emails(csv_file, template_file, sender_email, sender_password):
    


    with open(csv_file, 'r') as file:
		fieldnames = ['customer_name', 'customer_name2', 'customer_address', 'customer_post', 'customer_city',
                  'customer_telephon', 'customer_email', 'customer_tracking_number', 'customer_date']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        for row in reader:
            # Extract fields from the CSV row
            customer_email = row['customer_email']
            customer_name = row['customer_name']
            customer_address = row['customer_address']
            customer_post = row['customer_post']
            customer_city = row['customer_city']
            customer_telephon = row['customer_telephon']
            customer_tracking_number = row['customer_tracking_number']
            tracking_link = 'https://www.dpdgroup.com/si/mydpd/my-parcels/incoming?parcelNumber='

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
            }

        # Generate the HTML message body using the template
        message_body = generate_message_body(template_file, placeholders)

        # Send the email
        subject = 'Svetdekorja.si - Vaše naročilo je bilo odposlano. Sledite vašo pošiljko'
        send_email(sender_email, sender_password, customer_email, subject, message_body)

# Example usage
csv_file = 'DPD_IZVOZ3.csv'
template_file = 'email_body5.html'
sender_email = 'dragan@svetdekorja.si'
sender_password = '@IcFW@v-ZD94'

send_emails(csv_file, template_file, sender_email, sender_password)
