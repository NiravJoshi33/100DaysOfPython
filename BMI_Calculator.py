#Welcome to BMI Calculator

#get inputs
height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))

#calculate BMI
BMI = round(weight/(height**2),2)
print(f"Your BMI score is {BMI}")

#check the health
if BMI <= 18.5:
    print("You are underweight!")
elif BMI <= 25:
    print("You have normal weight!")
elif BMI <= 30:
    print("You are overweight!")
elif BMI <= 35:
    print("You are obsese!")
else:
    print("You are clinically obese!")