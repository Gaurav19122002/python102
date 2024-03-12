#nested if-elif statements
weight= float(input("enter your weight in kilograms"))
height= float(input("enter your height in meters"))
bmi= weight/(height**2)
if bmi<18.07:
    print(f"your bmi is {bmi} you are underweight")
elif bmi<25:
    print(f"your bmi is {bmi} you are fit")
elif bmi<30:
    print(f"your bmi is {bmi} you are overweight")
elif bmi<35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinically obese")