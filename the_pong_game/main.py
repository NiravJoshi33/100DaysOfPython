#Breaking down problem into pieces
#Display screen, a divider and score board
#Make ball. This will be a separate class. 
#Make ball bounce from the horizontal wall and detect collision with the vertical wall 
#Make player paddles - this will also be a separate class
#Move paddle as per the keyboard input
#Detect collision with the paddles

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.tracer(0)
user_paddle = Paddle(350, 0)
computer_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
time_delay = 0.05
screen.update()



game_is_on = True
screen.listen()



while game_is_on:
    screen.update()
    ball.move()
    time.sleep(time_delay)

    screen.onkey(key="Up", fun=user_paddle.up)
    screen.onkey(key="Down", fun=user_paddle.down)
    screen.onkey(key="w", fun=computer_paddle.up)
    screen.onkey(key="s", fun=computer_paddle.down)
    #computer_paddle.move_AI(ball.ycor()) #Impossible/Arcade mode enabled :)
    screen.update()

    #Detect collision with top and bottom wall
    #print(ball.ycor())
    if ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()

    print(f"X coordinate of ball: {ball.xcor()}")
    #Detect collision with the paddle
    if ball.xcor() > 330 and ball.distance(user_paddle) < 50:
        ball.bounce_x()
        time_delay *= 0.9
    elif ball.xcor() < -330 and ball.distance(computer_paddle) < 50:
        ball.bounce_x()
    #Detect when user paddle missed the ball    
    elif ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.increase_computer_score()
        scoreboard.update_scoreboard()
        screen.update()
    #Detect when computer paddle missed the ball
    elif ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.increase_user_score()
        scoreboard.update_scoreboard()
        screen.update()
    elif scoreboard.u_score > 10 or scoreboard.c_score > 10:
        game_is_on = False
        scoreboard.gameover()

screen.exitonclick()