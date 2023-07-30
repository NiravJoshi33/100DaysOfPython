from turtle import Turtle, Screen
from random import choice
#import turtle_dotted_line

timmy = Turtle()
side = 100
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'purple']

def draw_shape(n1):
    for _ in range(n1):
        timmy.forward(side)
        #turtle_dotted_line.dashed_line(side,1)
        timmy.right(360/n1)

for n in range(3,11):
    timmy.color(choice(colors))
    draw_shape(n)

screen = Screen()
screen.exitonclick()