import csv
from mailchimp3 import MailChimp

# Read CSV file and extract email addresses
emails = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        email = row[10]  # Assuming email column is at index 10
        if email:
            emails.append(email)

# Create notification emails
subject = "Notification Subject"
body = "Notification Body"

# Initialize Mailchimp API client
mailchimp = MailChimp('YOUR_API_KEY')

# Send emails using Mailchimp
for email in emails:
    response = mailchimp.campaigns.create(
        data={
            'recipients': {
                'list_id': 'YOUR_LIST_ID'
            },
            'type': 'regular',
            'settings': {
                'subject_line': subject,
                'reply_to': 'your_email@example.com',
                'from_name': 'Your Name',
                'html': body
            }
        },
        headers={'content-type': 'application/json'}
    )
    print(f"Email sent to {email}. Campaign ID: {response['id']}")
