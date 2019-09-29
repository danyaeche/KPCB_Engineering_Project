from card import  card

class foundation(object):
    def __init__(self):
        ace_pile = []
        heart_pile = []
        clover_pile = []
        diamond_pile = []
        ace_complete = False
        heart_complete = False
        clover_complete = False
        diamond_complete = False

    def add_ace(self, c):
        if c.suit != 0:
            print("A card with an Ace Suit must be added to the ace stack")
        if len(self.ace_pile) == 0:
            if c.rank != 0:
                print("First card in a suit pile must be an ace")
            else:
                self.ace_pile.append(c)
        else:
            if c.rank == (self.ace_pile[-1] + 1):
                self.ace_pile.append(c)
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")


    def add_heart(self,c):
        if c.suit != 0:
            print("A card with an Heart Suit must be added to the Heart stack")
        if len(self.heart_pile) == 0:
            if c.rank != 0:
                print("First card in a suit pile must be an heart")
            else:
                self.heart_pile.append(c)
        else:
            if c.rank == (self.ace_pile[-1] + 1):
                self.heart_pile.append(c)
            else:
                print("the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")


    def add_clover(self, c):
        if c.suit != 0:
            print("A card with an Clover Suit must be added to the clover stack")
        if len(self.clover.pile) == 0:
            if c.rank != 0:
                print("First card in a suit pile must be an clover")
            else:
                self.clover.pile.append(c)
        else:
            if c.rank == (self.clover.pile[-1] + 1):
                self.clover.pile.append(c)
            else:
                print(
                    "the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")

    def add_diamond(self,c):
        if c.suit != 0:
            print("A card with an Diamond Suit must be added to the clover stack")
        if len(self.diamond.pile) == 0:
            if c.rank != 0:
                print("First card in a suit pile must be an diamond")
            else:
                self.diamond.pile.append(c)
        else:
            if c.rank == (self.diamond.pile.pile[-1] + 1):
                self.diamond.pilee.append(c)
            else:
                print(
                    "the pile must be stack in the correct order -->  A ->  2  -> 3  ->  4  ->  5  ->  6  -> 7 -> 8 ->  9 ->  10 ->  J -> Q  -> K")




