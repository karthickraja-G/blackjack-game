from deck import Deck

class Player:
    def __init__(self,name)->None:
        self.name=name
        self.hand=[]
    
    def require_card(self,deck:Deck)->None:
        self.hand.append(deck.deal())

    def print_hand(self)->None:
        for card in self.hand:
            print(card)
