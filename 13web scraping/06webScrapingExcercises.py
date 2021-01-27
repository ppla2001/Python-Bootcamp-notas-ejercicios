#parte 1
import requests
import bs4

#parte 2
res = requests.get('https://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(res.text,'lxml')
soup

#parte 3 
authors = set()
for name in soup.select('.author'):
    authors.add(name.text)
authors

#parte 4
quotes = []
for frase in soup.select('.text'):
    quotes.append(frase.text)
quotes

#parte 5
