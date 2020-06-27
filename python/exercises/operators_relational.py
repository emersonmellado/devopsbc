# Equality operator ==
value = 100
number = 50
print(value == number) # False
print(value == 100) # True
print("-------------------------")

# Diferential operator
print(value != number) # True
print(value != 0) # True
# print(value <> number) # It will be true in older versions of Python
# print(value <> 0)  # It will be true in older versions of Python
print("-------------------------")

balance = 20
# Implementation 1
if (balance == 0):
    print("You have no balance to pay")
else:
    print("Your paying options are: Credit Card, Debit")

# Implementation 2
if (balance != 0):
    print("Your paying options are: Credit Card, Debit")

print("-------------------------")
# Less and greater than
print(value > 100) # I want to know if value is greater than 100
print(value < 100)
print(value >= 100) # I want to know if value is greater than 100 inclusive
print(value <= 100)