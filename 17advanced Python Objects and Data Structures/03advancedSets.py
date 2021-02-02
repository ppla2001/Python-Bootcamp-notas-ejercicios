s= set()
s.add(1)
s.add(2)
s.add(2)
s
s.clear()
s
s = {1,2,3}
sc = s.copy()
sc
s.add(4)
s
sc
s.difference(sc)#returns difference between two or more sets
#difference_update #returns set 1 after removing elements in set 2
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
s1
s.discard(2)
s

s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection(s2) #los que son iguales entre los dos sets
s1
s1.intersection_update(s2) #cambia s1 a lo que es la intersection entre los dos sets
s1

#is this joint
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
#returns true if they have null intersections
s1.isdisjoint(s2) #tienen en comun 1,2, deberia dar false
s1.isdisjoint(s3) #deberia dar true

#wether one set is inside another set
s1.issubset(s2) #deberia dar true

#whether one set contains another set
s2.issuperset(s1)

#semetric difference returns all elements that are exactly in one set, opposite of intersection
s1.symmetric_difference(s2) #deberia return 4

#union return union of two sets, all elemets that are in either of sets
s1.union(s2)

s1.update(s2) #updatea con union
