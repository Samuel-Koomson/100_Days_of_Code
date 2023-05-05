"""
	Python program which makes use of loops and arithmethic operations to add 
	the sum of two even numbers
"""

numbers1 = int(input("Enter first number: "))
numbers2 = int(input("Enter any number: "))
if numbers1 > numbers2:
    print("numbers1 cannot be greater than numbers2")

even_numbers = 0
for number in range(numbers1, numbers2):
    if number % 2 == 0:
        even_numbers += number
print(even_numbers)
