import random
from art import logo, vs
from game_data import data

print(logo)
print('\n')

first_play = random.choice(data)
first_play1 = {key: value for key, value in first_play.items() if key != 'follower_count'}
first_play = first_play1
print(first_play)
print('\n')
print(vs)
print('\n')
second_play = random.choice(data)
# for play in second_play:
second_play1 = {key: value for key, value in second_play.items() if key != 'follower_count'}
second_play = second_play1
print(second_play)
print('\n')

def most_popular():
    most_popular = []
    # print(most_popular)
    # print('\n')
    # popular = input("Who is more popular, 'A' for first_display or 'B' for second_display ").lower()
    if first_play1 > second_play1:
    # if A == popular:
      most_popular = first_play
    elif second_play1 > first_play1:
      most_popular = second_play
      return most_popular
    print('\n')
most_popular()

popular = input("Who is more popular, 'A' for first_display or 'B' for second_display ").lower()

A = first_play1
# print('\n')
# print(second_play1)

B = second_play1
# print(B)
# print('\n')
winning = True
while winning == True:
  
#   def most_popular():
#     most_popular = []
#     # print(most_popular)
#     print('\n')
#     # popular = input("Who is more popular, 'A' for first_display or 'B' for second_display ").lower()
#     if first_play1['follower_count'] > second_play1['follower_count']:
#     # if A == popular:
#       most_popular = first_play
#     elif second_play1['follower_count'] > first_play1['follower_count']:
#       most_popular = second_play
#       return most_popular
#     print('\n')
# most_popular()
  print(most_popular)
  print('\n')
  print(vs)
  print('\n')
  next_select = random.choice(data)
  next_select1 = {key: value for key, value in next_select.items() if key != 'follower_count'}
  print(next_select1)
    
  # if most_popular = False:
  # break
  print("sorry you lost, your score is: ")
