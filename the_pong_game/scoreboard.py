from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.u_score = 0
        self.c_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.color("white")
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Computer Score = {self.c_score}  User Score = {self.u_score}", align="center", font=("Arial", 24, "normal"))

    def increase_user_score(self):
        self.u_score += 1
    
    def increase_computer_score(self):
        self.c_score += 1
    
    def gameover(self):
        self.home()
        self.write("Game Over", align="center", font=("Arial", 32, "normal"))