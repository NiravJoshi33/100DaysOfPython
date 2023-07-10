#Welcome to Command Line Snake & Ladder Game
import random

#print ASCII art
print('''
         _                   .-=-.          .-==-.
        { }      __        .' O o '.       /  -<' )
        { }    .' O'.     / o .-. O \     /  .--v`
        { }   / .-. o\   /O  /   \  o\   /O /
         \ `-` /   \ O`-'o  /     \  O`-`o /
          `-.-`     '.____.'       `.____.
      ''')

P1_pos = 0 #Player 1 initial position is cell no. 0

while (P1_pos != 100 and P1_pos < 100):
    input("Please press 'Enter' to roll the dice")
    dice = random.randint(1,6)
    print("You rolled " + str(dice))
    P1_pos = P1_pos + dice
    if P1_pos == 4:
        P1_pos = 56
        print("Congratulations, Player 1 has climbed to cell no." + str(P1_pos))
    elif P1_pos == 12:
        P1_pos = 50
        print("Congratulations, Player 1 has climbed to cell no." + str(P1_pos))
    elif P1_pos == 14:
        P1_pos = 55
        print("Congratulations, Player 1 has climbed to cell no." + str(P1_pos))
    elif P1_pos == 22:
        P1_pos = 58
        print("Congratulations, Player 1 has climbed to cell no." + str(P1_pos))
    elif P1_pos == 41:
        P1_pos = 79
        print("Congratulations, Player 1 has climbed to cell no." + str(P1_pos))
    elif P1_pos == 54:
        P1_pos = 88
        print("Congratulations, Player 1 has climbed to cell no." + str(P1_pos))
    elif P1_pos == 28:
        P1_pos = 10
        print("Oh no, Player 1 climbed down to cell no." + str(P1_pos))
    elif P1_pos == 37:
        P1_pos = 3
        print("Oh no, Player 1 climbed down to cell no." + str(P1_pos))
    elif P1_pos == 47:
        P1_pos = 16
        print("Oh no, Player 1 climbed down to cell no." + str(P1_pos))
    elif P1_pos == 75:
        P1_pos = 32
        print("Oh no, Player 1 climbed down to cell no." + str(P1_pos))
    elif P1_pos == 94:
        P1_pos = 71
        print("Oh no, Player 1 climbed down to cell no." + str(P1_pos))
    elif P1_pos == 96:
        P1_pos = 42
        print("Oh no, Player 1 climbed down to cell no." + str(P1_pos))
    else:
        print("Player 1 has reached at cell no. " + str(P1_pos))
