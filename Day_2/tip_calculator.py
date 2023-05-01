#Python program that calculates and splits bills among a group

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = int(input("What is your total bill:"))
friends = int(input("How many friends are spliting bill: "))
tip = int(input("What percentage tip are you giving: "))
tip = bill * tip /100
total_bill = bill + tip
friends_pay = total_bill / friends
print(f"each friend pays {friends_pay:.2f}")

