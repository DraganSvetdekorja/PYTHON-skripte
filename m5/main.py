from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)

@app.route('/')
def display_products():
    # Connect to Magento 1 database
    conn = MySQLdb.connect(host='185.117.121.243', user='svetdeko_magento', passwd='M4m9z2ovCJ4M', db='svetdeko_magento')
    cursor = conn.cursor()

    # Query the product collection with category ID 141
    query = "SELECT p.sku, p.name, p.price, p.image, c.category_name FROM products p \
             INNER JOIN category_product cp ON p.product_id = cp.product_id \
             INNER JOIN categories c ON cp.category_id = c.category_id \
             WHERE cp.category_id = 141 LIMIT 20"
    cursor.execute(query)
    product_data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Pass the product data to the Flask template
    return render_template('product_template.html', products=product_data)

if __name__ == '__main__':
    app.run(debug=True)
