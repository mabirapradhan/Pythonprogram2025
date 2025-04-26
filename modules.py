import math
import random

rs=math.prod([1,2,3])
print(rs)

print(random.random()*100)
print(random.randint(2,5))

numbers= random.randint(1,10)
print(numbers)

num=int(input('enter a number'))
print(numbers)
if num == numbers:
    print('you are lucky')
else:
    print('try again')

import advfunction
advfunction.countdown(10)
