# while: used to perform same task repeatedly until conditon becomes false.

n=1
while n<=10:
    print(n)
    n=n+1

choice='yes' 

while choice.lower()=="yes":
    name=input('enter your name')
    print(name)
    choice=input('do you want to run again')


# password validation
correct_pass='1234'
total_attempt= 3
attempt=0

while attempt<=total_attempt:
    pin=input('enter your pin:')

    if pin.lower()==correct_pass:
        print('password matched')
        break
    else:
        print('password doesnot match')
        attemt+=1
else:
    print('you exceed the limit')

# palindrome number

num=int(input('enter a number'))

a=num
print(a)
r=0
while a>0:
    c=a%10
    r=r*10 +c
    a//=10

else:
    if num==r:
        print(f'{num}is palindrome')
    else:
        print(f'{num}is not palindrome')

# prime or composite

num=int(input('enter a number'))
for i in range(1,num+1):
   
    if num%i ==0:
        f+=1
   
if f==2:
    print(f'{num} is prime')
elif f>2:
    print(f'{num} is composite')
else:
    print('invalid number')



