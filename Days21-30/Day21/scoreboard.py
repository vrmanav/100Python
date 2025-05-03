from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=310)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", mode="r") as file:
            high_score = file.read()
            self.write(
                arg=f"Score: {self.score} High Score: {high_score}",
                align=ALIGNMENT,
                font=FONT,
            )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
