#Python program that creates a simple game of rock, paper scissors using a combination of conditions, booleans, and randomisation methods.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
human_player = input("Make a choice, type '0' for rock, '1' for paper or '2' for scissors: ")
human_player = int(human_player)
print(human_player)
computer_player = random.randint(0, 2)
print(computer_player)

if human_player == 0 and computer_player == 2:
  print("Rock, Human wins")
elif human_player == 2 != computer_player == 0:
  print("Rock, Computer wins")
elif human_player == 0 and computer_player == 0:
  print("It is a draw, do it again")
 
if human_player == 2 and computer_player == 1:
  print("Scissors, Human wins")
elif human_player == 1 != computer_player == 2:
  print("Scissors, Computer wins")
elif human_player == 1 and computer_player == 1:
  print("It is a draw, do it again")

if human_player == 1 and computer_player == 0:
  print("Paper, Human wins")
elif human_player == 0 != computer_player == 1:
  print("Paper, Computer wins")
elif human_player == 2 and computer_player == 2:
  print("It is a draw, do it again")
