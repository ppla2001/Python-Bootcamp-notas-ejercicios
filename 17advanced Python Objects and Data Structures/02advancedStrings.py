s = 'hello world'
s.capitalize() #first word in string
s.upper() #todos los words
s.lower() #todos los words
s.count('o') #cuantas o hay
s.find('o') # en q index position esta la o
s
s.center(20,'z') #quiero q el total length del string sea 20 y este en el medio de z
#son lo mismo
print('hello\thi')
'hello\thi'.expandtabs()

s = 'hello'
s.isalnum() #son alphanumeric?
s.isalpha() #si son del alphabet
s.islower() #si todo son lowercase
s.isspace() #si es todo whitespace, como hay letras va a dar False
s.istitle() #return true si esta formato de title: Hello
s.isupper() #lo contrario a islower
'HELLO'.isupper()
s.endswith('o')

#built in regular expresions 
s.split('e') #te parte todo en una list de lo de antes de la e y despues de la e
s = 'hiihhihihihhhi'
s.partition('i') #te devuelve lo de antes del partition, el partition y todo despues del partition
