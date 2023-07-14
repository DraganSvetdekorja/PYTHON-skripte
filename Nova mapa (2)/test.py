# - scrape basesite url https://www.met-met.si/trgovina/ with python selenium headless and beautifoulsoup 
# - go from base_url and page/1 to page/32 and collect
	product links from class li.isotope-item product type-productand save to product_links.csv
# - from product_links.csv go to product pages and extract 
sku	with span class sku 	, 
name with class h1.product_title 
price from class p.price and tag bdi, 
short description from class woocommerce-product-details__short-description	, 
kategorije from class span.posted_in and 
images from tag figure with class woocommerce-product-gallery__wrapperand save data to product_data.csv
# https://www.met-met.si/trgovina/
ChatGPT
Certainly! I can help you with scraping the provided website using Python, Selenium, and BeautifulSoup. Here's an example code that demonstrates the process you described:

python
Copy code
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up the Chrome driver (update the path to your chromedriver if needed)
driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

base_url = "https://www.met-met.si/trgovina/"
page_range = range(1, 33)  # Collect pages from 1 to 32

product_links = []

# Scrape product links from each page
for page in page_range:
    url = base_url + "page/{}/".format(page)
    driver.get(url)
    time.sleep(2)  # Wait for the page to load (adjust if necessary)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    products = soup.select("li.isotope-item.product.type-product")
    for product in products:
        link = product.find("a")["href"]
        product_links.append(link)

# Save product links to a CSV file
with open("product_links.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Product Link"])
    writer.writerows([[link] for link in product_links])

# Scrape product details from each product page
product_data = []

for link in product_links:
    driver.get(link)
    time.sleep(2)  # Wait for the page to load (adjust if necessary)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    sku = soup.find("span", class_="sku").text.strip()
    name = soup.find("h1", class_="product_title").text.strip()
    price = soup.find("p", class_="price").find("bdi").text.strip()
    description = soup.find("div", class_="woocommerce-product-details__short-description").text.strip()
    categories = [cat.text.strip() for cat in soup.select("span.posted_in a")]
    images = [img["src"] for img in soup.select("figure.woocommerce-product-gallery__wrapper img")]

    product_data.append([sku, name, price, description, categories, images])

# Save product data to a CSV file
with open("product_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["SKU", "Name", "Price", "Description", "Categories", "Images"])
    writer.writerows(product_data)

# Quit the driver
driver.quit()
Make sure to install the required packages: selenium, beautifulsoup4, and csv. You will also need to provide the correct path to the chromedriver executable compatible with your Chrome browser version.

This code will first scrape the product links from pages 1 to 32 on the provided website and save them to product_links.csv. Then, it will visit each product page, extract the SKU, name, price, short description, categories, and images, and save them to product_data.csv. The script utilizes headless mode for faster scraping. Adjust the waiting time (time.sleep()) if needed to allow for proper page loading.

Please note that web scraping can be subject to website terms and conditions, so ensure that you have the necessary permissions before scraping any website.






User
refectore code to functions
ChatGPT
Certainly! Here's a refactored version of the code using functions:

python
Copy code
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up the Chrome driver (update the path to your chromedriver if needed)
driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

def scrape_product_links(base_url, page_range):
    product_links = []

    # Scrape product links from each page
    for page in page_range:
        url = base_url + "page/{}/".format(page)
        driver.get(url)
        time.sleep(2)  # Wait for the page to load (adjust if necessary)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        products = soup.select("li.isotope-item.product.type-product")
        for product in products:
            link = product.find("a")["href"]
            product_links.append(link)

    return product_links

def save_product_links(product_links, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Link"])
        writer.writerows([[link] for link in product_links])

def scrape_product_data(product_links):
    product_data = []

    for link in product_links:
        driver.get(link)
        time.sleep(2)  # Wait for the page to load (adjust if necessary)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        sku = soup.find("span", class_="sku").text.strip()
        name = soup.find("h1", class_="product_title").text.strip()
        price = soup.find("p", class_="price").find("bdi").text.strip()
        description = soup.find("div", class_="woocommerce-product-details__short-description").text.strip()
        categories = [cat.text.strip() for cat in soup.select("span.posted_in a")]
        images = [img["src"] for img in soup.select("figure.woocommerce-product-gallery__wrapper img")]

        product_data.append([sku, name, price, description, categories, images])

    return product_data

def save_product_data(product_data, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["SKU", "Name", "Price", "Description", "Categories", "Images"])
        writer.writerows(product_data)

# Main execution
def main():
    base_url = "https://www.met-met.si/trgovina/"
    page_range = range(1, 33)  # Collect pages from 1 to 32

    # Scrape product links
    product_links = scrape_product_links(base_url, page_range)
    save_product_links(product_links, "product_links.csv")

    # Scrape product data
    product_data = scrape_product_data(product_links)
    save_product_data(product_data, "product_data.csv")

    # Quit the driver
    driver.quit()

if __name__ == "__main__":
    main()
In this refactored version, the code has been divided into functions to handle specific tasks. The scrape_product_links function scrapes the product links from the specified page range, and the save_product_links function saves the product links to a CSV file. Similarly, the scrape_product_data function extracts the product details from each product page, and the save_product_data function saves the product data to a CSV file.

The main execution has