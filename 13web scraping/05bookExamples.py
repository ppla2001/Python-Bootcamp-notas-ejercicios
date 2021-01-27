#queremos todos los libros con 2 estrellas
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
products = soup.select('.product_pod')

two_star_titles = []

for n in range(1,51):
    #hago el pedido a la pagina
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    #lo hago algo leible 
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #agarro todos los libros
    books = soup.select('.product_pod')
    #filter para agarrar solo los 2 star books 
    for book in books:
        # if 'star-rating Two' in str(book)

        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

two_star_titles