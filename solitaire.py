from deck import Deck
from card import Card
from foundation import Foundation
from tableau import Tableau

class Solitaire(object):
    def __init__(self):
        self.tableau = Tableau()
        self.deck = Deck()
        self.foundation = Foundation()
        self.game_won = False

    print("Hello, Welcome to Solitaire. This is a game you play by yourself and it's a lot of fun")

    print("Game Begin")

    while self.game_won == False:






