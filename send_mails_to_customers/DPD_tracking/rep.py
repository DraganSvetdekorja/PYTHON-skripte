import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the SMTP server
    smtp_server = 'smtp.example.com'
    smtp_port = 587
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
csv_file = 'customer_data.csv'

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract fields from the CSV row
        customer_name = row['Name']
        customer_email = row['Email']
        # ... map other fields as needed

        # Define the placeholders and their values for the HTML template
        placeholders = {
            'customer_name': customer_name,
            # ... add other placeholders and their values
        }

        # Generate the HTML message body using the template
        template_file = 'email_template.html'
        message_body = generate_message_body(template_file, placeholders)

        # Send the email
        sender_email = 'your_email@example.com'
        sender_password = 'your_email_password'
        subject = 'Your Subject'
        send_email(sender_email, sender_password, customer_email, subject, message_body)
