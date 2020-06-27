print("to convert Celsius to Fahrenheit enter a")
print("to convert Fahrenheit to Celsius enter b")
print("to convert Celsius to Kelvin enter c")
user_input = input()


def celsius_to_fahrenheit(temp):
    return (temp*9/5)+32


def fahrenheit_to_celsius(t):
    return (t-32)*5/9


def celsius_to_kelvin(x):
    return x+273


if user_input == "a":
    temperature = float(input("Enter the base temperature: "))
    result = celsius_to_fahrenheit(temperature)
elif user_input == "b":
    temperature = float(input("Enter the base temperature: "))
    result = fahrenheit_to_celsius(temperature)
elif user_input == "c":
    temperature = float(input("Enter the base temperature: "))
    result = celsius_to_kelvin(temperature)

print(result)