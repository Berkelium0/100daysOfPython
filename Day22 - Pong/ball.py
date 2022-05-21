from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.1
        self.x_direction = 10
        self.y_direction = 10
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.x_direction, self.ycor() + self.y_direction)

    def bounce_y(self):
        self.y_direction = -self.y_direction

    def bounce_x(self):
        self.x_direction = -self.x_direction
        self.move_speed *= 0.9

    def restart(self):
        self.bounce_x()
        self.move_speed = 0.1
        self.goto(0, 0)
