#para time code primero hay que escribir code
def func_one(n):
    return [str(num) for num in range(n)]
func_one(10)

def func_two(n):
    return list(map(str,range(n)))
func_two(10)

import time 
'''
Probando con la funcion 1
'''
#current time before code
start_time = time.time()
#run code
result = func_one(1000000)

#cyrrent time after code
end_time = time.time()

#elapsed time 
elapsed_time = end_time - start_time

print(elapsed_time)
'''
Probando con la funcion 2
'''
#current time before code
start_time = time.time()
#run code
result = func_two(1000000)

#cyrrent time after code
end_time = time.time()

#elapsed time 
elapsed_time = end_time - start_time

print(elapsed_time)

'''
Si es muy rapida la funcion va a tener un problema dando un tiempo, es decir la precision de la velocidad probablemente esste mal
'''
#para eso se usa timeit module, lo de arriba se puede usar en pedazos de codigo muy grandes (creo)

import timeit
#para funcion 1
stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
timeit.timeit(stmt,setup,number=1000000) #stmt y setup se pasa como string 

#para funcion 2
stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str,range(n)))
'''
timeit.timeit(stmt,setup,number=1000000) #stmt y setup se pasa como string 