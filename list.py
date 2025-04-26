# list
# sequence of elements seperated by comma and enclosed by quare or big bracket[].
# it is mutable that means elements inside list can be changed or altered

# creating list
abc=[]
print(abc,type(abc))
books=['nepali','english','maths',4,'social','science']

xyz=list[1,2,3]
print(xyz,type(xyz))

#accessingand indexind
print(books[3],type(books[3]))
print(books[-2],type(books[-2]))

print(books[1:4])
print(books[1:4:2])

print(books[4][1]) #accessing perticular alphabet 

# list methods
print(len(books))

#adding element
books.append([1,2,3])
print(books)

books.insert(2,3) #adding words(before word add,word to add)
print(books)

#removing elements from list 
books.pop()
print(books)

books.pop(2)
print(books)

# abc.pop()
# abc.pop(9)

#reverse list
books.reverse()
print(books)

books.pop(2)
print(books)

# sorting list
books.sort()
print(books)

print(books.count('english'))

books.remove('english')
print(books)


#wap to add all numbers inside list and give final sum.

number=[1,2,3,4,5]
a=0
for i in number:
    a+=i
print('the sum is',a)

