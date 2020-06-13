# Syntax for Variables
# VAR_NAME = EXPR

counter = 100 # Variable with a value assigned
counter_plus = 100.5 + 20.6 # Variable with an EXPRESSION assigned
name = 'John'
list = [0, 1, 3]
list_2 = ['John', "Rambo"]
# print(counter)
# print(counter_plus)
print(name)
# print(list)
# print(list_2)
name = "Rambo"
print(name)

# Python has a built-in INFERENCE system,
# that determines a type of a variable for you
# print(type(counter))
# print(type(counter_plus))
# print(type(name))
# print(type(list))
# print(type(list_2))

# Constants
# Be mindful that contants are a convention when outside of
# classes or functions
# The reason for it is its scope
NAME = "John"
print(NAME)
NAME = "Wayne"
print(NAME)
"""
# simple example of Scope
Title = "Title of my list" # This is in my global scope
1. Element one is a function # This is a local scope
    a. child_one = child one my list Title
    b. child_two = child one an expression or variable
2. Element two is another function
    a. child_one = child two an expression or variable
"""