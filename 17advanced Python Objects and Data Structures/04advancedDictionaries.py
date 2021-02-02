d = {'k1':1,'k2':2}
{x:x**2 for x in range(10)} #have the key be x for the value x**2 for x in range to 10, te crea dictionary con dictionary comprehension

for k in d.iteritems():
    print(k) #returns tuples of keys and values

for k in d.itervalues():
    print(k) #returns just the values

for k in d.iterkeys():
    print(k) #returns just the keys

d.viewitems() #te muestra todo
d.viewkeys() #solo keys
d.viewvalues() #solo values
