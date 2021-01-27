import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('img') #puede agarrar imagenes q no quiero 
soup.select('.thumbimage') #lo hago un poco mas especifico (solo quiero agarrar las imagenes dentro del articulo) 
#agarrando la foto q quiero
chabon_jugando = soup.select('.thumbimage')[0]
chabon_jugando
chabon_jugando['src']
#ahora para guardar la foto que quiero
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
'''image_link.content ''' #esto me da la informacion que necesito para guardar la foto (me da la info en binario)
f = open('webScrapingGuardandoFto.png','wb') #el final del nombre del archivo tiene q match con el final de lo q quiero guardar (image_link), el wb significa write binary (para q lo pueda leer la compu)
f.write(image_link.content)
f.close() 