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
        round = 1
        score_goal = 300
        Cards.clear()
        done = False
        deck = Cards.shuffle_new_deck()

        while not done:
            hands = 4
            print(f"\n--- Round {round} ---")
            print(f"Score needed to win this round: {score_goal}")
            print(f"Total score: {score}")

            while hands > 0:
                ## Play
                print(f"\nHands left: {hands}")
                hand = Cards.draw_card(deck)
                print("\nYour hand:")
                for i, card in enumerate(hand, start=1):
                    print(f"{i}. {card['value']} of {card['suit']}")

                played_cards = Cards.select_card(hand, 5)

                ## Score
                played_hand_name = Hand_Scoring.find_hand(played_cards)
                points_scored = Hand_Scoring.score_hand(played_hand_name)
                score = score + points_scored

                print(f"You scored {points_scored} this round with a {played_hand_name}!")
                print(f"You now have a total of {score} points!")

                Cards.discard(deck, "Discard", played_cards)

                ## Round over?
                if score >= score_goal:
                    print(f"\nCongragulations, you beat round {round}!")
                    round += 1
                    score_goal = int(score_goal * 1.5)
                    Cards.return_cards(deck, "Discard")
                    break

                hands -= 1

            if score < score_goal:
                print(f"You didn't beat {score_goal}. Game over.")
                print(f"Final score: {score}")
                done = True
            else:
                cont = input("\nPlay next round? (y/n): ").lower()
                if cont != "y":
                    done = True
                


    elif user_input == 2:
        print("Bye bye!!")
        game_over = True

