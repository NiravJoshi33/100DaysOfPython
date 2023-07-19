import turtle

timmy = turtle.Turtle() # object "timmy" is created
print(timmy)
timmy.shape("turtle") # shape method is used on the timmy object
timmy.color('red', 'green') # color method is used and red & green are passed as parameters
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()