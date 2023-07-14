import requests

# Specify the URL of the website
url = 'https://nova.svetdekorja.si/'

# Specify the username and password
username = 'dekor'
password = 'PpR2NwaPTxxRwUY7MrJJ'

#af34FXKQDF4txTI

# Create a session and set the authentication credentials
session = requests.Session()
session.auth = (username, password)

# Send a GET request to the website
response = session.get(url)

# Check the response status code
if response.status_code == 200:
    # Successful request
    print(response.text)
elif response.status_code == 401:
    # Unauthorized access
    print("Invalid credentials. Authentication failed.")
else:
    # Other status codes
    print(f"Request failed with status code: {response.status_code}")
