from turtle import Turtle, Screen
from random import choice, randint

jerry = Turtle()
screen = Screen()
screen.colormode(255) #default setting is 1.0 so it won't accept integer values for r,g & b so we need to set it to 255
jerry.home()
jerry.speed(0)
jerry.width(2)
orientation = 0
radius = 150

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, b, g)

for orientation in range(0,360, 5):
    jerry.color(random_color())
    jerry.setheading(orientation)
    jerry.circle(radius)

screen.exitonclick()