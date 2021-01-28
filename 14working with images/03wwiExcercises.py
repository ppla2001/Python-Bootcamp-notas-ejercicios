from PIL import Image
mask = Image.open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\14working with images\\mask.png')
word_matrix = Image.open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\14working with images\\word_matrix.png')

mask.show()

word_matrix.show()

mask.size
word_matrix.size
'''
x = 0
y = 0
w = 505
h = 251
matrix_cropeado = word_matrix.crop((x,y,w,h))
matrix_cropeado.show()
intente achicar la imagen de word matrix pero esta mal, tengo que estirar la de mask
'''

mask_cropeada = mask.resize((1015,559))
mask_cropeada.putalpha(100)
word_matrix.paste(mask_cropeada,(0,0),mask_cropeada)
word_matrix.show()