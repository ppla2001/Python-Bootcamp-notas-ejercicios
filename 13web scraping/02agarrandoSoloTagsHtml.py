import requests
import bs4
#grabbing a title
result = requests.get('https://en.wikipedia.org/wiki/Wim_Hof')
type(result)
result.text #esto me da todo el html de la pagina como un string 
#ahora usamos bs4 
soup = bs4.BeautifulSoup(result.text,'lxml') #se le pasa el texto de todo y la forma que queremos parse (lo q descargamos antes en consola)
soup #esto me devuelve lo mismo que result.text solo q con formato de html
soup.select('title') #esto me deja buscar con tags de html como seria title, h1, etc (te devuelve lista porq puede haber mas de un title o mas de un p)
soup.select('h1')
soup.select('title')[0].get_text() #aca lo que hago es agarrar todos titles, digo que quiero solo el primer resultado y q quiero solo el texto, me devuelve solo el texto en vez de <title>Wim Hof </title>
soup.select('h1')[0].get_text()
