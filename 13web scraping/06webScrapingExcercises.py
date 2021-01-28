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
for tag in soup.select('.tag-item'):
    print(tag.text)

#parte 6
#sin saber cuantas paginas tiene la url
base_url = 'https://quotes.toscrape.com/page/{}'

todavia_paginas = True
authors = set()
page = 1 

while todavia_paginas:
    page_url = base_url.format(str(page))
    res = requests.get(page_url)
    
    if 'No quotes found!' in res.text:
        break

    soup = bs4.BeautifulSoup(res.text,'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)
    page += 1

authors 

#sabiendo que tiene solo 10 paginas 
authors = set()

for page in range(1,11):
    page_url = base_url.format(str(page))
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)