import Cards
import requests
import os
from collections import Counter

card_values = {
    "ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

high_card_multi = 1
pair_multi = 2
two_pair_multi = 2
three_of_kind_multi = 3
straight_multi = 4
flush_multi = 4
full_house_multi = 4
four_of_kind_multi = 7
straight_flush_multi = 8


def find_hand(cards_picked):
    if not cards_picked:
        return "No cards"

    values = sorted([card_values[card["value"]] for card in cards_picked], reverse=True)
    value_counts = Counter(values)

    suits = [card["suit"] for card in cards_picked]
    suit_counts = Counter(suits)

    flush = len(suit_counts) == 1
    straight = (
                len(values) == 5 and 
                max(values) - min(values) == 4 and
                len(set(values)) == 5
               )
    
    if set(values) == {14, 2, 3, 4, 5}:
        straight = True
    
    if straight and flush:
        return "Straight Flush"
    elif 4 in value_counts.values():
        return "Four of a Kind"
    elif sorted(value_counts.values()) == [2, 3]:
        return "Full House"
    elif flush:
        return "Flush"
    elif straight:
        return "Straight"
    elif 3 in value_counts.values():
        return "Three of a Kind"
    elif list(value_counts.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in value_counts.values():
        return "Pair"
    elif len(values) > 0:
        return "High Card"
    else:
        return "No scorable hand."

    

def score_hand(hand_name):

    if hand_name == "High Card":
        return 5 * high_card_multi
    elif hand_name == "Pair":
        return 10 * pair_multi
    elif hand_name == "Two Pair":
        return 20 * two_pair_multi
    elif hand_name == "Three of a Kind":
        return 30 * three_of_kind_multi
    elif hand_name == "Straight":
        return 30 * straight_multi
    elif hand_name == "Flush":
        return 35 * flush_multi
    elif hand_name == "Full House":
        return 40 * full_house_multi
    elif hand_name == "Four of a Kind":
        return 60 * four_of_kind_multi
    elif hand_name == "Straight Flush":
        return 100 * straight_flush_multi

    