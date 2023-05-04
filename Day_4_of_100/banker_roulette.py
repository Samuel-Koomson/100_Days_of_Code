# This python program selects a random person from a list of people 
# By converting a string to list and randomly selecting one person to make a
# payment incured by all members of the list

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#print(names)

#Write your code below this line 👇
people = len(names)
payer = random.randint(0, people -1)
real_payer = names[payer]
print(f"{real_payer} is going to buy the meal today!")
