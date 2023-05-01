# Simple python project which checks whether a given number is odd or even
# This program makes use of the comparison operators == and modulo (%)

#  Don't change the code below
number = int(input("Which number do you want to check? "))
#  Don't change the code above

#Pseudocode
#1. Accept number input from user
#2. Use comparison operators to check whether the number entered is even or odd
#3. even number - divides 2 without remainder
#4. odd number - divides 2 with a remainder
#5. print your answer to the console

#Write your code below this line
if number % 2 == 0:
    print("Your number is an even number")
else:
    print("Your number is an odd number")
