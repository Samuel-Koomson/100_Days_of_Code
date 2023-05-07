#Python program that executes a hurdle game using while loop

move()

def go():
    turn_left()
    move()
go()

def right_turn():
    turn_left()
    turn_left()
    turn_left()
right_turn()

def descend():
    move()
    right_turn()
    move()
descend()
 
def jump_over():
    go()
    go()
    right_turn()
    descend()
jump_over()

while at_goal() == False:
    jump_over()

