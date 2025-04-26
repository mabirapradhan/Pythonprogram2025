# fruit finder

input_=input('type in a fruits name:')

list_fruit=['banana','apple','kiwi','orange']

for i in list_fruit:
    if input_.lower()==i.lower():
        print('you choose:',i)
        break
    else:
        print(i)
else:
    print('intem doesnot find')


num=int(input('enter a number'))
rs=1
for i in range(1,num+1):
    rs=rs*i

print(rs)

# factorial calculator

input=int(input('enter a number'))
a=0

for i in  range(1,num+1):
    a=a*i

print(f'the factorial of {input} is{a}')