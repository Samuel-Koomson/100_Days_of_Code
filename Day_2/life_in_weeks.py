#Python program which calculates the number of days, weeks and months that a person has left to live

# Don't change the code below
age = input("What is your current age? ")
# Don't change the code above

#Pseudocode
#1. provide your current age
#2. typecast the age into int
#3. set age limit to 90
#4. conduct your maths operations for days, weeks and months
#5. print out your result using f-String

#Write your code below this line
age = int(age)
#current_age = age
age_limit = 90 - age #current_age
days_left = age_limit * 365
weeks_left = age_limit * 52
months_left = age_limit * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

