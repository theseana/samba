# inputs
weight = input('Enter your Weight(kg): ')
hieght = input('Enter your Hieght(m): ')

# convert type
weight = float(weight)
hieght = float(hieght)

# equation
bmi = weight / (hieght * hieght)

# result
if bmi < 18.5:
    print('Body Weight Defict')
elif 18.5 <= bmi < 24:
    print('Normal')
elif 24 <= bmi < 30:
    print('Weight Over')
elif 30 <= bmi < 35:
    print('Obesity First Degree')
elif 35 <= bmi < 40:
    print('Obesity Second Degree')
elif 40 <= bmi:
    print('Obesity Third Degree')