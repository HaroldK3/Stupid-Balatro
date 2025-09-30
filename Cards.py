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
    cards = ",".join(cards_played)

    url = f"https://deckofcardsapi.com/api/deck/{deck_id}pile/{pile_name}/add/?cards={cards}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data


def return_cards(deck_id, pile_name):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/return/"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data





def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


## Testing the code to make sure it works as we go

deck = shuffle_new_deck()

hand = draw_card(deck)

players_hand = [f"{card['value']} of {card['suit']}" for card in hand]

clear()

print(" | ".join(players_hand))
