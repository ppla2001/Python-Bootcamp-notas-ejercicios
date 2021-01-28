from PIL import Image

mac = Image.open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\14working with images\\example.jpg') #le tengo que dar todo el directory porq sino no me muestra la imagen
mac.show()

mac.size #width, height
mac.filename
mac.format_description #international standard of jpeg it is 

#operations desde aca
mac.crop((0,0,100,100)) #los primeros dos numeros del tuple son x,y coordinates y los otros dos son width y height (esto que hice es el top left corner de la imagen) (el 0,0 de x,y significa que arranca desde el costado de izquierdo)

pencils = Image.open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\14working with images\\pencils.jpg')
pencils.show()
pencils.size
x = 0
y = 0
width = 1950 / 3
height = 1300 / 10
more_pencils = pencils.crop((x,y,width,height))
more_pencils.show() #pude cropear piola los primero tres lapices 

#ahora solo quiero los lapices de mas abajo
x = 0 #start en el x axil
y = 1100 #start em el y axil
w = 1950/3 #finish en el x axil
h = 1300 #finish en el y axil
more_more_pencils = pencils.crop((x,y,w,h))
more_more_pencils.show()

#ahora solo quiero agarrar la compu
mac.size
x = 1993 / 2 - 200
w = 1993 / 2 + 200
y = 800
h = 1257
mac_cropeada = mac.crop((x,y,w,h))
mac_cropeada.show()

mac.paste(im=mac_cropeada,box=(0,0)) #el primero es la foto que quiero pegar, el otro es la ubicacion donde la quiero pegar en la imagen (en este caso mac)
mac.show()
mac.resize((3000,500)) #para camiarle el tamano
mac.rotate(90) #rota 90 grados 

#Transparancy
red = Image.open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\14working with images\\red_color.jpg')
red.show()
blue = Image.open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\14working with images\\blue_color.png')
blue.show()
blue.putalpha(128) #si es 0 se hace completamente transparente, si es 255 es completamente opaco, si es algo en el medio es mas light el color
blue.show() # no se xq me cambia la foto a negro

red.putalpha(128)
red.show()

blue.paste(im=red,box=(0,0))
blue.show() #me dio algo rarisimo pero debe ser problema con las fotos
#como salvar?
#blue.save('') full file path o si lo quiero guardar en el mismo lugar solo le pongo nombre .png