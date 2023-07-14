import requests
from selectorlib import Extractor
import pandas as pd

# Create an Extractor object with the selectorlib configuration
e = Extractor.from_yaml_string('''
    product:
        css: div.card-body

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

# List of URLs to scrape
urls = [
    "https://www.tapetenshop.de/kollektionen/black-is-beautiful/",
    "https://www.tapetenshop.de/kollektionen/black-is-beautiful/?p=2"
	    "https://www.tapetenshop.de/kollektionen/black-is-beautiful/?p=3"
]

# List to store extracted data
data_list = []

# Scrape data from each URL
for url in urls:
    # Send a GET request to the web page
    response = requests.get(url)

    # Pass the HTML content to the Extractor's extract() method
    data = e.extract(response.text)

    # Append the extracted data to the list
    data_list.extend(data['product'])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data_list)

# Save the DataFrame to an Excel file
df.to_excel("black_is_beautifoul_extracted_data.xlsx", index=False)

print("Data has been extracted and saved to 'black_is_beautifoul_extracted_data.xlsx'.")
