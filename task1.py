# wap to calcualte hypotenuse by user given base and perpendicular

b=int(input('enter base:'))
p=int(input('enter perpendicular:'))

h=(b**2+p**2)**(1/2)

print('the hypotenuse is:',h)


# wap to find area and perimeter of circle

radius=float(input('enter radius of circle:'))
pi=3.14

area=pi*radius**2
perimeter=2*pi*radius

print('the area is',area)
print('the perimeter is',perimeter)


# wap to take input from user for their information and display them
name=input('enter name:')
grade=input('enter class:')
address=input('enter address:')

print(f'Helo{name}! Welocme to grade{grade}. Are you from{address}?')


# wap to convert temperature

c =float(input('enter temperature in celsius'))
f =(9/5)*(c+32)
print('temperature in farenheit:',f)


# wap to calculate simple interest

principle=float(input('enter principle:'))
time=float(input('enter time:'))
rate=float(input('enter rate:'))

si=(principle*time*rate)/100

print('simple interest is',si)





