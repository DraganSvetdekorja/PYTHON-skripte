import requests

insta_url = 'https://www.instagram.com'
inta_username = input('enter username of instagram : ')

response = requests.get(f"{insta_url}/{inta_username}/")

print
