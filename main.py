import sys
import random 
from card import Card
from deck import Deck 
from player import Player 

suits:list[str] =['Hearts','Diamond','Spade','Clubs']

ranks:list[str] =['2','3','4','5','6','7','8','9','10','K','Q','J','A'] 




deck=Deck(ranks,suits) 
player=Player("Karthick")
deck.shuffle()
#for _ in range(51):
 #   deck.deal()
for _ in range(2):
    player.request_card(deck)

player.print_hand()
print(player.calculate_score())
