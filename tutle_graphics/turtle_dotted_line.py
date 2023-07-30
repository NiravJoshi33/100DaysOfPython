from turtle import Turtle, Screen

timmy = Turtle("turtle")
timmy.color("red","green")
length = 10

def dashed_line(instances, length1):
    for _ in range (instances):
        
        timmy.forward(length1)
        timmy.up()
        timmy.forward(length1)
        timmy.down()

for _ in range(4):
    dashed_line(10, length)
    timmy.left(90)
    

screen = Screen()
screen.exitonclick()
