# # The simplest input
# n = input('Choose a number: ')
# print('Number %s \n' %(n))
# print('Number:',n)

# # Data Type Error
# n = input('Choose a number: ')
# print(type(n)) # str
# value = n + 100
#
# print('Input number %s \n' %(n))
# print('Calculated Number:',value)

# # Fixing Data type error
# n = input('Choose a number: ')
# value = int(n) + 100
#
# print('Input number %s \n' %(n))
# print('Calculated Number:',value)

# Wrap the input in a int() function to convert it from str to int
n = input('Choose a number: ')
value = int(n) + 100

print('Input number %s \n' %(n))
print('Calculated Number:',value)