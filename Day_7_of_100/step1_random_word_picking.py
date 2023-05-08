"""
In this step, we randomly select a word from the given list
Then we ask user to input any character of their choice
The selected character is matched against the randomly selected word to check whether 
the character matches the selected word
"""

#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Type a random character to guess: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for guess in chosen_word:
  if input == guess:
    print("correct")
  else:
    print("try again")
