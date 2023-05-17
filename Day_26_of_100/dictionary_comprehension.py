"""
Dictionary comprehension used on a string sentence to find the number characters in each word
The split function is introduced here to break down the string into individual words and then the 
the dictionary comprehension syntax is applied to it
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()
# print(sentence)
# result = {word:len(word) for word in sentence}

# print(result)

result = {word:len(word) for word in sentence.split()}

print(result)

