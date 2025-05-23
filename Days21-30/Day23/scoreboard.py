from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-380, 350)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(font=FONT, align="left", arg=f"LEVEL: {self.level}")

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(font=FONT, align="center", arg="⚠️ GAME OVER ⚠️")
