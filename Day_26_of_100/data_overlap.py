"""
In this program, two list comprehension methods are implemented, the first uses the open method which 
I am not familiar with yet probably because I have had to skip some lessons which I will go back to later
The second is the regular list option with which I can use list comprehension on
"""

# with open("file1.txt") as file1:
#     file1_data = file1.readlines()

# with open("file2.txt") as file2:
#     file2_data = file2.readlines()

file1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]

file2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

# result = [str(number) for number in file1_data if number in file2_data]

result = [number for number in file1 if number in file2]

# Write your code above 👆

print(result)
