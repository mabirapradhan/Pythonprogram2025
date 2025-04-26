# sets: it is a ordered collection with no duplicated element.
# it is seperted by comma and enclosed by().
# it is also mutable.

# empty set
s=set()
print(s,type(s))

s={1,2,3}
print(s,type(s))



numbers={5,3,7,9,0,11,13,1,5}
print(numbers,type (numbers)) #removes duplicates and makes it in orederd collection


#adding new elements in set
numbers.add(24)
print(numbers)

s.clear()
print(s,type(s))

#numbers.remove(2)
#print(numbers)

numbers.pop()
#numbers.pop()
print(numbers)


odd=set([1,3,5,7,9,11])

u=set(range(1,21))
print(u)

rs=numbers.intersection(odd)
print(rs)

print(numbers.difference(odd))
print(numbers.union(odd))
print(numbers.update())
print(numbers.isdisjoint(odd))

a=set(range(1,21,2))
b=set(range(2,21,2))
print(a)
print(b)

print(a.isdisjoint(b))
print(a.issubset(u))


list_1={'ram','hari','shyam','gita'}
list_2={'gita','sita','liza','ram'}

common=list_1.intersection(list_2)
print(common,len(common))

