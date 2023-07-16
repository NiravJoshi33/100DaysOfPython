#Blackjack Game

import random

#Rules:
#Two players in a game: dealer and you
#First two cards are dealt to you and dealer. You can see both of your cards and only one of the dealer's cards
#The goal is to have cards with the values totaling closest to 21 but not more than 21
#After seeing the cards, player can decide whether to get a new card or see the result with the existing cards
#Dealer has to take new card of the total of their card is <17
#Jack, Queen and King are considered to have value of 10
#Ace "A" can have either 1 or 11 value. Owner of the card can decide the value

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = [random.choice(cards), random.choice(cards)]
user_total = sum(user_cards)
print(f"Total of player's cards is: {user_total}")
#print(user_cards)
dealer_cards = [random.choice(cards), random.choice(cards)]
print(f"One of the dealer's cards: {dealer_cards[0]}")
dealer_total = sum(dealer_cards)
while dealer_total < 17:
    new_card = random.choice(cards)
    dealer_cards.append(new_card)
    dealer_total = sum(dealer_cards)
    #print(dealer_cards)
    #print(dealer_total)
#print(dealer_cards)
gameover = False
while not gameover:
    draw = input("Do you want to draw another card: Y/N?")
    #print(draw)
    if draw == "Y":
        new_card = random.choice(cards)
        user_cards.append(new_card)
        print(user_cards)
        user_total = sum(user_cards)
        print(f"New the total of the user's cards is: {user_total}")
        if user_total > 21:
            gameover = True
            print(f"Total of your cards is {user_total} which is above 21 so you lose")
    elif draw == "N":
        if user_total == 21:
            gameover = True
            #print("Blackjack")
            print("You won!")
        if user_total < 21:
            if dealer_total == 21:
                gameover = True
                print("You lose")
            if dealer_total > 21:
                gameover = True
                print("You win")
            if dealer_total < 21:
                if dealer_total > user_total:
                    gameover = True
                    print("You lose")
                elif dealer_total == user_total:
                    gameover = True
                    print("It's a draw")
                else:
                    gameover = True
                    print("You win")

print(f"User's Cards: {user_cards}")
print(f"User's total: {user_total}")
print(f"Dealer's cards: {dealer_cards}")
print(f"Dealer's total: {dealer_total}")

