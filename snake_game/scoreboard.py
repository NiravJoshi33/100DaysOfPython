from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/home/nirav/OneDrive/CS/Python/100DaysOfPython/snake_game/my_file.txt","r") as file:
                self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
    
    def reset_score(self):
        if self.score > self.highscore:
            with open("/home/nirav/OneDrive/CS/Python/100DaysOfPython/snake_game/my_file.txt","w") as file:
                file.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    # def gameover(self):
    #     self.home()
    #     self.write("Game Over", align="center", font=("Arial", 32, "normal"))