# types of operators

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
a=0
print(a is 8)
print(a is not 8)
print (a=='8')


# 7) membership operator
# in: returns true if member belong to the sequence or group,otherwise false
# not  in:returns true if member doesn't belong to the sequence or group,otherwise false
res='Ram'in['ram','apple','ktm',1,2,3,4,'abcd']
res= 'a' not in 'apple'
res= 'b' not in 'apple'

print(res)
#8) ternary operator
age=int(input('enter your age:'))
res='adult'if (age>=18) else print('child')
print(res)

# wap to calcualte hypotenuse by user given base and perpendicular

b=float(input('enter base:'))
p=float(input('enter perpendicular:'))

h=0.5*(b**2)+(p**2)

print('the hypotenuse is:',h)