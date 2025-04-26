# arguments types of function
# 1. positional arguments : it uses index value of sequential argument

# define function
def subtract(a,b):
    # PASS
    result=a-b
    return result

# calling function
rs=subtract(5,3)
print('the final subraction is',rs)


# default argument:
def add(x=10,y=5):
    # x=int(input('enter a value'))
    rs=x+y
    print(rs)

add(3)

# KEYWORD ARGUMENT:each value is sended with their respective keys and parameter name
#  must be send as aregument keys.

def sub (num2,num1):
    rs=num1-num2
    print(rs)

sub(num1=5,num2=3)

# ARBITRARY ARGUMENTS:passing multiple argument and store by one single parameter and operate
#  as sequential/literable object.
# it uses *args,where we use single streak(*) before parameter name for sequential or positional argumets.
# it uses **args,for keyword argument,kwargs.

# define function
# def totalsum(a,b,c,d,e):
    # rs=a+b+c+d+e
    # return rs

def totalsum(*args):
    print(args,type(args))
    # rs=0
    # for i in args:
        # rs+=1
    rs= sum(args)
    return rs
# call function:
rs=totalsum(5,2,9,0,5)
print('the total sum is',rs)

# **args :keyword args
def detail(**args):
    print(args,type(args))
    print (args.items())
    for k,v in args.items():
        print(k,v)

    print(f"Hello, I am {args['name']}. I am from {args['address']}.I am a {args['position']}.")
# we cannot use single cotation inside cotation.
detail(name='Mabira',address='KTM',position='student')


def result(sub,*marks):
    print(sub,type(sub))
    print(marks,type(marks))
    print(f'the result os {sub}  subject is {sum(marks)}')

result('maths',40,50,60,80)



