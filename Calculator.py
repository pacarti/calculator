import sys

print("Hello! Welcome in a simple calculator program.") # \nPlease enter first number: ", end = '')

operator = None
result = None
b = None

while(operator != '0'):

    
    print("Please enter first number: ", end = '')
    try:
        a = float(input())
    except KeyboardInterrupt:
        print('\n')
        sys.exit()
    except:
        print("Wrong character. Please type number.")
        continue           
    while(b != True):
        print("Please enter second number: ", end = '')    
        try:
            b = float(input())
            break
        except KeyboardInterrupt:
            print('\n')
            sys.exit()
        except:
            print("Wrong character. Please type number.")
            continue


    print("Please choose the operation you want to make. 0 to exit: \n + to add \n - to subtract \n * to multiply \n : to divide \n % to modulo \n / to divide and round up to intiger.:", end = ' ')
    # try:
    operator = input()
    # except:
               
    
    if operator == '0':
        print("Goodbye. See you soon.")
        sys.exit()
    elif operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == ':':
        result = a / b
    elif operator == '%':
        result = a % b
    elif operator == '/':
        result = a // b
    else:
        print("Wrong character. Please choose +, -, *, :, %, / or 0. ")    
    print(f"Result is: {result}")

    print("Do you want to make some operation again?(y/n): ", end = '')
    choice = input()
    if choice == 'n' or choice == 'N':
        print("Goodbye. See you soon!")
        # sys.exit()
        break
    elif choice == 'y' or choice == 'Y':
        continue
