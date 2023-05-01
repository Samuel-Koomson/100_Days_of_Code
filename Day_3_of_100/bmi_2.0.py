# Python program that makes use of nested loops (if, elif, else) to interprete BMI values

# Don't change the code below 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#Pseudocode
#1.Typecast the inputs into floats and int respectively
#2. conduct the mathematical operation to generate the BMI
#3. Round-up the bmi result into an integer
#4. Interprete bmi values using nested loop conditions 

#Write your code below this line
bmi = weight / height ** 2
#print(round(bmi))

if bmi < 18.5:
  print(f"Your BMI is {round(bmi)}, you are underweight")
elif bmi >= 18.5 and bmi <=25:
   print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
  print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    if bmi > 35:
        print(f"Your BMI is {round(bmi)}, you are clinically obese.")
