#Python code that generates random integers from a range of two numbers

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random

virtual_coin = random.randint(0, 1)
print(virtual_coin)

if virtual_coin == 0:
    print("Tails")
else:
    print("Heads")

