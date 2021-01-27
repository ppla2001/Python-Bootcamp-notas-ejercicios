import requests
import bs4
#leer la table dada en notebook que dice syntax|match result
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('.toctext')
soup.select('.toctext')[-1].get_text()

for item in soup.select('.toctext'):
    print(item.text)