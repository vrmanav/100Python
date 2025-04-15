from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    "Move turtle forward by 50 steps"
    tim.forward(50)


def move_backward():
    "Move turtle backward by 50 steps"
    tim.backward(50)


def move_left():
    "Move turtle left by 10 degrees"
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_right():
    "Move turtle right by 10 degrees"
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    "Clear the screen & move reset turtle's position"
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
