print("***HELLO WELCOME TO THE BEST BMI CALCULATOR!!***")
weight = float(input("Enter your weight in lbs:"))
height = float(input("Enter your height in inches:"))
weight_= weight * 703
height_= height * height
BMI = (weight_//height_)
if BMI <16:
   print("Your BMI is",BMI,"You are severely underweight")
elif BMI>=16 and BMI<18.4:
   print("Your BMI is",BMI,"You are underweight")
elif BMI>=18.5 and BMI<24.9:
   print("Your BMI is",BMI,"You are normal weight")
elif BMI>=25 and BMI<29.9:
   print("Your BMI is",BMI,"You are overweight")
elif BMI>=30 and BMI<34.9:
   print("Your BMI is",BMI,"You are obese")
elif BMI>=35 and BMI<39.9:
   print("Your BMI is",BMI,"You are severely obese")
elif BMI>39.9:
    print("Your BMI is",BMI, "You are morbidly obese!")