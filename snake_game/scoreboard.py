from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
    
    def gameover(self):
        self.home()
        self.write("Game Over", align="center", font=("Arial", 32, "normal"))