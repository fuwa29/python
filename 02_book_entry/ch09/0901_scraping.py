# 0901 web scraping
import urllib.request
from bs4 import BeautifulSoup

req  = urllib.request.urlopen('http://quality-start.in/company')
soup = BeautifulSoup(req, "html.parser")

contact = soup.find('a', class_='btn')
print(contact.string)

contact = soup.find('a', class_='btn-lg')
print(contact.string)

contact = soup.find('p', class_='page-header')
print(contact.string)
