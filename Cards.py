import requests
import os

def shuffle_new_deck():
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        deck_id = data["deck_id"]
        print("Deck successfully created.")
        print(data)
    else:
        print(f"Error making deck: {response.reason}")
    
    return deck_id


def draw_card(deck_id):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=8"
    response = requests.get(url)
    response.raise_for_status()

    cards = response.json() ["cards"]

    return cards


def discard(deck_id, pile_name, cards_played):
    card_codes = [card["code"] for card in cards_played]
    cards = ",".join(card_codes)

    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/add/?cards={cards}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(f"Added {cards_played} to {pile_name}")
    
    return data


def return_cards(deck_id, pile_name):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/return/"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data

def select_card(hand, max_cards=5):
    while True:
        print("\nSelect up to 5 cards to play: ")
        choice = input().strip()
        try:
            nums = list(map(int, choice.split()))
            if 1 <= len(nums) <= max_cards and all(1 <= i <= len(hand) for i in nums):
                return [hand[i-1] for i in nums]
            else: 
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")



def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
