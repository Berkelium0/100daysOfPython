# import colorgram
#
# colors = colorgram.extract('hirst_color_template.jpg', 30)
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_list.append((r, g, b))
#
# print(rgb_list)
from turtle import Turtle, Screen, colormode
import random

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
              (46, 73, 62), (47, 66, 82)]


tim = Turtle()
tim.penup()
tim.hideturtle()
colormode(255)
tim.goto(-300, -250)
tim.speed(0)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.goto(-300, tim.ycor() + 50)

s = Screen()
s.exitonclick()
