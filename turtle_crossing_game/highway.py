from turtle import Turtle
from car_manager import LANE_POSITIONS
LINE_LENGTH = 10
GAP = 10
HIGHWAY_POS = []
for pos in LANE_POSITIONS:
    lane_pos = pos - 37.5
    HIGHWAY_POS.append(lane_pos)
lane_pos = LANE_POSITIONS[-1] + 37.5
HIGHWAY_POS.append(lane_pos)
lane_pos = LANE_POSITIONS[-2] + 37.5
HIGHWAY_POS.append(lane_pos)
lane_pos = LANE_POSITIONS[-3] + 37.5
HIGHWAY_POS.append(lane_pos)
    
        
print(HIGHWAY_POS)

class Highway(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.hideturtle()
        self.penup()

    def draw_dotted_line(self):
        self.pendown()
        self.forward(LINE_LENGTH)
        self.penup()
        self.forward(GAP)

    def draw_highway(self):
        for pos in HIGHWAY_POS:
            self.goto(-300, pos)
            while self.xcor() < 300:
                self.draw_dotted_line()
                self.penup()

