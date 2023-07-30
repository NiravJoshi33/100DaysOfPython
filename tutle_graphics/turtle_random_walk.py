from turtle import Turtle, Screen
from random import choice, randint, random

tom = Turtle()
screen = Screen()
screen.colormode(255) #default setting is 1.0 so it won't accept integer values for r,g & b so we need to set it to 255
steps = 15 # length of one step line
instances = 500 # Set how many times the loops needs to run
#colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'purple', 'CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat', 'SlateGray', 'SeaGreen']
tom.pensize(3)
tom.speed(0)
directions = [0, 90, 180, 270, -90, -180, -270]

for _ in range (instances):
    #tom.color(choice(colors)) # select random color from the "colors" list
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    #print(f"r = {r}, g = {g}, b = {b}")
    tom.color(r, g, b)
    tom.forward(steps)
    #tom.left(randint(-180, 180))
    #tom.setheading(choice(directions))
    tom.left(choice(directions))


screen.exitonclick()

