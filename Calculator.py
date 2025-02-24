# Calculator
num1 = int(input("Enter the number 1 : ")) # Take 1st number from user
num2 = int(input("Enter the number 2 : "))# Take 2st number from user
operation = input("Select Opertion : ") # Take operation like Add,Sub ETC....
if operation == '+':
    print(f"Sum of {num1} and {num2} is {num1 + num2}") # Operation for sum
elif operation == '-':
    print(f"subtraction of {num1} and {num2} is {num1 - num2}") # Operation for Difference
elif operation == '*':
    print(f"Product of {num1} and {num2} is {num1 * num2}") # Operation for Product
elif operation == '/':
    print(f"Division of {num1} and {num2} is {num1 / num2}") # Operation for Division
else:
    print(" Incorrect number or operation ")

