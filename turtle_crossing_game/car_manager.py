from turtle import Turtle
from random import choice, randint
COLORS = ["red", "blue", "black", "brown", "yellow", "violet", "orange", "maroon"]
#NO_OF_CARS = 10
LANE_POSITIONS = [-200, -175, -150, -125, -100, -75, -50, -25, 0, 25, 50, 75, 100, 125, 150, 175, 200]
#X_POSITIONS = [0, 50, 150, 200, 250, 300]
CAR_STEP = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.goto(300, choice(LANE_POSITIONS))
        self.setheading(180)
        
    
    def move(self):
        new_x = self.xcor() - CAR_STEP
        self.goto(new_x, self.ycor())
    
    def start(self, list_of_cars):
        for name in list_of_cars:
            rand_x = 300
            rand_y = choice(LANE_POSITIONS)
            name.goto(rand_x, rand_y)
    
    def reset_car_pos(self):
        rand_x = 300
        rand_y = choice(LANE_POSITIONS)
        self.goto(rand_x, rand_y)