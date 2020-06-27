# This function will count the body mass
def bodyMassIndex(weight,height):
    bmi=(weight*703)/(height*height)
    print(f'User BMI = {bmi:.2f}')
    if bmi < 18.5:
        printBmi=(f'User with weight {weight} pound and height {height} inches is underweight')
    elif bmi <=24.9:
        printBmi=(f'User with weight {weight} pound and {height} height has normal weight')
    elif bmi <=29.9:
        printBmi=(f'User with weight {weight} pound and {height} height is overerweight')
    else:
        printBmi=(f'User with weight {weight} pound and {height} height is considered in obese category')
    return printBmi
# get data from user
invalidInput=True
while invalidInput:
    try:
        user_weight=float(input("Please enter your Weight in Pounds "))
        user_height = float(input("Please enter your Height in Inches "))
    except:
        print("Please enter your data in right format")
        continue
    # call function bodyMassIndex if data from user is in correct format
    if isinstance(user_weight,float) & isinstance(user_height,float):
        print(bodyMassIndex(user_weight,user_height))
        invalidInput=False
    else:
        invalidInput=True