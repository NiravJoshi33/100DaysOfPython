from turtle import Turtle
STARTING_POSITION = (0, -280)
X_STEP = 20
Y_STEP = 20

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def up(self):
        x = self.xcor()
        y = self.ycor()
        new_y = y + Y_STEP
        self.goto(x, new_y)
    
    def left(self):
        x = self.xcor()
        new_x = x - X_STEP
        y = self.ycor()
        self.goto(new_x, y)
    
    def right(self):
        x = self.xcor()
        new_x = x + X_STEP
        y = self.ycor()
        self.goto(new_x, y)
    
    def reset_pos(self):
        self.goto(STARTING_POSITION)
    