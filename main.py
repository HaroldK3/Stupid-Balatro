import Cards
import Hand_Scoring
import requests
import os

game_over = False

while not game_over:
    print("--- Welcome to the Stupid Balatro! ---")
    print("1. Start new game")
    print("2. Exit program")

    user_input = int(input())

    if user_input == 1:
        score = 0
        Cards.clear()
        done = False
        deck = Cards.shuffle_new_deck()

        while not done:
            hand = Cards.draw_card(deck)
            played_cards = Cards.select_card(hand)
            score = score + Hand_Scoring.scoring_hand(played_cards)



    elif user_input == 2:
        print("Bye bye!!")
        game_over = True

