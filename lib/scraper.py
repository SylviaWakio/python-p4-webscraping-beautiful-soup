from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)


doc = BeautifulSoup(html.text, 'html.parser')

# heading = heading = doc.select('.heading-primary')[0].get_text(strip=True)
# print (heading)

courses = doc.select('.heading-25-extrabold.color-black') [0].attrs