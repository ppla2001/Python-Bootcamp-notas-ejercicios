import math
help(math) #me dice que cosas tiene math
value = 4.35
math.floor(value) # redondea al valor mas chico
math.ceil(value) #redondea al valor mas grande
round(value) #redondea
round(4.5) # va para abajo
round(5.5) #va para arriba
#siempre se intenta redondear a numeros pares 
math.pi
from math import pi
pi
math.e
math.inf #infinito
math.nan #not a number
math.log(math.e)
math.log(100,10) #me devuelve lo que tendria que elevar al cuadrado a 10 para que me de 100 en este caso seria 10**2
math.sin(10)
math.degrees(pi/2)
math.radians(180)

#vamos a random module
import random
random.randint(0,100)
random.seed(101) #tengo que correr todo el codigo de abajo junto con esta linea para que me de los mismos numeros todo el tiempo
print(random.randint(0,100)) # es decir, por mas veces que corra el codigo, este me deberia dar 74 siempre (a menos que reinicie seed en ese caso cambiaria a otro numero)
print(random.randint(0,100)) # lo mismo con este
print(random.randint(0,100)) # etc...
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
#random item from list
mylist = list(range(0,20))
mylist
random.choice(mylist)
#grab multiple items from list
#sample with replacement, allow int to be chocen more than once
random.choices(population=mylist,k=10) #ddeberia tocar numeros iguales en algun momento
#sample without replacement, una vez que se elige un numero, no te puede tocaar de nuevo
random.sample(population=mylist,k=10)
#shuffle, se te queda para siempre shuffled
random.shuffle(mylist)
mylist

random.uniform(a=0,b=100)#randomly pick a value between a and b, floating points are allowed, cada numero tiene la misma likelyhood de ser elegido
random.gauss(mu=0, sigma=1) #normal distribution