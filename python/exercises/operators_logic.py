# Logic Operators or Boolean operator
# and operators
number = 100
sum = number + 20
print(sum>0 and number>0) # True
print(sum>0 and number<0) # False
print("------------------")
"""
Truth tables
sum>0 | number>0 | sum>0 and number>0 | sum>0 or number>0
0     | 0        | 0                  | 0
0     | 1        | 0                  | 1
1     | 0        | 0                  | 1
1     | 1        | 1                  | 1
"""

# or operator
print(sum>0 or number>0) # True
print(sum>0 or number<0) # True
print(sum<0 or number>0) # True
print(sum<0 or number<0) # True
print("------------------")
# not operator
print(sum>0) # True
print(not(sum>0)) # False

print(sum>0 and number>0) # True
print(sum>0 and not(number>0)) # False

print(not(sum>0 and not(number>0))) # True
print("------------------")

print(sum>0 or number>0) # True
print(not(sum>0) or number>0) # True
print(sum>0 or not(number>0)) # True
print(not(sum>0) or not(number>0)) # False
print(not(not(sum>0) or not(number>0))) # True