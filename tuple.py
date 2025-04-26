# tuple : it is same as lsit but it is enclosed by parenthesis () and it is imutable.
# we can oly access or making support of tuple.
# it is basically used for security purpose.

abc=()
print(abc,type(abc))

books=('nep'',math','science','Social','math')
print(books,type(books))

# accesing & indexing
print(books[3][0:3])

#show those elements starts with letter's'

for item in books:
    if item.lower().startswith('s'):
        print(item)

for item in books:
    if item.lower().startswith(('e','m')):
        print(item)

print(books.count('math'))

# books.append('l')

# wap to store names of your friend in list and show as tuple.

friends=[]
no_friends=int(input('enter total no of frineds'))
i=0
while i<no_friends:
    names=input('enter your friends name:')
    friends.append(names)
    i+=1

print(friends,type(friends))

#converting into tuple #only used for count and indexing
friends= tuple(friends)
print(friends,type(friends))

