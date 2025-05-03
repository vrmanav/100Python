from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=310)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
