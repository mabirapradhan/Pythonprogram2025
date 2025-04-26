# data types:
 # numeric type : integer(int),float(float)
 # text data type : string(str)
 # sequence type : list(list), tuple(tuple) ,range(range)
 # boolean type : true,false(bool)
 # mapping type : dictionary(dict)
 # set type : set(set)

# DATA STRUCTURE
# list
# tuple
# dictionary
# set

# TYPES OF OPERATORS

#1) ARITHMETIC  operators = +,-,*,/
# exponential(power)- **
# floor division- // {n=int(n/10)}
# modulos(remainder)- % 5/2=2.5 rem=1

import math
# print(maths.ceil(1.000001))
# print(maths.floor(1.999999))

#2) ASSIGNMENT OPERATOR
# += a+=3  -> a=a+3
# -=,*=,/=,**=,//=,%=


#3)Comparison operator
# >,<,<=,>=  : it returns boolean result
# == (= in qbasic)
# != (<> in qbasic)


# 4) Logical operator
#and,or
#not() -negation of result (convert into false if it is true and viceversa)


# 5) Bitwise operator
# &- bitwise and
# |- bitwise or
# ~- bitwise negation

# 6) identity operator
# is:
# is not :

# 7) membership operator
# in: returns true if member belong to the sequence or group,otherwise false
# not  in:returns true if member doesn't belong to the sequence or group,otherwise false

#8) ternary operator
age=int(input('enter your age:'))
res='adult'if (age>=18) else print('child')
print(res)

# string is a sequence of characters enclosed either by single or double quote '' or "" or """
# string never allows single quotes inside single quote
# string can be used everywhere

# list
# sequence of elements seperated by comma and enclosed by quare or big bracket[].
# it is mutable that means elements inside list can be changed or altered

# tuple : it is same as lsit but it is enclosed by parenthesis () and it is imutable.
# we can oly access or making support of tuple.
# it is basically used for security purpose.

# dictionary
# unordered collection of elements having key:value,separeted by comma(,) and enclosed by {}
# it is mapping data type structure.


# SETS: it is a ordered collection with no duplicated element.
# it is seperted by comma and enclosed by().
# it is also mutable.

# CONTROL FLOW
#1. Conditional statement:if,if else,if elseif else,nested if 

# if : it is used when we have deal with single condition
#elif for elseif
# nested if (if inside another if)

# LOOP OF INTERACTION :performs same task repeatedly until condition is satisfied
# syntax:
#initalization
#condition check
#perform task
#interation increment/decrement
#terminate/result

# WHILE: used to perform same task repeatedly until conditon becomes false.

# Comprehension 

# 1. List comprehension
# even=[expression for item in iterable if condition]

# 2.set

word={1,3,43,22,34}
length={len(i) for i in word}
print(length)

# 3.dictionary 
# syntax={key_exp:value_exp for item in iterable(can be counted) if condition}

# enumertes: add index of iterable item with that item

# zip : combines two or more literable itemsas element-wise.It's pair looks like tuple.
#zip(literable1,leterable2,...)

import functions

functions.simple_interest()
