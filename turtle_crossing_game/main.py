from turtle import Screen, Turtle
from player import Player
from car_manager import Car
from highway import Highway
import time
from scoreboard import Scoreboard

finish_line = 250
next_car_const = 10
t = 0.05
highway = Turtle()
scoreboard = Scoreboard()
scoreboard.u_score = 0
#NO_OF_CARS = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#Draw highway lanes
highway = Highway()
highway.draw_highway()
#print("highway is drawn")
screen.update()
car_list = []
# for i in range(NO_OF_CARS):
#     new_car = "car" + str(i)
#     new_car = Car()
#     #new_car.reset_car_pos()
#     car_list.append(new_car)
#print("Car list is created")
player = Player()
#car = Car()
game_is_on = True
screen.listen()
#screen.onclick(fun=car.start(car_list))
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Left", fun=player.left)
screen.onkey(key="Right", fun=player.right)
#print("Stage is initiated")
screen.update()

a = 0
while game_is_on:
    screen.update()
    #print("Entered while loop")
    for vehicle in car_list:
        #print("Entered for loop")
        vehicle.move()
        if vehicle.xcor() < -300:
            vehicle.reset_car_pos()
        #Detect if turtle collides with the car
        if player.distance(vehicle) < 20:
            game_is_on = False
            scoreboard.gameover()
    
    if player.ycor() > finish_line:
        scoreboard.increase_user_level()
        scoreboard.update_scoreboard()
        player.reset_pos()
        next_car_const = next_car_const - 1
        t = t*0.9

    
    time.sleep(t)
    a = a + 1

    if a == next_car_const:
        new_car = Car()
        car_list.append(new_car)
        a = 0

screen.exitonclick()
