from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.title("Road Cross game")
screen.setup(width=800, height=800)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

screen.exitonclick()
