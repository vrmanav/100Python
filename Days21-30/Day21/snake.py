from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.HEAD = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            prev_segment_xcoor = self.segments[segment - 1].xcor()
            prev_segment_ycoor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(prev_segment_xcoor, prev_segment_ycoor)
        self.HEAD.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.HEAD.heading() != 270:
            self.HEAD.setheading(90)

    def move_down(self):
        if self.HEAD.heading() != 90:
            self.HEAD.setheading(270)

    def move_left(self):
        if self.HEAD.heading() != 0:
            self.HEAD.setheading(180)

    def move_right(self):
        if self.HEAD.heading() != 180:
            self.HEAD.setheading(0)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.HEAD = self.segments[0]
