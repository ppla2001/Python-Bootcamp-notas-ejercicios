#Parte 1
import csv
data = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\04Exercise_Files\\find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
len(data_lines)
link = []

for num_row, data in enumerate(data_lines):
    link += data[num_row]
''.join(link)

#Parte 2
import PyPDF2
import re

f = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\04Exercise_Files\\Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages

pdf_text = ''
pattern1 = r'\d{3}'

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    page_text = page.extractText()

    pdf_text = pdf_text+' '+page_text


for match in re.finditer(pattern1,pdf_text):
    print(match)




pattern = r'\d{3}.\d{3}.\d{4}'

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num) 

    page_text = page.extractText()

    match = re.search(pattern,page_text)

    if match:
        print(match.group)