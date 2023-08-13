from turtle import Turtle
from ball import Ball

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)
        
    def create_paddle(self, x, y):
        self.shape("square")
        self.penup()
        self.color("orange")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def up(self):
        y1 = self.ycor()
        x1 = self.xcor()
        if y1<300:
            new_y = y1 + 30
            self.goto(x1, new_y)

    def down(self):
        y1 = self.ycor()
        x1 = self.xcor()
        if y1>-300:
            new_y = y1 - 30
            self.goto(x1, new_y)

    def move_AI(self, y_ball):
        x2 = self.xcor() 
        y2 = y_ball
        self.goto(x2, y2)     