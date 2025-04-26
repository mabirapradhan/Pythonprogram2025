# Suppose there is a list with strings or word.wap to display strings having even length.

words = ["english", "samajik", "nepali", "science", "math", "english"]

for i in words:
    if len(i) % 2 == 0:
        print(i)


# Wap to print even numbers from 1 to given range.

end = int(input("Enter end of range: "))

for i in range(1, end + 1):
    if i % 2 == 0:
        print(i)

# wap to sort numbers of list by core method.
numbers=[1,5,6,33,23,42,1,55]
numbers.sort()
print(numbers)

# wap to extract digits only from text.'user234@hello790' -> '234790'

text='user234@hello790 '
rs=''

for i in text:
   if i.isdigit():
      rs+=1

print('final result is',rs)



