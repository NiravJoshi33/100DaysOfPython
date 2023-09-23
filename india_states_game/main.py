import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('India States Game')
image = 'india_states_game/India_map.gif'
screen.addshape(image)
#screen.setup(width=600, height=600)
turtle.shape(image)

data = pd.read_csv('india_states_game/indian_states_coordinates.csv')
states = data['State'].to_list()

#print(data[data['State'] == "Gujarat"]['X'])
correct_states = []

while len(correct_states) < 28:
    user_answer = screen.textinput(title='Guess the state name', prompt='Enter the name of state:').title()
    print(user_answer)
    
    if user_answer == 'Exit':
        break
    elif user_answer in correct_states:
        pass
    elif user_answer in states:
        correct_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_state = int(data[data['State'] == user_answer]['X'])
        print(f'x coordinate is {x_state}')
        y_state = int(data[data['State'] == user_answer]['Y'])
        print(f'y coordinate is {y_state}')
        t.goto(x_state, y_state)
        t.write(user_answer)

states_to_learn = []
for state in states:
    if state not in correct_states:
        states_to_learn.append(state)

pd.DataFrame(states_to_learn).to_csv('india_states_game/States_to_learn.csv')
#print(data)



screen.exitonclick()