import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game Project")

us_map = 'blank_states_img.gif'
screen.addshape(us_map)
turtle.shape(us_map)

state_names = pandas.read_csv('50_states.csv')
country = state_names.state.to_list()
print(state_names)

right_answer = []
unknown_state = []

while len(right_answer) < 50:
    guessed_state = screen.textinput(f"{len(right_answer)}/50 States so far", 'Enter a state to be added').title()

    if guessed_state == 'Exit':
        unknown_state = []
        # unknown_state = state_names.state.to_list()
        for index, row in state_names.iterrows():
            state = row['state']
            # if unknown_state[0] != 'state':
            if state not in right_answer:
                unknown_state.append(state)
        print(unknown_state)
        state_to_learn = pandas.DataFrame(unknown_state)
        state_to_learn.to_csv('state_to_learn.csv')
        break

    # for state in state_names:
    if guessed_state in state_names.state.to_list():
        right_answer.append(guessed_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_rows = state_names[state_names.state == guessed_state]
        new_turtle.goto(int(state_rows.x), int(state_rows.y))
        # new_turtle.write(state_rows.state)
        new_turtle.write(guessed_state)

    # if guessed_state == 'Exit':
    #     unknown_state = list()
    #     for state in state_names:
    #         if state != right_answer:
    #             unknown_state.append(state)
    #     print(unknown_state)
# state_to_learn = pandas.DataFrame(unknown_state)
# state_to_learn.to_csv('state_to_learn.csv')

