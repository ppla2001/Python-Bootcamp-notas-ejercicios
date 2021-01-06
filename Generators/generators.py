def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result
create_cubes(10)

for x in create_cubes(10):
    print(x)
#todo lo de arriba se puede hacer mas facil de la siguiente manera
#de esta forma estamos siendo mas eficientes con la memoria 
def create_cubes(n):
    for x in range(n):
        yield x**3
create_cubes(10) #no te muestra la lista 

for x in create_cubes(10):
    print(x)

#otro ejemplo
def gen_fibon(n):
    a = 1 
    b = 1 
    for i in range(n):
        yield a
        a,b = b,a+b
for number in gen_fibon(10):
    print(number)

# mas conceptos 

def simple_gen():
    for x in range(3):
        yield x 
for x in simple_gen():
    print(x)

g = simple_gen()
g
print(next(g))
print(next(g))
print(next(g))
print(next(g)) #va a dar error porque ya pasamos por todos los numeros, en for no me da este error porq cuando usas for, agarra el error y automaticamente deja de llamar next

#otra funcion
s = 'hello'
for letter in s:
    print(letter)
next(s) #no se puede iterate, para poder hay que usar lo siguiente
s_iter = iter(s)
next(s_iter)
next(s_iter)
next(s_iter)
next(s_iter)
next(s_iter)

#lo mas importante es aprender a usar yield