from deck import Deck
from card import Card

# This is the Tableau class for the game

'''
The class Tableau
1.At initialization, it creates a seven list for the tableau 
2.At initialization, it creates a dictionary to keep track of the content for all the list 
3.At initialization, it ass the appopriate number of cards to each pile and has the last card be visible.
4.it has three method, one to check if the transaction between on pile to another is valid 
Another to remove a card from a pile and the card underneath becomes visible 
Another to add a card to a pile
'''


class Tableau(object):
    def __init__(self):
        self.pile_1 = []
        self.pile_2 = []
        self.pile_3 = []
        self.pile_4 = []
        self.pile_5 = []
        self.pile_6 = []
        self.pile_7 = []
        self.pile_dict = {1: self.pile_1, 2: self.pile_2, 3: self.pile_3, 4: self.pile_4, 5: self.pile_5,
                          6: self.pile_6, 7: self.pile_7}

        for i in range(1, 8):
            for j in range(i):
                self.pile_dict[i].append(Deck.pop_blind())
            self.pile_dict[i][-1].visible = True

    '''
    This is a method that check is a move of card from one pile of the tableau to another
    pile of the tableau is legal 
    '''
    def valid_transaction(self, from_pile_n, end_pile_n):
        if len(self.pile_dict[end_pile_n]) == 0:
            if self.pile_dict[from_pile_n][-1].rank == 12:
                return True
            else:
                return False
        elif self.pile_dict[from_pile_n][-1].suit < 2 and self.pile_dict[end_pile_n][-1] > 1:
            if self.pile_dict[from_pile_n][-1].rank == self.pile_dict[end_pile_n][-1].rank - 1:
                return True
        elif self.pile_dict[from_pile_n][-1].suit > 1 and self.pile_dict[end_pile_n][-1] < 2:
            if self.pile_dict[from_pile_n][-1].rank == self.pile_dict[end_pile_n][-1].rank - 1:
                return True
        else:
            return False

    '''
    This is a method to add a card to a pile 
    '''
    def add_card_pile(self, pile_number, c):
        c.visible = True
        self.pile_dict[pile_number].append(c)

    '''
    This is method to remove a card from a pile 
    '''
    def remove_card_pile(self, pile_number):
        if len(self.pile_dict) == 0:
            print("The pile is empty, no card can be removed from it")
            return None
        a_card = self.pile_dict[pile_number].pop()
        self.pile_dict[pile_number][-1].visible = True
        return a_card
