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