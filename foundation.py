from card import Card
# This is the foundation class

'''
1. The foundation class takes in no object. 
2. At initialization the foundation class generate a list for each of the pile for the suits: ace_pile, heart_pile, c
lover_pile, diamond_pile
3. At initialization the foundation class generate a boolean flags too make sure that each pile is complete: 
ace_complete, heart_complete, clover_complete, diamond_complete
4. the class also have four functions to for each suit. These functions dictate when a card can and eill be added and 
when a stack os complete
it sets. the appropriate boolean flag to true.
'''


class Foundation(object):
    def __init__(self):
        self.heart_pile = []
        self.diamond_pile = []
        self.clover_pile = []
        self.spades_pile = []
        self.heart_complete = False
        self.diamond_complete = False
        self.clover_complete = False
        self.spades_complete = False

    '''
    The add_ace method operates when a card can and how it will be added to the heart_pile
    1. Checks if the heart_pile is already complete if it is print out statement to console
    2. Checks if the card is the appropriate suit: if not print out statement stating so 
    3. Checks if the pile is empty that the first card in the stack is an ace of the correct suit 
    4. Checks if that the cards are place in the correct order. 
    '''
    def add_heart(self, card_a):
        if self.heart_complete:
            print("The stack of aces are full")
        elif card_a.suit != 0:
            print("A card with an Heart Suit must be added to the Heart Stack")
        elif len(self.heart_pile) == 0:
            if card_a.rank != 0:
                print("First card in a suit pile must be an heart")
            else:
                self.heart_pile.append(card_a)
        else:
            if card_a.rank == (self.heart_pile[-1] + 1):
                self.heart_pile.append(card_a)
                print("Card " + card_a + " is added to the stack")
                if len(self.heart_pile) == 13:
                    self.heart_complete = True
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  -> "
                      " 5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")

    def heart_pop(self, pop):
        a_card = self.heart_pile.pop()
        self.heart_complete = False
        return a_card
    '''
    The add_diamond method operates when a card can and how it will be added to the diamond_pile
    1. Checks if the diamond_pile is already complete if it is print out statement to console
    2. Checks if the card is the appropriate suit: if not print out statement stating so 
    3. Checks if the pile is empty that the first card in the stack is an heart of the correct suit 
    4. Checks if that the cards are place in the correct order. 
    '''
    def add_diamond(self, card_d):
        if self.diamond_pile:
            print("The stack of diamonds are full")
        elif card_d.suit != 3:
            print("A card with an Diamond Suit must be added to the Diamond Stack")
        elif len(self.diamond_pile) == 0:
            if card_d.rank != 0:
                print("First card in a suit pile must be an diamond")
            else:
                self.diamond_pile.append(card_d)
        else:
            if card_d.rank == (self.diamond_pile[-1] + 1):
                self.diamond_pile.append(card_d)
                print("Card " + card_d + " is added to the stack")
                if len(self.diamond_pile) == 13:
                    self.diamond_complete = True
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  "
                      "5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")

    def diamond_pop(self, pop):
        a_card = self.diamond_pile.pop()
        self.diamond_complete = False
        return a_card

    '''
    The add_clover method operates when a card can and how it will be added to the clover_pile
    1. Checks if the clover_pile is already complete if it is print out statement to console
    2. Checks if the card is the appropriate suit: if not print out statement stating so 
    3. Checks if the pile is empty that the first card in the stack is an heart of the correct suit 
    4. Checks if that the cards are place in the correct order. 
    '''
    def add_clover(self, card_c):
        if self.clover_complete:
            print("The stack of clovers are full")
        elif card_c.suit != 2:
            print("A card with an Clover Suit must be added to the Clover Stack")
        elif len(self.clover_pile) == 0:
            if card_c.rank != 0:
                print("First card in a suit pile must be an clover")
            else:
                self.clover_pile.append(card_c)
        else:
            if card_c.rank == (self.clover_pile[-1] + 1):
                self.clover_pile.append(card_c)
                print("Card " + card_c + " is added to the stack")
                if len(self.clover_pile) == 13:
                    self.clover_complete = True
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  "
                      "5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")

    def clover_pop(self, pop):
        a_card = self.clover_pile.pop()
        self.clover_complete = False
        return a_card
    '''
   The add_diamond method operates when a card can and how it will be added to the spades_pile
   1. Checks if the spades_pile is already complete if it is print out statement to console
   2. Checks if the card is the appropriate suit: if not print out statement stating so 
   3. Checks if the pile is empty that the first card in the stack is an heart of the correct suit 
   4. Checks if that the cards are place in the correct order. 
   '''
    def add_spades(self, card_s):
        if self.spades_pile:
            print("The stack of diamonds are full")
        elif card_s.suit != 3:
            print("A card with an Spades Suit must be added to the Spades Stack")
        elif len(self.spades_pile) == 0:
            if card_s.rank != 0:
                print("First card in a suit pile must be an spade")
            else:
                self.spades_pile.append(card_s)
        else:
            if card_s.rank == (self.diamond_pile[-1] + 1):
                self.spades_pile.append(card_s)
                print("Card " + card_s + " is added to the stack")
                if len(self.spades_pile) == 13:
                    self.spades_complete = True
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  "
                      "5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")

    def spades_pop(self, pop):
        a_card = self.spades_pile.pop()
        self.spades_complete = False
        return a_card