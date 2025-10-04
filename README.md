# Stupid-Balatro
A dumbed down version of the game Balatro using Chase Robert's Deck of Cards API. https://deckofcardsapi.com/

## Issues
-I really struggled setting up this repository to work with vs code. Never done that before.

-I kinda understood what was going on with the API calls, I get what they do and how they work, so that took me like an hour to fully get all of the methods I wanted for this project. All of the API work can be found in the Cards.py file. 

-The hand scoring threw me for a loop, because I didn't get how to check the higher cards like ace, king, queen, and jack, but then I realized I can just keep counting from 10 and treat it all like glorified math equations. 

-At this point, I have a pretty functional game of Dumb Balatro. It draws a hand of 8, lets you choose what to play, parses the hand into a hand name, and then it scores it. If you beat the round score, you move on, and if you don't, the game ends. I didn't think I would be here so soon. 

-Once I got all of the game functionality going, I realized I didn't have a way to shuffle the deck after I put the cards from the discard pile back, so that was weird. 

-I hope to add the planet cards before the deadline. I have a way to keep track of the multiplier, though I may need to move that from Hand_Scoring to main. 
