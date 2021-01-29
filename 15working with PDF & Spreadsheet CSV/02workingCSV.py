import csv
'''
#primero abrimos file 
data = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\example.csv')

#convertimos en csv data
csv_data = csv.reader(data)

#reformat into python object list of lists
data_lines = list(csv_data)
me da error porq cada file tiene distintos encodings, ejemplo si el file tiene @, el clasic encoding no sirve, si la file esta en castellano y tiene acentos el clasic encoding no sirve, se puede buscar en google cual es el encoding q se tiene q usar
'''
#primero abrimos file 
data = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\example.csv',encoding='utf-8')

#convertimos en csv data
csv_data = csv.reader(data)

#reformat into python object list of lists
data_lines = list(csv_data)
data_lines[0] #[0] column names
len(data_lines) #hay x rows + column information

for line in data_lines[:5]:
    print(line)

#si quiero alguna especifica tengo q pensar q numero es el q corresponde, ej quiero la row 10
data_lines[10] #funciona porq el 0 es column names entonces arranca de index 1 con row 1
#si quiero informacion especifica de row 10, como es una lista, puedo indexing, ej: quiero el mail
data_lines[10][3]

#si quiero solo los mails de todos 
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])
all_emails

data_lines[10] #nombre y apellido separado
#quiero agarrar nombre y apellido junto
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+ ' ' + line[2])
full_names

#escribir a un csv file 
file_to_output = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\to_save_file.csv',mode='w',newline='') #va overwrite file of the same name, se puede cambiar el mode dependiendo de lo q quiera hacer
csv_writer = csv.writer(file_to_output,delimiter=',') #delimiter, cual es el separador, que seapra una columna de otra
csv_writer.writerow(['a','b','c']) #escribe solo una row, esto es column names 
csv_writer.writerows([['1','2','3'],['4','5','6']]) #escribe varias rows, tiene q match la length (en este caso son tres datos), esto es mi data
#hace falta close file 
file_to_output.close()

#ahora en vez de overwrite la file, le quiero agregar 
f = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\to_save_file.csv',mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['7','8','9'])
f.close()