import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    car_manager.spawn_car()
    car_manager.move_cars()
    time.sleep(0.1)

    if player.ycor() > 280:
        player.level_up()
        car_manager.level_up()
        scoreboard.update_score()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    screen.update()

screen.exitonclick()
