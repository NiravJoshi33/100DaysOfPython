from turtle import Turtle, Screen
import random as r

timmy = Turtle("turtle")
timmy.color("red","green")
# step = r.choice(0,101)
step = 100
angle = 90

for _ in range(4):
    timmy.forward(step)
    timmy.left(angle)



screen = Screen()
screen.exitonclick()