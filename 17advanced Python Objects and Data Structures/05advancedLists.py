l = [1,2,3]
l.append(4)

l.count(10) #cuantas veces esta en la list

x = [1,2,3]
x.append([4,5])
print(x) #te appends el entire element to the list, te mete la lista en la lista

x = [1,2,3]
x.extend([4,5])
print(x) #te agrega todo en la lista original en vez de meter una lista en la primera lista

l.index(2) #index of whatever is placed in the variable, si quiero index algo q no esta en la list me da error

l.insert(2,'inserted') #index and object, olaces object in the index supplied
l #inserted en index 2

l.pop() #borra el ultimo element the la list y camibia permanent en la list
l
l.pop(0) #borra el primer index numero

l.remove('inserted') #removes the first occurance of a value
l

l = [1,2,3,4,3]
l.remove(3)
l

l.reverse()
l

l.sort()
l
