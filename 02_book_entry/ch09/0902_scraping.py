# web scriping
import urllib.request
from bs4 import BeautifulSoup

req  = urllib.request.urlopen('http://quality-start.in/company')
soup = BeautifulSoup(req, "html.parser")

side_menu = soup.find('div', class_ = 'list-group')
print(side_menu)

for i in side_menu.find_all('a'):
    print(i.string)