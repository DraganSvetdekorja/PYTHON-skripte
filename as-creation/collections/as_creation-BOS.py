from selectorlib import Extractor
from bs4 import BeautifulSoup

import requests 
r = requests.get('https://www.tapetenshop.de/kollektionen/bos-battle-of-style/')

soup = BeautifulSoup(r.content, "html.parser")

products = soup.find_all('div', 'card-body')
for product in products:
		name = product.find("p", class_="product-name").text.strip()
		
		brand = product.find("p", class_="text-small").text.strip()
		price = product.find("p", class_="product-price").text.strip()
		image = product.find("img", class_="product-image").text.strip()
		#image = product.find("a", class_="product-image-link").text
		#sku = product.find("a", class_="product-image-link").text	
		print(name)
#		print('\n')
		print(brand)
#		print('\n')
		print(price)
#		print('\n')
		print(image)
#		print('\n')
			
		
		
		
		
		
		
		
		        # brand:
            # css: p.text-small
            # type: Text			
        # price:
            # css: p.product-price
            # type: Text
        # image:
            # css: img.product-image
            # type: Attribute
            # attribute: src
        # url:
            # css: a.product-image-link
            # type: Link
        # sku:
            # css: meta:nth-child(5)
            # type: Attribute
            # attribute: content
		
		# print(name)
		        # name:
            # css: p.product-name
            # type: Text

#print(soup.prettify())
