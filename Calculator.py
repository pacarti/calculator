import sys

print("Hello! Welcome in a simple calculator program. Please choose the operation you want to make: \n + to add \n - to subtract \n * to multiply \n : to divide \n % to modulo \n \ to divide and round up to intiger. \n\n 0 to exit:", end = ' ')

operator = input()

if operator == '0':
    print("Goodbye. See you soon.")
    sys.exit()
