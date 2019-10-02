# This is the card class

'''
This is the card class
1.Card class takes in suit(#0-3) and rank(#0-12) to the constructor
2. At initialization card class creates str_rank list and str_suit list as a mapping for suit and rank
for cards
3. At intilization the card class creates a is visible property set to False
4. Card class also has __str__() method to determine how it;s printed
5. Card class has method hide and show to set visibility
'''


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.str_suit = ['H', 'D', 'C', 'S']  # Heart==red Diamond==Red, Clover==Black, Spades==Black
        self.str_rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.visible = False

    '''
    __str__() method to show how the card is shown when printed to the console 
    '''
    def __str__(self):
        if self.visible:
            res = (self.str_suit[self.suit], self.str_rank[self.rank])
            print (res)
            return res
        else:
            res = "###"
            print (res)
            return res

    '''
    method the sets card.visible parameter to False 
    '''
    def hide(self):
        self.visible = False

    '''
    method the sets card.visible parameter to True  
    '''
    def show(self):
        self.visible = True




