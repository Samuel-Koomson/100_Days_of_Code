"""
In this program, the syntax is written as;
1. The statement to be executed comes first, in this case the squaring which is number ** 2
2. The for loop then follows 
3. The last part is the old or original list within which we are working on  
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)
