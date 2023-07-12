#Rock Paper Scissor

#import random module
import random

#Add ASCII hand signs

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

signs = [rock, paper, scissors]

u_choice = int(input("Please Enter 1 for Rock, 2 for Paper or 3 for Scissor: "))
c_choice = random.randint(1,3)

print(f"You have selected {u_choice}")
print(signs[u_choice - 1])
print(f"Computer has selected {c_choice}")
print(signs[c_choice - 1])

if u_choice > 3 or u_choice < 1:
    print("You have entered invalid value")
elif u_choice == c_choice:
    print("It's a draw")
elif u_choice == 1:
    if c_choice == 2:
        print("You lose!")
    else:
        print("You win!")
elif u_choice == 2:
    if c_choice == 1:
        print("You win!")
    else:
        print("You lose!")
else:
    if c_choice == 1:
        print("You lose!")
    else:
        print("You win")  