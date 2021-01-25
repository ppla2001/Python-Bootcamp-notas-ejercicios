#Ejercicio 1
def gensquares(n):
    for x in range(n):
        yield x ** 2
for x in gensquares(10):
    print(x)

#Ejercicio 2
import random
random.randint(1,10)
def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)
for num in rand_num(1,10,12):
    print(num)

#Ejercicio 3
s = 'hello'
s_iter = iter(s)
next(s_iter)
next(s_iter)
next(s_iter)
next(s_iter)
next(s_iter)

#Ejercicio 4
'''
El uso de generator con yield en vez de una funcion normal se usa para poder usar menos memoria con el uso del codigo para mejor optimizacion, va generando a medida que se le pasan valores
'''

#Extra Credit
'''
es como list comprehension solo que en vez de dejarlo en la memoria va a ir generandolo, cambiar [] por (), poder ir iterando y no tener todo en la memoria 
'''