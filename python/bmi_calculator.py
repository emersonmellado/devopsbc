print("Hello!  This is a a script to calculate your BMI!!")
print("--------------------------------------------------")
mass = float(input("Enter mass in kilograms: "))
height = float(input("Enter height in meters: "))
BMI = mass / (height ** 2) # (height ** 2)=(height * height)
print(f'BMI is {BMI:.2f}') #1: BMI = 15; 2: BMI = 23.5; 3: BMI = 29.8; 4: BMI = 31
if BMI < 18.5:
    printBmi = (f'User with weight {mass} kg and height {height} meters is underweight')
elif BMI <= 24.9:
    printBmi = (f'User with weight {mass} kg and {height} meters has normal weight')
elif BMI <= 29.9:
    printBmi = (f'User with weight {mass} kg and {height} meters is overweight')
else:
    printBmi = (f'User with weight {mass} kg and {height} meters is considered in obese category')

print(printBmi)