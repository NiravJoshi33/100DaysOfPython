from snake import Snake
from turtle import Screen
import time

snake = Snake()
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
    time.sleep(0.05)
    
    snake.move()
    












screen.exitonclick()