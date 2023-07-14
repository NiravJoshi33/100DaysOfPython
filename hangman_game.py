import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Generate a random word
word_list = ["ardvark", "baboon", "camel"]
#chosen_word = word_list[random.randint(0,len(word_list)-1)]
#Instead of using long function like above, we could use randomchoice function
chosen_word = random.choice(word_list)
#print(chosen_word)

lives = 6
print(f"You have {lives} lives")

#Create a list of as many blanks as characters in the chosen word 
display = []
for n in range(0,len(chosen_word)):
    display.append("_") 
print(display)

#Ask use to guess the character
end_of_game = False
while not end_of_game:
    guess = input("Please guess the character: ").lower()
    print(guess)
    a = 0
    #Check if the guessed character is in the word & Replace the display list in case the char matches
    for n in range(0,len(chosen_word)):
        if guess == chosen_word[n]:
            print("Chosen character exists in the word")
            display[n] = guess
            a = 1
        
    if a == 0:
        lives = lives - 1
        print(f"Oops! Now you have {lives} lives left")
        a = 1
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")
        #Join all the elements and print
        print(f"{''.join(display)}")
    
    if lives == 0:
        end_of_game = True
        print("You lost all the lives")
    
    print(stages[lives])
