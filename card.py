'''

This is the card class for the solitaire game

'''

class card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.str_rank = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ']
        self.str_suit = ['A', 'D', 'C', 'S']
        self.visible = False

    def __str__(self):
        if self.visible:
            res = (self.str_rank[self.suit], self.str_rank[self.rank])
            print (res)
            return res
        else:
            res = "###"
            print (res)
            return res

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True




