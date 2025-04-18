from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Score()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.HEAD.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.HEAD.xcor() > 330
        or snake.HEAD.xcor() < -330
        or snake.HEAD.ycor() > 330
        or snake.HEAD.ycor() < -330
    ):
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.HEAD.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
