from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_position = [-140, -90, -40, 10, 60, 110, 160]

turtles = []
for turtle_count in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_count])
    tim.goto(x=-230, y=y_position[turtle_count])
    turtles.append(tim)
    tim.speed("slowest")

user_bet = screen.textinput(
    title="Make your guess", prompt="Which color do you think will win"
)

game_is_ON = True

while game_is_ON:
    for turtle in turtles:
        if turtle.xcor() < 215:
            random_distance = random.randint(1, 20)
            turtle.forward(random_distance)
        else:
            game_is_ON = False
            winner = turtle.pencolor().capitalize()

if user_bet == winner:
    print("🎉 You made a correct guess. You WIN !!")
else:
    print(f"😕 You were unlucky. {winner} turtle won the race.")
screen.exitonclick()
