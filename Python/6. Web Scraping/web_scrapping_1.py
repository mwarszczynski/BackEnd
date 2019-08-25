from bs4 import BeautifulSoup
import requests

url = ('http://coreyms.com')

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
# print(article.prettify())

headline = article.h2.a.text
print(headline)