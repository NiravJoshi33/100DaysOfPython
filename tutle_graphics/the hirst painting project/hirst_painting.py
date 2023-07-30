import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('tutle_graphics/the hirst painting project/spot_art-reference.png', 20)
#print(colors[0].rgb)

rgb_colors = []
for color in colors:
    #rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    t = (r, g, b)
    rgb_colors.append(t)

#print(rgb_colors)

bob = Turtle()
screen = Screen()
screen.colormode(255) #default setting is 1.0 so it won't accept integer values for r,g & b so we need to set it to 255
bob.home()
bob.speed(0)
y = 0

for _ in range (10): # no. of columns
    for _ in range (10): # no. of rows
        bob.dot(15, random.choice(rgb_colors))
        bob.up()
        bob.forward(50)
        bob.down()
    y = y + 50 # once a row is completed, the turtle is offset by 10 points in y direction
    bob.up()
    bob.setposition(0,y)
    bob.down()
screen.exitonclick()