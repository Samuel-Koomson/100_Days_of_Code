"""
Program checks whether the player wins or not

#Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
"""

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ['_'] * len(chosen_word)
# display = []
# #len_chosen_word = len(chosen_word)
# for char in chosen_word:
#   display.append('_')
# print(display)
while '_' in display:
  guess = input("Guess a letter: ").lower()
      
  for position in range(len(chosen_word)):
      if chosen_word[position] == guess:
        display[position] = guess  
  #   char = chosen_word[position]  
  #   if char == guess:
  #     display[position] = char
  print(display)
# while guess == display:
  
  # for guess in display:
  #   if guess == display:
  #     print('You Win')
if '_' != display:
  print('You win, good job')
    
