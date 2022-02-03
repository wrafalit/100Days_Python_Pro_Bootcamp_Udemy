# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(weight)/(float(height)**2)
round_bmi = round(bmi,1)

if round_bmi < 18.5:
    print(f"Your BMI is {round_bmi}, you are" +"\033[1m underweight \033[0;0m")
elif round_bmi < 25:
    print(f"Your BMI is {round_bmi}, you have a \033[1mnormal weight\033[0;0m.")
elif round_bmi < 30:
    print(f"Your BMI is {round_bmi}, you are \033[1mslightly overweight\033[0;0m.")
elif round_bmi < 35:
    print(f"Your BMI is {round_bmi}, you are \033[1mobese\033[0;0m.")
else:
    print(f"Your BMI is {round_bmi}, you are clinically obese.")



