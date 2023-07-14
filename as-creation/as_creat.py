from selectorlib import Extractor
import requests 
r = requests.get('https://www.tapetenshop.de/kollektionen/bos-battle-of-style/')
e = Extractor.from_yaml_string("""
product:
    css: div.card-body
    xpath: ""
    multiple: true
    type: Text
    """)
e.extract(r.text)