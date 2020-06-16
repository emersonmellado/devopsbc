# Arithmetic
number = 100
sum = number + 10
print(sum, type(sum))

sub = number - 23
print(sub, type(sub))

div = number / 5
print(div, type(div))

mul = number * 8
print(mul, type(mul))

# % Modulus
remainder = number % 6           # 100 / 6 = 100 - 96 = 4
print("Remainder:", remainder)
print("Remainder:", number % 2)  # 100 / 2 = 0
print("Remainder:", number % 3)  # 100 / 3 = 100 - (33 + 33 + 33) = 1

# Order of operations ()
print(10+2-5*6/4)
print((10+2-5*6/4)%2)
print((10+(2-5*6)/4)%2)

# Exponent
print("2^3=", 2**3)
print("2^3=", (2**3)%2) # 0 is even - NOT 0 is odd

# Floor division
print("Floor D 1=", 9//2)
print("Floor D 2=", 9.0//2.0)
print("Floor D 3=", -11.0//3)

print("-----------------------")

# Alternative use of Operators
# +, %
# + = Concatenator
# % = Helper for spread value.

print(sum + sub, type(sum + sub))
print(sum + sub + div, type(sum + sub + div))
label_sum = "Sum"
print(label_sum + str(sum) + "Sub=" + str(sub)) # Concatenation

print("Sum: {:d}".format(sum))

print("Sum: %d" %(sum))
print("Sum: %d Sub: %d" %(sum, sub))
print("Sum:", sum, "Sub:", sub)

print(label_sum + " %d" %(sum))
print("Sum= %s" %(label_sum))