import sys

print("Hello! Welcome in a simple calculator program. \nPlease enter first number: ", end = '')
a = int(input())
print("Please enter second number: ", end = '')
b = int(input())

print(a)
print(b)
print("Please choose the operation you want to make. 0 to exit: \n + to add \n - to subtract \n * to multiply \n : to divide \n % to modulo \n / to divide and round up to intiger.:", end = ' ')

operator = input()

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
print(f"Result is: {result}")
