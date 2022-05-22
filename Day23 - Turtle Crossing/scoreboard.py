from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def update_score(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(-100, 0)
        self.write("Game Over.", font=FONT)