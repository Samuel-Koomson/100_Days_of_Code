"""
This code slices through the list to print out all even numbers using list comprehension
The mudulo is used to look out for even numbers and printing them out.
This reduces the code by several lines
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)
