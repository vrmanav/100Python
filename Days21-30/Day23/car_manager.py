import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            y_cor = random.randint(-380, 340)
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(380, y_cor)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
