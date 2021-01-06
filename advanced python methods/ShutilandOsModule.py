files_path = 'C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\advanced python methods>'
f = open('practiceOsModule.txt', 'w+')
f.write('This is a test string!')
f.close()
import os 
os.getcwd() # me da en que directory estoy
os.listdir() #me da todo lo que esta adentro de mi directory
os.listdir('C:\\Users') # me da todos los users que hay
#mover files around
import shutil
shutil.move('practiceOsModule.txt', 'C:\\Users\\plape\\OneDrive\\Escritorio') # lo movi a desktop
os.listdir('C:\\Users\\plape\\OneDrive\\Escritorio') # con esto puedo chequear si se movio

#borrar files 
'''
os.unlink(path) borra one file de la path que le diga
os.rmdir(path) borra one folder de la path que le diga pero la folder tiene que estar vacia 
shutil.rmtree(path) borra todas las files y folders en la path que le diga
'''
#vamos a usar send2trash que lo tengo que descargar de command prompt
import send2trash
os.listdir()
shutil.move('C:\\Users\\plape\\OneDrive\\Escritorio\\practiceOsModule.txt', os.getcwd()) #volvi a traer file que movi antes a desktop
send2trash.send2trash('practiceOsModule.txt') #esta en trashbin de desktop

os.getcwd()
files_path2 = 'C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\advanced python methods\\exampleTopLevel'
for folder, subfolders, files in os.walk(files_path2): # te lo hace para todo (oswalk)
    print(f'Cureenty looking at {folder}\n')
    print('The subfolder are: ')
    for sub_fold in subfolders:
        print(f'\tSubfolder: {sub_fold}\n')
    print('the files are')
    for f in files:
        print(f'\tFile: {f}')
print('All done!')