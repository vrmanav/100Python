from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
import time

LEFT_PADDLE_COOR = (-450, 0)
RIGHT_PADDLE_COOR = (450, 0)

screen = Screen()
screen.listen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.setup(width=1000, height=800)

left_paddle = Paddle(LEFT_PADDLE_COOR)
right_paddle = Paddle(RIGHT_PADDLE_COOR)
ball = Ball()

screen.onkey(key="q", fun=left_paddle.go_up)
screen.onkey(key="a", fun=left_paddle.go_down)

screen.onkey(key="w", fun=right_paddle.go_up)
screen.onkey(key="s", fun=right_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() < -375 or ball.ycor() > 375:
        ball.bounce()

screen.exitonclick()
