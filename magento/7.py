# Certainly! Here's an updated version of the code that displays the retrieved product collection in an HTML table with sortable and filterable columns. It also includes the functionality to export the data to a CSV file and an Excel file.



import requests
import json
import csv
import pandas as pd

from tabulate import tabulate

# API endpoint URL
api_url = "http://your_magento1_domain/api/xmlrpc"

# API credentials
api_username = "your_api_username"
api_password = "your_api_password"

# Create a session
session = requests.Session()

# Login to the API
login_data = {
    'username': api_username,
    'password': api_password
}
login_response = session.post(api_url + '/login', data=json.dumps(login_data))

# Check if login was successful
if login_response.status_code != 200:
    raise Exception("Login failed")

# Retrieve the product collection
collection_data = {
    'sessionId': session.cookies['PHPSESSID'],
    'resourcePath': 'catalog_product.list',
    'args': [{
        'filters': {
            'status': '1'  # Filter by status (1: enabled, 2: disabled)
        },
        'storeView': 'default',  # Specify the store view
        'sort': 'name',  # Sort by product name
        'limit': 10  # Limit the number of products
    }]
}
collection_response = session.post(api_url + '/call', data=json.dumps(collection_data))

# Check if the collection retrieval was successful
if collection_response.status_code != 200:
    raise Exception("Failed to retrieve the product collection")

# Parse the response
collection = json.loads(collection_response.text)

# Access the retrieved products
products = collection['result']

# Create a list to store the table rows
table_data = []

# Iterate over each product and extract the details
for product in products:
    product_id = product['product_id']
    sku = product['sku']
    name = product['name']
    price = product['price']

    # Retrieve the product attributes
    attributes_data = {
        'sessionId': session.cookies['PHPSESSID'],
        'resourcePath': 'product_attribute.list',
        'args': [product_id]
    }
    attributes_response = session.post(api_url + '/call', data=json.dumps(attributes_data))
    attributes = json.loads(attributes_response.text)['result']

    # Retrieve the product images
    images_data = {
        'sessionId': session.cookies['PHPSESSID'],
        'resourcePath': 'product_media.list',
        'args': [product_id]
    }
    images_response = session.post(api_url + '/call', data=json.dumps(images_data))
    images = json.loads(images_response.text)['result']

    # Retrieve the product categories
    categories_data = {
        'sessionId': session.cookies['PHPSESSID'],
        'resourcePath': 'catalog_product.listOfAssignedCategories',
        'args': [product_id]
    }
    categories_response = session.post(api_url + '/call', data=json.dumps(categories_data))
    categories = json.loads(categories_response.text)['result']

    # Create a row for the HTML table
    row = [product_id, sku, name, price]

    # Add attribute values to the row
    for attribute in attributes:
        row.append(attribute['value'])

    # Add image URLs to the row
    image_urls = [image['url'] for image in images]
    row.append(", ".join(image_urls))

    # Add category names to the row
    category_names = [category['name'] for category in categories]
    row.append(", ".join(category_names))

    # Add the row to the table data
    table_data.append
