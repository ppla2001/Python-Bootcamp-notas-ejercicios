##### PARTE 1 REGULAR EXPRESSIONS #####
text = "The agent's phone number is 408-555-1234. Call soon!"
'phone' in text
import re
pattern = 'phone'
re.search(pattern,text)
pattern2 = 'Not in text'
re.search(pattern2,text) # si no devuelve nada significa q no hay match osea que no esta adentro del string
match = re.search(pattern,text)
match
match.span()
match.start()
match.end()
#el search solo te da el primer match
text2 = 'My phone once, my phone twice'
match2 = re.search('phone',text2)
match2
#encontrar muchos
matches = re.findall('phone',text2)
matches #te lo devuelve como objetos, no te da las especificaciones que te da el search
len(matches)
#para que te de todos con las especificaciones de search se usa re.finditer con un for loop
for match in re.finditer('phone',text2):
    print(match)
#como arriba, se puede usar los metodos
for match in re.finditer('phone',text2):
    print(match.span())
#para que te de el span es .group()
for match in re.finditer('phone',text2):
    print(match.group())

##### PARTE 2 REGULAR EXPRESSIONS #####
#hace falta que vea bien los character identifiers en notebook
text #lo defini arriba
celu = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text) # hay que ponerle r adelante de los identifiers para indicarle a python q estamos buscando un pattern
celu #si le cambio los numeros pero no la cantidad me va a seguir dando un match
celu.group() #me daba el numero
#mirar la lista de quantifiers del notebook que tambien es importante
celular = re.search(r'\d{3}-\d{3}-\d{4}',text) #esto es lo mismo que el de arriba solo que con menos codigo
celular
celular.group()
celular_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # lo que hace esto es los separa en tres grupos mientras que toma \d osea que sigue tomando que quiero digitos en la separacion
results = re.search(celular_pattern,text)
results.group()
results.group(1) #esto me da la parte 1 de 3 de la separacion que hicimos arriba para los numeros

##### PARTE 3 REGULAR EXPRESSIONS #####
re.search(r'cat','The cat is here') # me da resultado
re.search(r'cat','The dog is here') #no me da resultado
re.search(r'cat|dog','The dog is here') # al poner | significa or entones estoy diciendo que busque cat or dog en el string
re.findall(r'at','The cat in the hat sat there') #me encuentra todos los at osea cAT hAT sAT, me devuelve solo los at
re.findall(r'.at','The cat in the hat sat there') #si uso un . significa que me va a dar todo lo que este antes del AT osea me devuelve todo el CAT HAT SAT
re.findall(r'...at','The cat in the hat went splat') # ver resultado para entender un poco mas
re.findall(r'^\d','1 is a number') #string im looking for starts with a (in this case) digit, me da como resultado 1 pero si hago:
re.findall(r'^\d','The 1 is a number') #me da como que no hay resultado
re.findall(r'\d$','The number is 2') # string im looking for ends with a (in this case) digit
#quiero exclude algunos characters
phrase = 'There are 3 numbers 34 inside 5 this sentence' #quiero que me devuelva solo lo q no son numeros, exclude numbers
pattern = r'[^\d]' #esto esta diciendo que exlcuya digitos
re.findall(pattern,phrase) #me devuelve lista de todo lo que no son numeros
#para que se vea mas lindo cuando corro el codigo
pattern = r'[^\d]+' #esto esta diciendo que exlcuya digitos
re.findall(pattern,phrase) #me devuelve lista de todo lo que no son numeros

#get rid of punctuation
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
re.findall(r'[^!.?]+',test_phrase)
#o
clean = re.findall(r'[^!.? ]+',test_phrase)
' '.join(clean) #todo esto lo hice para unir todo sacandole la punctuation
#inclusion
texto = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are.'
patternn = r'[\w]+-[\w]+'
re.findall(patternn,texto)
#multiple options for matching
textone = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
re.search(r'cat(fish|nap|claw)',textone) #me devuelve catfish
re.search(r'cat(fish|nap|claw)',texttwo) # devuelve catnap
re.search(r'cat(fish|nap|claw)',textthree) #no me devuelve nada
re.search(r'cat(fish|nap|erpillar)',textthree) #devuelve caterpillar
