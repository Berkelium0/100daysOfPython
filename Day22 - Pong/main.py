from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if l_paddle.distance(ball) < 50 and ball.xcor() > 320 or r_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.restart()

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.restart()

screen.exitonclick()
