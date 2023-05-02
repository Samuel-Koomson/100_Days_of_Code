# Python program that creates a simple treasure hunt game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
select1 = input('This is the time to take your first step select "left" or "right"')
if select1 == "left":
  print("Sorry you made a wrong choice, GAME OVER")
  print('exit game')
else:
  print(" Great proceed to next level")
select2 = input("Ready for your next step, select 'left' or 'right'")
if select2 == 'left':
  print('You are doing well, head to next level')
else:
  print('Sorry this is the end for you. Try Again')
select3 = input('Impressive let us see what you are made of, select "left" or "right"')
coins = 0
points = 100
if select3 == "left":
  coins += points 
  print('great you are made of steel, you win 100 coins')
  print(f"Your new point is {points}")
else:
  print('Sorry you ended with no points')

select4 = input('Impressive let us see what you are made of, select "left" or "right"')
if select4 == "right":
  print("YOU are incredible")
  points += coins
  print(f"{points}")
select5 = input('make a magic choice, select "red" or "orange" or "green"')
if select5 == 'red':
  print("SORRY, you lost it all, final score is 0")
elif select5 == 'orange':
  print("You are a magician, you gained 500 extra points")
  points += 500
  print(f"Your final score is {points} points")
else:
  if select5 == "green":
    print("SORRY, you lost it all, final score is 0")
