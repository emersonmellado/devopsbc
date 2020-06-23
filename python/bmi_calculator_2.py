print("Hello! This is the B.M.I calculator. \n"
      "-----------------------------------\n")
height = float(input("Please, enter your height in meters: "))
weight = float(input("Please, enter your weight in kilos: "))
print("-----------------------------------")
bmi_index = (weight / (height * height))
print("Your B.M.I. is: ")
print(round(bmi_index))
if (bmi_index <= 25):
    print("34.8% of people have the same B.M.I. as you.")
elif (bmi_index <= 30):
    print("49.8% of people have the same B.M.I. as you." + str(bmi_index))
elif (bmi_index <= 35):
    print("11.5% of people have the same B.M.I. as you." + str(bmi_index))
elif (bmi_index <= 40):
    print("2.9% of people have the same B.M.I. as you." + str(bmi_index))
else:
    print("1.0% of people have the same B.M.I. as you." + str(bmi_index))