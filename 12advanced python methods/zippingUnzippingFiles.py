#creo los files para comprimir en un zip
f = open('fileone.txt','w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()

#a partir de aca paso todos los files a un zip
import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED) #lo primero de adentro es que archivo y lo segundo el formato
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')#lo de adentro es donde lo quiero mandar todo, #si me fijo se creo la carpeta

#para comprimir carpetas enteras generalmente se usa la shutil module 
import shutil
dir_to_zip = "C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\extracted_content" #para agarrar directory mas facil click derecho y copy path
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip) #lo primero es el nombre de donde lo mando, segundo formato, tercero es donde lo mando
shutil.unpack_archive('example.zip','final_unzip','zip') #primero es nombre de cual estoy unzipping, segundo es carpeta que quiero que cree para madnarlo, tercero formato