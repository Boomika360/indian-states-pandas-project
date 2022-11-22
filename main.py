import pandas

import turtle

from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=500, width=500)
screen.title("indian states")
image = "blankmap.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 30:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/30 is correct",
                                    prompt="what's another state name").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.color("red")
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
screen.exitonclick()
