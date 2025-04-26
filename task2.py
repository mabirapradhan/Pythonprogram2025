# ticket price

age=int(input('enter your age'))
no_ticket=int(input('enter no of ticket'))

if age>0 and age<100:
    # for child
    if age<12:
        price=100
        if no_ticket>5:
          total_price=(price*no_ticket)
          total_price-=total_price*0.1
          print(f'the total price is {total_price}')
        else:
          total_price=(price*no_ticket)
          print(f'the total price is {total_price}')
        

    if age>=12 and age<=60:
        price=200
        if no_ticket>5:
          total_price=(price*no_ticket)
          total_price-=total_price*0.1
          print(f'the total price is {total_price}')
        else:
          total_price=(price*no_ticket)
          print(f'the total price is {total_price}')

    # for older citizen
    if age>60:
       price=150
       if no_ticket>5:
          total_price=(price*no_ticket)
          total_price-=total_price*0.1
          print(f'the total price is {total_price}')
       else:
          total_price=(price*no_ticket)
          print(f'the total price is {total_price}')

else:
   print('invalid age')



# wap to display largest number among 3 inputs.

num_1= int(input('enter first number'))
num_2= int(input('enter second number'))
num_3= int(input('enter third number'))

if num_1>num_2 and num_1>num_3:
    print(f'{num_1} is the greatest number')

elif num_2>num_1 and num_2>num_3:
    print(f'{num_2} is the greatest number')

elif num_3>num_1 and num_3>num_2:
 print(f'{num_3} is the greatest number')

else:
   print('error')
  


# TO CALCULATE FINAL SALARY

#Basic salary
#Bonus (if person has worked for more than 5 years(experience))
#Deduction (tax if salary exceeds x )
#=Final salary


salary=float(input('enter your salary'))
exp_year=float(input('enter your year of experience'))
deduct_amt=5000

if salary>50000 and exp_year>5:
    bonus=salary*0.1
    final_salary=salary+bonus-deduct_amt

elif salary>50000 and exp_year<=5:
    bonus=0
    final_salary=salary+bonus-deduct_amt

elif salary<50000 and exp_year>5:
    bonus=salary*0.1
    deduct_amt=0
    final_salary=salary+bonus+deduct_amt

else:
    bonus=0
    deduct_amt=0
    final_salary=salary+bonus+deduct_amt

print(f'my final salary is{final_salary}')


      







