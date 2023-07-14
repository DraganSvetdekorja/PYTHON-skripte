import magento

url = 'https://b2b.svetdekorja.si/'
apiuser = 'dekor'
apipass = 'af34FXKQDF4txTI'

# Create an instance of API
client = magento.API(url, apiuser, apipass)

# A filter expression as dictionary.
order_filter = {'created_at':{'from':'2011-09-15 00:00:00'}}
products = client.product.list(order_filter)

# Get a list of product types
product_types = client.product_types.list()

# Get a specific product
sku = 'ALEX'
product = client.product.info(sku)

# Add comment to an order
order_increment_id = '100000001 '
status = 'canceled'
client.order.addcomment(order_increment_id, status)

print(products)

print(sku)