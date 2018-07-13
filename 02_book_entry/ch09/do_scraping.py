# web scraping
import urllib.request
from bs4 import BeautifulSoup
#import bs4

req  = urllib.request.urlopen('http://quality-start.in/company')
soup = BeautifulSoup(req, "html.parser")

print(soup.find('h1').text)
#print(soup.find('p', class_="g_title").text)
print(soup.find('p').text)
