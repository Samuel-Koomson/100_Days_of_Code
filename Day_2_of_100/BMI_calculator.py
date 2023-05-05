# python program that calculates the body mass index of a user

# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above

#Pseudocode
#1.Typecast the inputs into floats and int respectively
#2. conduct the mathematical operation to generate the BMI
#3. Round-up the bmi result into an integer

#Write your code below this line 👇
height = float(height)
weight = int(weight)
bmi = weight / height ** 2
#print(type(weight))
print(round(bmi))

if bmi < 15:
   print("you are underweight")
elif bmi > 15 and bmi <=25:
   print("you have normal weight")
elif bmi > 25 and bmi >= 30:
  print("you are obesed")
