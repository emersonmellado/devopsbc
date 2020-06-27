# example is my identifier and I am assigning the value "Hello class"
example = "Hello class"
print(example)
number = 123
print(number) # 123

# Python is case sensitive
Example = "Is different than example"
print(Example)

# You cannot assign values to some symbols as if they are variables
# $ = "some value"
# @ = "Also not allowed"
# % = "You cannot assign a value to some symbols"
# 1_dollar = "This is not good"
currency_sign = "$ USD"
at = "This is allowed"  # user@example.com
one_dollar = "This is okay"
print(currency_sign)
print(at)
print(one_dollar)

# Naming Conventions - We'll talk more about it on OOP
class Person:
    _name = "John"
    _last_name = "Rambo"
# Person - This is good
# person - Don't do it like

# Encapsulation
_this_is_private = "This is my private value"
__this_is_strongly_private = "This is my strongly private value"
sometimes__ = "You will attach stuff to python"

# if, for, while is a reserved word
# if = "hello"
# def is also reserverd
def printme():
    print("Hello from a function")

printme()
# In order to break a running loop you use continue or break or even return
# You cannot use those words as variables.

# On some languages you can override the base language signs like + / - *,
# this is something not encouraged on python
value = 2+2 # 4