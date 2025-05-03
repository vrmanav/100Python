from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

SCREEN_TOP = (0, 380)

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

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
