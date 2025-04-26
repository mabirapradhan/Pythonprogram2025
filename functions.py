# Functions : It is a block of reuable code that performs a specific task.
# in python we define a function using def keyword followed by namewith () and colon.

# why we use function:
# to organize code into resuable code.
#  to avoid repeating the same code.
# to make debugging easier.
# to make large program in managable way.


# DEFINE FUNCTION
# syntax: def function_name (parameters):
            #statement/code block
            # return result  //optional


# CALLING FUNCTION
# function_name(argumentws)  // argument and parametrs are optional
# example:
def greet(name):
    print(f'Hello {name}, How are you?')

greet('Everyone')


def greet(name):
    print(f'Hello {name}, How are you?')

names=['preshak','riya','mabira','baibhav','arnav','shasrika']
for i in names:
    greet(i)

# two types of functions:
# BUILD IN FUNCTION:lower(),upper(),print(),input(),type(),int(),float()
# keywords: def,class

# CUSTOM FUNCTION:user defined function.

    # A. return type

def add():
    a=10
    b=5
    c=a+b
    return c
result=add()
print('the final result is',result)

    # B. non return typw

def add():
    a=10
    b=5
    c=a+b
    print('the result is',c)

# WAP to calculate simple interest using python function.

def simple_interest():
    principle=float(input('enter principle:'))
    time=float(input('enter time:'))
    rate=float(input('enter rate:'))
    si=(principle*time*rate)/100
    return si #return keyword is our last line of code
    print('hello')
si=simple_interest()
print('the final simple interset is',si)

# wap to check a number is even or odd.

def check():
    num=int(input('enter a number'))
    if num%2==0:
        print('number is even')
    else:
        print('number is odd')

check()

# sum of digits
def sum():
    num = int(input('Enter a number: '))
    c=0
    sum = 0

    while num > 0:
        c=num % 10
        sum += c
        num //= 10
        return sum

sum_digits=sum()
print('the sum of digits is',sum_digits)

# prime or composite
def check():
    num= int(input('enter a number'))
    f=0
    c=0
    for i in range(1,num+1):
        c= i%2
        if c==0:
            f+=1

    if f ==2:
        print('the number is prime')
    else:
        print('the number is composite')

check()

# if string is palindrome
def check_string():
    word=input('enter a word')
    rev=word[::-1]
    if rev== word:
        print('the string is palidrome')
    else:
        print('the string is not palindrome')

# count vowel letters
def vowels():
    count=0
    word='Hello Everyone'
    vowel=['a','e','i','o','u']
    for i in word:
        if i.lower() is vowel:
            count+=1
    print('total vowels is',count)
vowels()



    


   



