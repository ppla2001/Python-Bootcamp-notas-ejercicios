#primero importamos todos los modules
import shutil
import os
import re
#Ahora vamos a unzip el archivo
#le tengo que dar el directory de donde esta el archivo porq sino no lo encuentra
'''
shutil.unpack_archive('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\12advanced python methods\\apm_Puzzle\\unzip_me_for_instructions.zip','puzzle','zip')
''' # lo dejo como comentario porq ya lo hice una vez, no hace falta que se siga repitiendo
#una vez hecho esto, tengo que iterar por todos los archivos de todas las carpetas, esto se hace usando os module
os.getcwd()
f_path = 'C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\12advanced python methods\\apm_Puzzle\\puzzle\\extracted_content'

def busqueda(file,pattern_celu=r'\d{3}-\d\d\d-\d\d\d\d'):
    f = open(file,'r')
    texto = f.read()
    if re.search(pattern_celu,texto):
        return re.search(pattern_celu,texto)
    else:
        pass

results = []

for folder,subfolders,files in os.walk(f_path):
    for f in files:
        full_path = folder+'\\'+f
        # print(full_path) lo dejo como comentario porq me llena con todas las carpetas y files
        results.append(busqueda(full_path))

# results 

for r in results:
    if r != None:
        print(r.group())