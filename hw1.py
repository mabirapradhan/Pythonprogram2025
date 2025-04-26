# 1. Write a program to switch values between two variables. 
a=10
b=5

a,b=b,a

print('a=',a)
print('b=',b)

# 2. Student Attendance System 
total_classes = int(input('Enter total no of classes: '))
attend_classes = int(input('Enter no of classes attended: '))

attend_percentage = (attend_classes / total_classes) * 100

if attend_percentage >= 75:
    print('Eligible for exam.')
else:
    print('Not eligible for exam.')

# 3.  Electricity Bill Calculator 
unit=int(input('enter no of unit'))
cost = 0

if unit <= 100:
    cost = unit * 2
elif unit <= 200:
    cost = unit * 3
elif unit <= 500:
    cost= unit * 5
else:
    cost= unit * 7

print(f'Total electricity bill is: {cost}')

# ATM Withdrawal System
pin = input("Enter your PIN: ")
balance = 10000

if pin != "1234":
    print("Incorrect PIN")
else:
    print("1. Withdraw Money")
    print("2. Check Balance")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        amt = int(input("Enter amount to withdraw: "))
        if amt > 5000:
            print("Withdrawal limit exceeded.")
        elif amt <=5000:
            print("Transaction successful")
        else:
            balance -= amt
            print(f"Remaining Balance: {balance}")
    elif choice == "2":
        print(f"Current Balance: {balance}")
    else:
        print("Invalid ")

# 5. Divisibility Check 

num = int(input('Enter a number:'))

if num%3==0 and num%5==0:
    print('Divisible by both 3 and 5')
elif num%3==0 :
    print('Divisible by 3 only')
elif num%5==0:
    print('Divisible by 5 only')
else:
    print('Not divisible by 3 or 5')

    

# 6. Odd or Even Number 
num = int(input('Enter a number:'))

if num % 2== 0:
    print('Even')
else:
    print('Odd')