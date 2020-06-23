weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

weight_kg = weight / 2.205 # pounds to kg
height_m = height / 39.37

BMI = weight_kg / (height_m ** 2)
print(f'BMI is {BMI:.2f}')