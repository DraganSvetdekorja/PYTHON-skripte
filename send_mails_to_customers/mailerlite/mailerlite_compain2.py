import pandas as pd
import requests
import json

# Read data from Excel file
excel_file = 'products.xlsx'
df = pd.read_excel(excel_file)

# Prepare data for MailerLite API
api_key = 'YOUR_API_KEY'
campaign_id = 'YOUR_CAMPAIGN_ID'

product_data = []
for _, row in df.iterrows():
    product = {
        'name': row['Product Name'],
        'description': row['Product Description'],
        'price': row['Price'],
        'image': row['Image URL']
    }
    product_data.append(product)

# Get the template content from MailerLite API
template_id = 'YOUR_TEMPLATE_ID'
api_url = f'https://api.mailerlite.com/api/v2/templates/{template_id}'
headers = {'Content-Type': 'application/json', 'X-MailerLite-ApiKey': api_key}

response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    template_content = json.loads(response.text)
    html_content = template_content['html']
else:
    print(f'Error: {response.text}')
    exit()

# Replace placeholders in the template with product data
for product in product_data:
    html_content = html_content.replace('{Product Name}', product['name'])
    html_content = html_content.replace('{Product Description}', product['description'])
    html_content = html_content.replace('{Price}', str(product['price']))
    html_content = html_content.replace('{Image URL}', product['image'])

# Update campaign content with modified template using MailerLite API
api_url = f'https://api.mailerlite.com/api/v2/campaigns/{campaign_id}/content'
data = {'html': html_content}

response = requests.put(api_url, headers=headers, json=data)
if response.status_code == 200:
    print('Campaign content updated successfully!')
else:
    print(f'Error: {response.text}')
