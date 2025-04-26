# loop or interation :performs same task repeatedly until condition is satisfied
# syntax:
#initalization
#condition check
#perform task
#interation increment/decrement
#terminate/result


#for loop
#for in string

string='mabira'

for letter in 'mabira':
    print(letter,end='')

#for in list/tuple

for i in [1,2,3,4,5,6]:
 print(i)

std={
   'name':'mabira'
   'address'-'kathmandu'
}
print(std.keys())
print(std['name'])

for key in std.keys():
   print(std[key])
   

   for i in range(1,8,2):
      print(i)

# wap to find if number is even or odd

num=int(input('enter a number'))
c=num %2
if c==0:
    print(f'{num} is even')
else:
    print(f'{num}is odd')

# wap to find multiplication table

num=int(input('ener a number'))

for i in range(1,10):
    m=num*i
print(f'{num}x{i}={m}')

# break and continue

for i in range(1,15): 
    if i ==5:
        break
    else:
        print(i)
    
for i in range(1,15): # till 14 only
    if i ==5:
        continue
    else:
        print(i)

# wap to check whether a required fruit is match or not.

#nested loop:

colors=['black','red','yellow','blue']
cars=['BMW','Tesla','Toyata']

for car in cars:
    for color in colors:
        print(f'{car} is {color}')