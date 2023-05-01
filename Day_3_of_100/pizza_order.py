#Python program that uses nested loop conditions to generate a pizza order

 # Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

# Write your code below this line

# Pseudocode
# 1. declare and initialize seize of pizza
# 2. declare and initialize the toppings
# 3. check the size selected against the options declared
# 4. Check whether user wants pepperoni
# 5. If you selects yes, add pepperoni price to selected size
# 6. check whether user wants extra cheese
# 7. If user selects yes, add cheese price to selected cost
# 8. print final bill to the console

S_price = 15
M_price = 20
L_price = 25

pepperoni_price = 2
extra_cheese_price = 1

if size == 'S':
    pizza_price = S_price
elif size == 'M':
    pizza_price = M_price
else:
    pizza_price = L_price
    
if add_pepperoni == 'Y':
    if size == 'S':
        pizza_price += pepperoni_price
    else:
        pizza_price += 3

if extra_cheese == 'Y':
     pizza_price += extra_cheese_price
print(f"Your final bill is: ${pizza_price}")
  
