#ejemplo de error y arreglarlo con print etc
x = [1,2,3]
y = 2
z = 3 
result = y + z
result2 = x + y # no se puede agregar lista con integer, se puede agregar una lista a una lista con concatination o un numero con un numero
print(result)
print(result2)

#ahora vamos a ver usando el debugger
import pdb
a = [1,2,3]
b = 2
c = 3
result_one = b + c

pdb.set_trace() #para que me devuelva los resultados tengo que poner print(variable)
result_two = a + b