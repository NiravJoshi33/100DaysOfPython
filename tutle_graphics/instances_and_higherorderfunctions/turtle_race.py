from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["Jim", "Bob", "Timmy", "James", "Jack", "Rob"]

if bet:
    is_race_on = True


i = 0
y = -100
for player in turtles:
    turtles[i] = Turtle('turtle')
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-240, y)
    i = i + 1
    y = y + 50

while is_race_on:
    for player in turtles:
        rand_distance = randint(0,10)
        player.forward(rand_distance)
        if player.xcor() > 230:
            print(f"{player} has won")
            print(f"The color of the winner turtle is {player.pencolor()}")
            winner = player
            is_race_on = False

print(f"Your bet was on {bet}")
print(f"color of the winner turtle is {winner.pencolor()}")

if bet == winner.pencolor():
    print("You have won!")
else:
    print("You lost")

screen.exitonclick()