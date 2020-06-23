def bmi_app():
    get_name = str(input('Hello i am the BMI_CALCULATOR, WHO ARE YOU?'))
    print("hello" + get_name + ", Summer is coming")
    print('if you give me your weight in kilos separating decimals with a .')
    print('And your height in meters again separating decimals with a .')
    print('i will tell you if you need to start going to the gym')
    print('lets start \n ')
def main():
    bmi_app()
    get_height = 0.0
    get_weight = 0.0
    bmi_index = 0.0
    get_height = float(input('Give me your height in meters human!: '))
    get_weight = float(input('and now your weight in kilos: '))
    bmi_index = get_weight / (get_height * get_height)
    print("BeP bOp...")
    """
    BMI
    Categories:
    Underweight = < 18.5       # 18.5 non inclusive
    Normal weight = 18.5–24.9  # 25 non inclusive
    Overweight = 25–29.9       # 30 non inclusive
    Obesity = BMI of 30 or greater
    """

    if bmi_index < 18.5:
        print("a Human with a bmi of:" + str(bmi_index) + "is underweight, eat more")
    elif bmi_index < 25:
        print("it seems you can go to the beach you are normal! " + str(bmi_index))
    elif bmi_index < 30:
        print("watch out! " + str(bmi_index))
    else:
        print("start eating your veggies you bmi index is: " + str(bmi_index) + "you are overweight")
main()