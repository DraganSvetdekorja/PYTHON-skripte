import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://nova.svetdekorja.si/tapete-svet-dekorja.html'

username = 'dekor'
password = 'PpR2NwaPTxxRwUY7MrJJ'



session = requests.Session()
session.auth = (username, password)

# Send a GET request to the website
response = session.get(url)

# Check the response status code
if response.status_code == 200:
    # Successful request
    #print(response.text)
	
	#response = requests.get(url)

	# Create a BeautifulSoup object to parse the HTML content
	soup = BeautifulSoup(response.content, 'html.parser')

	# Find the <ul> element with the class "items filter-checkbox"
	kolekcija_ul = soup.find('div', class_='kolekcija')
	
	
	ul_element = kolekcija_ul.find('ul', class_='filter-checkbox')
	##print(ul_element)
	list = ul_element.find_all('label')
	for kolekcija in list: 
		print(kolekcija.text)

elif response.status_code == 401:
		# Unauthorized access
	print("Invalid credentials. Authentication failed.")
else:
		# Other status codes
	print(f"Request failed with status code: {response.status_code}")


# Extract the text from <label> elements within the <ul> element
# label_texts = [label.get_text(strip=True) for label in ul_element.find_all('label')]

# # Print the extracted label texts
# for label_text in label_texts:
    # print(label_text)
