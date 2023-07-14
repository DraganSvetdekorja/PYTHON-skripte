import pandas as pd
from jinja2 import Environment, FileSystemLoader
import yagmail

# Read CSV file
df = pd.read_csv('customers.csv')

# Load the email template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('email_template.html')

# SMTP settings for your email provider
email_sender = 'your_email@example.com'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_email_password'

# Iterate over each row in the CSV
for _, row in df.iterrows():
    name = row['name']
    email = row['email']
    tracking_number = 'ABC123'  # Replace with actual tracking number
    tracking_link = 'https://example.com/tracking'  # Replace with actual tracking URL

    # Render the email template with customer-specific data
    email_body = template.render(name=name, tracking_number=tracking_number, tracking_link=tracking_link)

    # Send the email
    yag = yagmail.SMTP(smtp_username, smtp_password, smtp_server, smtp_port)
    yag.send(to=email, subject='Order Shipment', contents=email_body, headers={'X-Priority': '1'})
    yag.close()
