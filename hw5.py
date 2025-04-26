# # wap to sort numbers of list by core method.
numbers=[1,5,6,33,23,42,1,55]
numbers.sort()
print(numbers)


menu={
    'burger':120,
    'pizza':250,
    'coffee':90
    }
print(menu.items())
order=input('enter your order')
order_= order
for i in menu:
        if order=='burger':
                print(order_.values['burger'])
        elif order=='pizza':
                print(menu.values['pizza'])
        elif order=='coffee':
                print(menu.values['coffee'])
        else:
                print('order is not available')


# atm widraw
balance = 20000  
min_balance = 500
max_withdraw = 10000

amount = int(input("Enter the amount you want to withdraw: "))

if amount > max_withdraw:
        print(" Error:Maximum withdrawal limit per transaction is 10,000.")
elif amount % 100 == 0:
        print("Amount is in multiples of 100.")
elif balance - amount < min_balance:
        print("ErrorMinimum balance must be 500. ")
else:
        balance -= amount
        print(f" New balance: {balance}")

