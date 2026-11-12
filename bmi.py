def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    if bmi < 18.5:
        print("BMI is underweight")
        value = -1
        
    elif bmi >= 18.5 and bmi <25.0:
        print("BMI is normal weight")
        value = 0
        
    else:
        print("BMI is overweight")
        value = 1

    return bmi,value

bmi_output = calculate_bmi(height=1.60, weight=55)
print("BMI = " + str(bmi_output))


