import Cards
import requests
import os
from collections import Counter

card_values = {
    "ACE": 14 or 2, "KING": 13, "QUEEN": 12, "JACK": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}


def scoring_hand(cards_picked):
    values = sorted([card_values[card["value"]] for card in cards_picked], reverse=True)
    value_counts = Counter(values)

    suits = [card["suit"] for card in cards_picked]
    suit_counts = Counter(suits)

    