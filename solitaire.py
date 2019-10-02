from deck import Deck
from card import Card
from foundation import Foundation
from tableau import Tableau

class Solitaire(object):
    def __init__(self):
        self.tableau = Tableau()
        self.deck = Deck()
        self.foundation = Foundation()

    

