
# python send emails to customers from EXCEL file with Python. Map fileds csv to html massage body
# custom provided html template

# ChatGPT
# To send emails to customers from an Excel file using Python and map CSV fields to the HTML message body, you can follow the steps outlined below:

# Install necessary packages:

# pandas: for reading data from the Excel file
# openpyxl: for working with Excel files
# smtplib: for sending emails using the Simple Mail Transfer Protocol (SMTP)
# email.mime.multipart: for creating multipart email messages
# email.mime.text: for creating plain text email message parts
# email.mime.image: for embedding images in email messages
# email.mime.base: for handling base64 encoding
# You can install these packages using pip:

# python
# Copy code
# pip install pandas openpyxl
# Prepare the HTML template:
# Create an HTML template file (template.html) that will serve as the body of the email. You can include placeholders for the dynamic data using curly braces, like {name} or {email}. Make sure to save the template file in the same directory as your Python script.

# Example template.html:

# html
# Copy code
# <html>
# <body>
  # <h1>Hello {name}!</h1>
  # <p>This is a sample email. Your email address is: {email}.</p>
# </body>
# </html>
# Read data from the Excel file:
# Use the pandas library to read the data from the Excel file into a DataFrame.

# python
# Copy code
# import pandas as pd

# # Read the Excel file into a DataFrame
# df = pd.read_excel('customers.xlsx')
# Iterate over the DataFrame and send emails:
# For each row in the DataFrame, create a personalized email message by replacing the placeholders in the HTML template with the corresponding values from the row. Then, use the smtplib library to send the email.

# python
# Copy code
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # SMTP server settings
# smtp_host = 'your_smtp_host'
# smtp_port = 587
# smtp_username = 'your_username'
# smtp_password = 'your_password'

# # Iterate over the DataFrame rows
# for index, row in df.iterrows():
    # # Read customer data from the row
    # name = row['Name']
    # email = row['Email']

    # # Load the HTML template
    # with open('template.html', 'r') as file:
        # template = file.read()

    # # Replace placeholders in the template with customer data
    # message = template.replace('{name}', name).replace('{email}', email)

    # # Create the email
    # msg = MIMEMultipart()
    # msg['From'] = 'your_email@example.com'
    # msg['To'] = email
    # msg['Subject'] = 'Your Subject'
    # msg.attach(MIMEText(message, 'html'))

    # # Send the email
    # with smtplib.SMTP(smtp_host, smtp_port) as server:
        # server.starttls()
        # server.login(smtp_username, smtp_password)
        # server.send_message(msg)
# Replace your_smtp_host, your_username, and your_password with your SMTP server details.

# Make sure to modify the 'Name' and 'Email' column names in the df.iterrows() loop to match the column names in your Excel file.

# Run the script:
# Save the Python script in the same directory as the Excel file, the HTML template, and run the script:

# python
# Copy code
# python send_emails.py
# The script will iterate over the rows in the Excel file, generate personalized emails using the HTML template, and send them to the respective customers' email addresses.

# Note: Ensure that you have the necessary permissions to send emails using your SMTP server, and make sure to handle any potential errors or exceptions that may occur during the email sending process.





# User
# create functions, mail should be compressed 
# ChatGPT
# Certainly! I can help you modify the code to include functions and compress the email attachments. Here's an updated version of the code:





import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import zipfile


def read_excel_data(file_path):
    """
    Read data from the Excel file and return a DataFrame.
    """
    df = pd.read_excel(file_path)
    return df


def create_email_message(name, email, template_file):
    """
    Create the email message by replacing placeholders in the template with customer data.
    """
    with open(template_file, 'r') as file:
        template = file.read()

    message = template.replace('{name}', name).replace('{email}', email)
    return message


def attach_files_to_email(file_paths, email_message):
    """
    Attach files to the email message.
    """
    for file_path in file_paths:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file_path, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=file_path)
        email_message.attach(part)


def send_email(smtp_host, smtp_port, smtp_username, smtp_password, sender_email, recipient_email, subject, message):
    """
    Send the email.
    """
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)


def compress_files(file_paths, output_file):
    """
    Compress files into a ZIP archive.
    """
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            zipf.write(file_path, arcname=file_path)


def send_emails_from_excel(file_path, template_file, attachment_files, smtp_host, smtp_port, smtp_username, smtp_password, sender_email, subject):
    """
    Send emails to customers from an Excel file using the provided template and attachments.
    """
    # Read data from the Excel file
    df = read_excel_data(file_path)

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        # Read customer data from the row
        name = row['Name']
        email = row['Email']

        # Create the email message
        message = create_email_message(name, email, template_file)

        # Create a compressed attachment
        compressed_attachment = f'{name}_attachments.zip'
        compress_files(attachment_files, compressed_attachment)

        # Attach the compressed file to the email
        email_message = MIMEMultipart()
        email_message.attach(MIMEText(message, 'html'))
        attach_files_to_email([compressed_attachment], email_message)

        # Send the email
        send_email(smtp_host, smtp_port, smtp_username, smtp_password, sender_email, email, subject, email_message.as_string())

        # Delete the compressed file
        zipf.close()
        del zipf


# SMTP server settings
smtp_host = 'your_smtp_host'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'
sender_email = 'your_email@example.com'
subject = 'Your Subject'

# File paths
excel_file = 'customers.xlsx'
template_file = 'template.html'
attachment_files = ['file1.txt', 'file2.txt']

# Send emails
send_emails_from_excel(excel_file, template_file, attachment_files, smtp_host, smtp_port, smtp_username, smtp_password, sender_email, subject)
