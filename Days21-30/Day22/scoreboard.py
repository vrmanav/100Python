from turtle import Turtle

FONT = ("Courier", 65, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-120, 305)
        self.write(arg=f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(120, 305)
        self.write(arg=f"{self.r_score}", align=ALIGN, font=FONT)

    def l_paddle_scores(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_paddle_scores(self):
        self.r_score += 1
        self.update_scoreboard()