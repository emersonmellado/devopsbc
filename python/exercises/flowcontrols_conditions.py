"""
Syntax:

if CONDITION:
    # Condition is True
else:
    # Condition is False

Usage: Condition is replaced with an expression
True path: you write logic for the true case
False path: you write logic for the false case
"""
value = input("Give me a number: ")
if isinstance(value, int):
    print("All good, keep going")
else:
    value = float(value)

if value == 100:
    print("Value is equal to 100")
elif value>100:
    print("Value is greater than 100")
elif value<100:
    print("Value is less than 100")
else:
    print("Value it NOT equal to 100")