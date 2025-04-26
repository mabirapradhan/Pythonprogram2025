# Check if a Triangle is Valid
a = int(input('Enter 1st side:'))
b = int(input('Enter 2nd side: '))
c = int(input('Enter 3rd side: '))

if a + b > c and a + c > b and b + c > a:
    print('Triangle is Valid ')
else:
    print('Triangle is Invalid ')

# Determine the Type of Triangle
a = int(input('Enter 1st side:'))
b = int(input('Enter 2nd side: '))
c = int(input('Enter 3rd side: '))
if a == b == c:
    print('It is an Equilateral Triangle')
elif a == b or b == c or a == c:
    print('It is an Isosceles Triangle')
else:
    print('It is a Scalene Triangle')

#  BMI (Body Mass Index) Calculator
weight = float(input('Enter weight in kg:'))
height = float(input('Enter height in meters:'))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal weight')
elif bmi < 30:
    print('Overweight')
else:
    print('Obese')

# Count Number of Even and Odd Digits in a Number.
num = input('Enter a number:')
even = 0
odd = 0

for i in num:
    if i.isdigit():
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1

print('No of Even digits are:', even)
print('No of Odd digits are:', odd)

# Print a Simple Pattern (Stars).
for i in range(1, 4 + 1):
    print("* " * i)

# Sum of Digits of a Number : 1234
num = int(input('Enter a number: '))
c=0
sum = 0

while num > 0:
    c=num % 10
    sum += num % 10
    num //= 10

print('Sum of digits:', sum)

#  Sum of Even Numbers between 1 and N. closed interval of N
n = int(input('Enter a number : '))
sum = 0

for i in range(2, n + 1, 2):
    sum += i
print('Sum of even numbers from 1 to', n, 'is', sum)

#  WAP to check a number is Armstrong
import math
num=int(input('enter a number:'))
tem=num
r=0
l=len(str(num))
while num>0:
    c=num%10
    r=r+math.pow(c,l)
    num//=10

if r==tem:
    print('the armstrong is:',tem)
else:
    print('the number is not armstrong:')

#  print all divisors of a number. 
n = int(input('Enter a number: '))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')

#  WAP to display multiplication table from 2 to 5 using nested loop.
for i in range(1, 11): 
    for j in range(2, 6):  # Tables 2 to 5
        print(f'{j} x {i} = {j*i}', end='  ') 
    print()

#  WAP to count vowel letters in a string or text.
text=(input('enter text'))
count=0
vowel=['a','e','i','o','u']
for letter in text:
    if letter.lower() in vowel:
        count+=1
    
print('total vowel letter is',count)