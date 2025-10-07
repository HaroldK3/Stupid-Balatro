# Stupid-Balatro
A dumbed down version of the game Balatro using Chase Robert's Deck of Cards API. https://deckofcardsapi.com/

## Description
Balatro is a rogue-like poker game where you have to beat blinds that may or may not have debuffs. My Balatro is a simplified version of that game, utilizing the scoring of the poker hands and the draw, shuffle, and pile API calls that the Deck of Cards API offers. While there are no jokers, planet cards, or tarot cards, this game functions exactly like Balatro does if you take all of that out. 

## Issues
-I really struggled setting up this repository to work with vs code. Never done that before.

-I kinda understood what was going on with the API calls, I get what they do and how they work, so that took me like an hour to fully get all of the methods I wanted for this project. All of the API work can be found in the Cards.py file. 

-The hand scoring threw me for a loop, because I didn't get how to check the higher cards like ace, king, queen, and jack, but then I realized I can just keep counting from 10 and treat it all like glorified math equations. 

-At this point, I have a pretty functional game of Dumb Balatro. It draws a hand of 8, lets you choose what to play, parses the hand into a hand name, and then it scores it. If you beat the round score, you move on, and if you don't, the game ends. I didn't think I would be here so soon. 

-Once I got all of the game functionality going, I realized I didn't have a way to shuffle the deck after I put the cards from the discard pile back, so that was weird. 

-Discarding also went wrong, because I forgot that the hand is my call and not the API's, so I had to go back and make sure it was updating the hand as well as discarding the cards from the deck to the discard pile. Shew.

-I hope to add the planet cards before the deadline. I have a way to keep track of the multiplier, though I may need to move that from Hand_Scoring to main if I'm gonna do planet cards. Honestly, I may can make a whole planet card file and put them there.  

## Final Comments
Now that this project is done, I understand the use of API calls and how they work. I really enjoyed making this game, and it was interesting enough to keep me entertained and focused while I was learning. The game challenged me to think outside of the box with my math to calculate the poker hands, and had me overthinking my loop variables by the end of it. Overall, I am proud of myself for getting this to work, and I hope I remember to keep working on it, utilizing my skills I'm learning in Server Side, in the near future.
