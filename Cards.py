import requests

def shuffle_new_deck():
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Deck successfully created.")
        print(data)
    else:
        print(f"Error making deck: {response.reason}")


