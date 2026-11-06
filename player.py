from deck import Deck
from card import Card
class Player:
    def __init__(self,name)->None:
        self.name=name
        self.__hand=[]
    
    def request_card(self,deck:Deck)->None:
        self.__hand.append(deck.deal())

    def print_hand(self)->None:
        for card in self.card_in_hand():
            print(card)
    def card_in_hand(self)->list[Card]:
        return self.__hand.copy()

    def calculate_score(self)->int:
        total=0 
        for card in self.card_in_hand():
            if card.rank in ('K','J','Q'):
                total+=10 
            elif card.rank=='A':
                total+=11 
            else:
                total+=int(card.rank) 
        return total


