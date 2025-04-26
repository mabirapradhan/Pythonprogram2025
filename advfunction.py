# lamda function: anonymous function

def square(n):
    # print(n**2)
    return (n**2)
square(5)

# square=lambda x:x**2
# print(square(5))

# map(): it accept literable object and function name as call and apply same function to all literable items.

number=[1,2,3,4,5,6,7]

final = list(map(square,number))

print(final)

def s(lis):
    f_list=[]
    for i in lis:
        f_list.append(i**2)
    return f_list

list=s(number)
print(list)


# filter(): it worls sama as map but it choose to filter out items as per given condition.

# def odd(n):
#     if n%2 != 0:
#         return True
#     else:
#         return False
    
# odd_num =list(filter(odd, number))
# print(odd_num)
        
# a= lambda x:'even' if x%2==0 else 'odd'
# print(a(6))

# wap to return name if length is even otherwise return odd as text using map() & lambda.

# def even(name):
#     name=['mabira','sita','ram','shreeya']
#     a=0
#     a=len(name)
#     if a%2==0:
#         return name
#     else:
#         return 'odd'
# even=list(map(even,name))
# print(even)

# even_names= list(map(lambda name: name if len(name)%2==0 else 'odd',name))
# print(even_names)
# odd_names= list(map(lambda name: True if len(name)%2!=0 else False,name))
# print(odd_names)

# recursion function : a function call inside a same function.

# def fun_name():
    # print('hello)
    # func_name()

# func_name()

# wap to find factorial of given number.
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n* fact(n-1)
    
print(fact(5))

# wap to make countdown program.
def countdown(sec):
    if sec==0:
        return
    print(sec)
    countdown(sec-1)

countdown(5)

# overriding

def greet(first=None,last=None):
    if first != None and last != None:
        print(f'Hello{first} {last} ji')
    elif first != None:
        print(f'Hello{first} Ji')
    elif last != None:
        print(f'Hello{last} Ji')
    else:
        print('Hello')
    
    greet()
    greet('Mabira')
    greet(None,'Pradhan')
    greet(last='Pradhan')
    greet('Mabira','Pradhan')
