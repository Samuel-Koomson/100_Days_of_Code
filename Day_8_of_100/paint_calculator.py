""" Creating a simple function that calculates the quantity of paint needed to paint a wall
This takes 3 parameters and 3 arguements. it returns the quantity of paints by approximating 
it to the nearest whole number using the ceil function from the maths module
"""

#Write your code below this line 👇







#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height=test_h, width=test_w, cover=coverage):

    paint_calc = math.ceil(height * width / cover)
    print(f"You'll need {paint_calc} cans of paint")
    return (paint_calc)
paint_calc(test_h, test_w, coverage)
