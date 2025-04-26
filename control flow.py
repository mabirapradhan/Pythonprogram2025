# control flow
#1. Conditional statement:if,if else,if elseif else,nested if 

# if : it is used when we have deal with single condition
#elif for elseif
# nested if (if inside another if)


age= int(input('enter your age'))

if age>=18:
    citizenShip=input('enter your citizenship')
    if citizenShip.lower=='nepali':
        print('you are eligible to vote')
    else:
        print('you are not eligible to vote')
        
else:
    print('you are too young to vote')


# Match statement

day=int(input('enter day number'))

match day:
    
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case _:
        print('invalid')

    
# calating using match statement

num_1= float(input('first number'))
num_2= float(input('second number'))
operator=input('enter operator')

match operator:
     case '+' :
        print(f'Addition result s',num_1+num_2)
     case '-' :
        print(f'subraction result is ',num_1-num_2)
     case '*' :
        print(f'multiplication result is ',num_1*num_2)
     case '/' :
        print(f'divide result is ',num_1/num_2)
     case '**' :
        print(f'exponential result is ',num_1**num_2)
     case '//' :
        print(f'num_1//num_2=',num_1//num_2)
     case _ :
        print('error')

    
