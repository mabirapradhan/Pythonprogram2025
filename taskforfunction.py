# WAP to take input as principal amt,time and rate and pass these as argument and return simple interest.

def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si

p=float(input('enter principle:'))
t=float(input('enter time:'))
r=float(input('enter rate:'))

si=simple_interest(p,t,r)
print('the simple interest is',si)

# Wap too check a given number is prime or composite

def check(num):
    f=0
    c=0
    for i in range(1,num+1):
        c=i%2
        if c==0:
            f+=1
    if f==2:
        print(f'{num} is prime')
    elif f>2:
        print(f'{num} is composite')
    else:
        print(f'{num} is neither composite nor prime')

num=int(input('enter a number'))
check(num)


    
