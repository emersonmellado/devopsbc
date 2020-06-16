# Syntax for Variables
# VAR_NAME = EXPR

x = 1
y = 2
z = x + y
# print("Z:", z)

counter = 98 + 5 # Variable with a value assigned
counter_plus = counter + 20.6 # Variable with an EXPRESSION assigned
name = 'John'
list = [0, 1, 3]
list_2 = ['John', "Rambo"]

# Python has a built-in INFERENCE system,
# that determines a type of a variable for you, use the type()
# function to see it

# Primitive types: Numbers (Int, Float, decimal), String, Booleans

print("Counter=", counter, "| type=", type(counter))
print("Counter + 20.6=", counter_plus, "| type=", type(counter_plus))
print("Name=", name, "| type=", type(name))
print("List=", list, "| type=", type(list))
print("List2=", list_2, "| type=", type(list_2))

print("=========================")
# You can also print using concatenation,
# Just make sure to concatenate str()
print("Counter= " + str(counter) + " | type= " + str(type(counter)))

# name = "Rambo"
# print("Reassign name:", name)

# Constants
# Be mindful that contants are a convention when outside of
# classes or functions
# The reason for it is its scope
NAME = "John"
print(NAME)
NAME = "Wayne"
print(NAME)
"""
# Data Structures example: Classes, Functions, Enumerators, Lists
# simple example of Scope
Title = "Shopping list" # This is in my global scope
1. Produce # This is a local scope
    a. corn = child one my list Title
    b. potato = child one an expression or variable
2. Bakery
    a. cake = child two an expression or variable
    b. bread
    c. pecan pie
"""

"""
Data Structure quick and dirty example:
# 100 is just data
counter = 100 | this is an expression
Class DataStructure
    counter = 100
    plus = 20.6
    name = "John
"""
