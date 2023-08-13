from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.home()
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
    
    def bounce_y(self):
        self.y_move = self.y_move*-1
    
    def bounce_x(self):
        self.x_move = self.x_move*-1

    def reset_ball(self):
        self.home()
        self.bounce_x()