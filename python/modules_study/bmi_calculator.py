def bmi(weight, height):
    return round(weight / (height ** 2), 2)

def bmi_imperial(weight, height):
    weight_kg = weight / 2.205  # pounds to kg
    height_m = height / 39.37 # inces to meters
    return round(weight_kg / (height_m ** 2), 2)