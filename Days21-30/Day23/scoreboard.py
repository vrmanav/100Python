from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-330, 350)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(font=FONT, align="center", arg=f"SCORE: {self.score}")
