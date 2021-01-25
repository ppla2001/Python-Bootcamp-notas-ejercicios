from collections import Counter

mylist = [1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3]
Counter(mylist) #cuenta cuantos unos dos y tres, sirve tambien para strings en forma de dictionary
sentence = 'How many times does each word show up in this sentence with a word'
Counter(sentence.lower().split())

letters = 'aaabbbbbbcccccccccccdddddddddddd'
c = Counter(letters)
c 
c.most_common() #te da la lista del mas comun al menos 
c.most_common(2) # los dos mas comunes y asi cambiando el numero 
## me puedo fijar en el notebook que hay bastantes 
list(c)
#mas cosas 
from collections import defaultdict
d = {'a':10}
d
d['a']
d['wrong'] # me da error porq no existe en el diccionario
#para hacer un diccionario donde on me salte errores
d = defaultdict(lambda: 0) # para hacer que los valores salten default adentro de defaultdict lo haces con lambda y pones que queres que sea el default value 
d['correct'] = 100
d['correct']
d['Wrong key!']
d

#otra cosa
mytuple = (10,20,30)
mytuple[0]
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
Dog # es como crear una class
sammy = Dog(age=5,breed='Husky',name = 'Sam')
type(sammy) # no te dice que es un tuple
sammy
sammy.age # lo puedo llamar como si fueran atributes en una clase pero tambien lo puedo llamar como un tuple como se ve abajo
sammy[0]