import requests
from selectorlib import Extractor

# Create an Extractor object with the selectorlib configuration
e = Extractor.from_yaml_string('''
    product:
        css: div.card-body
 #       xpath: ""
        multiple: true
        type: Text
        children:
            name:
                css: p.product-name
                type: Text
            brand:
                css: p.text-small
                type: Text
            price:
                css: p.product-price
                type: Text
            image:
                css: img.product-image
                type: Attribute
                attribute: src
            url:
                css: a.product-image-link
                type: Link
            sku:
                css: meta:nth-child(5)
                type: Attribute
                attribute: content
''')

# Send a GET request to the web page
url = "https://www.tapetenshop.de/kollektionen/bos-battle-of-style/"
response = requests.get(url)

# Pass the HTML content to the Extractor's extract() method
data = e.extract(response.text)

# Print the extracted data
for product in data['product']:
    print("Product Name:", product['name'])
    print("Brand:", product['brand'])
    print("Price:", product['price'])
    print("Image URL:", product['image'])
    print("Product URL:", product['url'])
    print("SKU:", product['sku'])
    print("-----------------------------------")
