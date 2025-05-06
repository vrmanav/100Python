import turtle
import pandas

IMAGE = "./blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Enter a state's name?",
    ).title()

    if answer_state in all_states:

        x = data[data.state == answer_state].x
        y = data[data.state == answer_state].y
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x.item(), y.item())
        state_turtle.write(answer_state)
        guessed_states.append(answer_state)

    elif answer_state == "Give Up":
        remaining_states = []
        for state in all_states:
            if state not in guessed_states:
                remaining_states.append(state)
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break
