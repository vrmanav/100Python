from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_len=1, stretch_wid=7)

    def go_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)
