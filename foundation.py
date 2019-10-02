from card import card

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
        self.ace_pile = []
        self.heart_pile = []
        self.clover_pile = []
        self.diamond_pile = []
        self.ace_complete = False
        self.heart_complete = False
        self.clover_complete = False
        self.diamond_complete = False

    '''
    The add_ace method operates when a card can and how it will be added to the ace_pile
    1. Checks if the ace_pile is already complete if it is print out statement to console
    2. Checks if the card is the appropriate suit: if not print out statement stating so 
    3. Checks if the pile is empty that the first card in the stack is an ace of the correct suit 
    4. Checks if that the cards are place in the correct order. 
    '''
    def add_ace(self, card_a):
        if self.ace_complete:
            print("The stack of aces are full")
        elif card_a.suit != 0:
            print("A card with an Ace Suit must be added to the Ace Stack")
        elif len(self.ace_pile) == 0:
            if card_a.rank != 0:
                print("First card in a suit pile must be an ace")
            else:
                self.ace_pile.append(card_a)
        else:
            if card_a.rank == (self.ace_pile[-1] + 1):
                self.ace_pile.append(card_a)
                print("Card " + card_a + " is added to the stack")
                if len(self.ace_pile) == 13:
                    self.ace_complete = True
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  -> "
                      " 5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")

    '''
    The add_heart method operates when a card can and how it will be added to the heart_pile
    1. Checks if the heart_pile is already complete if it is print out statement to console
    2. Checks if the card is the appropriate suit: if not print out statement stating so 
    3. Checks if the pile is empty that the first card in the stack is an heart of the correct suit 
    4. Checks if that the cards are place in the correct order. 
    '''
    def add_heart(self, card_h):
        if self.heart_complete:
            print("The stack of hearts are full")
        elif card_h.suit != 1:
            print("A card with an Heart Suit must be added to the Heart Stack")
        elif len(self.heart_pile) == 0:
            if card_h.rank != 0:
                print("First card in a suit pile must be an heart")
            else:
                self.heart_pile.append(card_h)
        else:
            if card_h.rank == (self.ace_pile[-1] + 1):
                self.heart_pile.append(card_h)
                print("Card " + card_h + " is added to the stack")
                if len(self.heart_pile) == 13:
                    self.heart_complete = True
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  5  "
                      "->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")

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