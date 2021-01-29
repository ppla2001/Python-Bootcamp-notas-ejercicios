import PyPDF2
f = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\Working_Business_Proposal.pdf','rb') #rb es read binary
pdf_reader = PyPDF2.PdfFileReader(f) #para que lea el pdf
pdf_reader.numPages #cuando lo llamo deberia dar la cantidad de paginas q tiene si es q funciona
page_one = pdf_reader.getPage(0) #primera pagina
page_one_text = page_one.extractText() #esto me lo da como un python string
page_one_text
#a veces pasa q cuando pedis las paginas te lo da pero cuando pedis el texto te da empty strings, si me da empty strings el pdf file no es compatible con pdf2
f.close()

#adding to pdf files
f = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
#para addPage, lo q quiero agregar deberia ser un pdfPageObject no un python string, por ejemplo:
type(first_page) #esto es un ejemplo
pdf_writer.addPage(first_page)
pdf_output = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\Some_BrandNew_Doc.pdf','wb') #overwrites another pdf file with this name
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

#quiero all text dentro de un pdf file 
f = open('C:\\Users\\plape\\OneDrive\\Escritorio\\Python\\Python-Bootcamp-notas-ejercicios\\15working with PDF & Spreadsheet CSV\\Working_Business_Proposal.pdf','rb')

pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):

    page = pdf_reader.getPage(num)

    pdf_text.append(page.extractText())

print(pdf_text[1]) #printie la pagina 1