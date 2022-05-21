from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.speed(0)
        self.penup()
        self.setheading(90)
        self.goto(pos)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)
