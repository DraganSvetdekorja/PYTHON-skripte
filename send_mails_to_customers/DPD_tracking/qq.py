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

# Read the CSV file
csv_file = 'customer_data.csv'

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract fields from the CSV row
        customer_name = row['Name']
        customer_email = row['Email']
        # ... map other fields as needed

        # Compose the HTML message body
        message_body = f'''
            <html>
                <head></head>
                <body>
                    <h1>Hello {customer_name}</h1>
                    <p>This is the body of the email.</p>
                    <!-- You can include other HTML elements here -->
                </body>
            </html>
        '''

        # Send the email
        sender_email = 'your_email@example.com'
        sender_password = 'your_email_password'
        subject = 'Your Subject'
        send_email(sender_email, sender_password, customer_email, subject, message_body)
