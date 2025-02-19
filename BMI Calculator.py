print("### Welcome to the BMI calculator! ### \n")

name = input("First things first, what's your name? ")
print ("Hello, " + name + "!")

weight = float(input("Please tell me your weight in kilograms to calculate your BMI: ").replace("," , "."))
print("OK, next step...")

height = float(input("Now, write your height in meters? ").replace("," , "."))
if height == 0:
    print("ERROR: Height can't be zero.")
    exit()
else:
    BMI = weight / (height ** 2)

weight_status = "Unknown"
if BMI <18.5: 
  weight_status = "Underweight"
elif 18.5 <= BMI < 24.9:
  weight_status = "Normal range"
elif 25 <= BMI < 29.9:
  weight_status = "Overweight"
elif 30 <= BMI < 34.9:
  weight_status = "Obese class 1"
elif 35 <= BMI < 39.9:
  weight_status = "Obese class 2"
elif BMI >= 40:
  weight_status = "Obese class 3"

print(f"Your body mass index is: {BMI:.2f}, and according to United States National Library of Medicine, \n your weight status is: " + weight_status)