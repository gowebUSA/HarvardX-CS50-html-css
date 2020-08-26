import sys

try:
    x = int(input("x: "))
    y = int(input("x: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1) #1 is a status of error

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1) #1 is a status of error

print(f"{x} / {y} = {result}")