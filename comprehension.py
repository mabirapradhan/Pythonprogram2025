# Comprehension 

# 1. List comprehension
# even=[expression for item in iterable if condition]

numbers=range(1,51)

even=[]
for i in numbers:
    if i%2==0:
        even.append(i)

print(even)

numbers=range(1,51)
even=[i for i in numbers if i%2==0]
print(even)

word=['hello','everyone','we','are','here','ram']
b=[i.capitalize() for i in word]
# for i in word:
#  b.append(i.capitalize())

print(b)

# 2.set
length={len(i) for i in word}
print(length)

# 3.dictionary 
# syntax={key_exp:value_exp for item in iterable(can be counted) if condition}

square={}
for i in length:
    square[i]=i**2
print(square)

square={i:i**2 for i in length}
print(square)

# nested comprehension
table=[[i*j for j in range(1,11)] for i in range(1,6)]
print(table)


# enumertes: add index of iterable item with that item
fruits=['apple','cherry','banana','mango','kiwi']

# e_fruits= enumerate(fruits)
for index,fruits in enumerate(fruits):
    print(index)

for index,fruits in enumerate(fruits):
    print(index,fruits)


# zip : combines two or more literable itemsas element-wise.It's pair looks like tuple.
#zip(literable1,leterable2,...)

names=['alex','bob','harry']
marks=[80,86,90]

final=zip(names,marks)

for items in final:
    print(items)