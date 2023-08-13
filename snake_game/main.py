from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #turns turtle animation off

game_is_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        snake.grow_snake()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()



    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg.position())<15:
            scoreboard.reset_score()
            snake.reset_snake() 







screen.exitonclick()