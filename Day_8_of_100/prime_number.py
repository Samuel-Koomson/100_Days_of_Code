"""
Program that checks whether a given number is a prime number or not. 
In order to do that we use the boolean data type and comparison operators to 
check whether a number is prime or not
"""

#Write your code below this line 👇
n = int(input("Check this number: "))

def prime_checker(number):
    prime_num = True
    for num in range(2, number):
        if number % num == 0:
            prime_num = False
    if prime_num:
        print("It's a prime number")
    else:
        print("It's not a prime number")     
prime_checker(number=n)
