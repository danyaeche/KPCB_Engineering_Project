from card import Card
import random

# This is the deck class
'''
The Deck class for the solitaire game 
The class take in no inputs for the constructor
At initialization, the class create a stack(list) to hold all the cards that will represent the deck
At initialization, iterate through all the possible types of card all 52 of them and add them to the list
At initialization, Shuffle the cards in the stack 
'''


class Deck(object):
    def __int__(self):
        self.stock = []
        for i in range(4):
            for j in range(13):
                c = Card(i, j)
                self.stock.append(c)

        self.stock = random.shuffle(self.stock)

    '''
    The method reveal the contents are the top card in the deck without removing it from the deck
    '''
    def reveal_top(self):
        if len(self.stock) == 0:
            print("There are no more cards in the stack")
            return None
        a_card = self.stock[len(self.stock) - 1]
        a_card.visible = True
        print(a_card)
        return None

    '''
    The method removed the top card from the deck 
    '''
    def pop(self):
        if len(self.stock) == 0:
            print("There are no more cards in the stack")
            return None
        a_card = self.stock.pop()
        a_card.visible = True
        print(a_card)
        return a_card

    '''
    The method removed the top card from the deck but face down so content of the card can't be seen 
    '''
    def pop_blind(self):
        if len(self.stock) == 0:
            print("There are no more cards in the stack")
            return None
        a_card = self.stock.pop()
        a_card.visible = False
        print(a_card)
        return a_card















