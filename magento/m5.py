# To retrieve a product collection from Magento 1 with attributes, all images, and categories, along with sorting and filtering, you can use the Magento 1 API and collection methods. Here's an example in python:


import requests
import json

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

# Print the details of each product
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

    # Print the details of the product
    print(f"Product ID: {product_id}")
    print(f"SKU: {sku}")
    print(f"Name: {name}")
    print(f"Price: {price}")
    print("Attributes:")
    for attribute in attributes:
        print(f"- {attribute['attribute_code']}: {attribute['value']}")
    print("Images:")
    for image in images:
        print(f"- {image['url']}")
    print("Categories:")
    for category in categories:
        print(f"- {category['category_id']}: {category['name']}")
    print("\n")

# Logout from the API
session.post(api_url + '/logout', data=json.dumps({'sessionId': session.cookies['PHPSESSID']}))
