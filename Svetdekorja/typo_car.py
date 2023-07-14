from bs4 import BeautifulSoup as bs
import requests
url = 'https://www.tyremarket.com/Car-Tyres'
html_text = requests.get(url).text
soup = bs(html_text, 'html.parser')
# print (soup.nav)

# for string in soup.nav.stripped_strings:
    # print(string.strip('-'))
	
	
d = {}

for e in soup.select('nav ul li'):
	s = list(e.stripped_strings)
	d.update({s[0]: s[1:]})
	#print(s)

print(d)	