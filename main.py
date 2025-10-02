import Cards
import requests
import os

game_over = False

while not game_over:
    print("--- Welcome to the Stupid Balatro! ---")
    print("1. Start new game")
    print("2. Exit program")

    user_input = int(input())

    if user_input == 1:
        Cards.clear()
        done = False
        deck = Cards.shuffle_new_deck()

        while not done:
            hand = Cards.draw_card(deck)
            Cards.select_card(hand)



    elif user_input == 2:
        print("Bye bye!!")
        game_over = True

