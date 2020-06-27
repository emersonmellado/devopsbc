from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    weight_kg = 100
    height_mi = 2

    BMI = weight_kg / (height_m ** 2)
    return(f'BMI is {BMI:.2f}')