from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
