from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.u_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.color("red")
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level = {self.u_score}", align="center", font=("Arial", 24, "normal"))

    def increase_user_level(self):
        self.u_score += 1
    
    
    def gameover(self):
        self.home()
        self.write("Game Over", align="center", font=("Arial", 32, "normal"))