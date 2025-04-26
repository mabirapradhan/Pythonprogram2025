 # data types:
 # numeric type : integer(int),float(float)
 # text data type : string(str)
 # sequence type : list(list), tuple(tuple) ,range(range)
 # boolean type : true,false(bool)
 # mapping type : dictionary(dict)
 # set type : set(set)

name='mabira'
print(name,type(name))
books=['english','nepali','maths']
print(books,type(books))
book=('english','nepali','maths')
print(book,type(book))
rang=range(1,6)
print(rang,type(rang))
boolean=True
print(boolean,type(boolean))
dictionary= {'name':'mabira','address':'kathmandu'}
print(dictionary,type(dictionary))
sets=(1,2,3,2,1,'A','a','b','B')
print(sets,type(sets))

print('_'*10)


detail='my name is ram.i am 7 years old.i am going to schol tomorow.'
print(detail,type(detail))

details='my name is ram.i am 7 years old.i am going to schol tomorow.'.split()
print(details,type(details))


# Explicit type conversion : forcefully type conversion
a=5
print(a,type(a))
b=float(a)
print(b,type(b))

num1=int(float('5.5'))
print(num1,type(num1))

res= num1+a
print(res)

c=int('5')
print(c,type(c))

books=['english','nepali','maths']

books.append('social')
print(books)

books=tuple(books)
print(books,type(books))
