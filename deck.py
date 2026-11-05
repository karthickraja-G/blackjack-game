from card import Card
import random


class Deck:
    def __init__(self,ranks,suits)->None:
        self.ranks=ranks 
        self.suits=suits 
        self.cards=[]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank,suit)) 
    #def count_cards(self)->int:
     #   return len(self.cards)
    
   # def print_cards(self)->None:
    #    for card in self.cards:
     #       print(card)
    def shuffle(self)->None:
        random.shuffle(self.cards)
    
    def deal(self)->Card:
        if not self.cards:
            raise Exception("DECK IS EMPTY")
        return self.cards.pop()
