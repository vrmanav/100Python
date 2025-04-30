from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
from turtle import Screen
import time

LEFT_PADDLE_COOR = (-450, 0)
RIGHT_PADDLE_COOR = (450, 0)

screen = Screen()
screen.setup(width=1000, height=800)
screen.title("Ping Pong game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

left_paddle = Paddle(LEFT_PADDLE_COOR)
right_paddle = Paddle(RIGHT_PADDLE_COOR)

ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(key="q", fun=left_paddle.go_up)
screen.onkey(key="a", fun=left_paddle.go_down)
screen.onkey(key="w", fun=right_paddle.go_up)
screen.onkey(key="s", fun=right_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball hits upper & lower wall
    if ball.ycor() < -360 or ball.ycor() > 360:
        ball.bounce_y()

    # Ball collides with either of the paddle
    if (ball.distance(right_paddle) < 35 and ball.xcor() > 400) or (
        ball.distance(left_paddle) < 35 and ball.xcor() < -400
    ):
        ball.bounce_x()

    # Ball missed by R paddle
    if ball.xcor() > 515:
        ball.reset_position()
        scoreboard.l_paddle_scores()

    # Ball missed by L paddle
    if ball.xcor() < -515:
        ball.reset_position()
        scoreboard.r_paddle_scores()

screen.exitonclick()
