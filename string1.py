# string is a sequence of characters enclosed either by single or double quote '' or "" or """
# string never allows single quotes inside single quote
# string can be used everywhere

name='dursikshya education network'
address="ktm"
description="""
    i am student a student od see batch 2081.
"""

print(name)
print(address)
print(description)

#accesing and indexing (jsut as right$ we start from 0,1,2,3... and for left we start from -1,-2,-3...)
print(name,address)

print(name[4])

# slicing or substring (like mid$ we extract from middle)

print(name[11:21])

# concatination -adding two or more than two strings

str_1=name[0:10]
str_2=name[21:]

print(name[:20])
print(name[11:])

# printing even letters
print (name[1:10:2]) 
print (name[::-1])

# formating

print(f'{name} at {address}.{description}')

print('{} at {}',format(name,address))
print(name,'at',address)
