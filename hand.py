from card import card
import random

class hand(object):
    def __int__(self):
        self.stock = []
        self.pointer = 0
        for i in range(4):
            for j in range(13):
                c = card(i,j)
                self.stock.append(c)

        self.stock = random.shuffle(self.stock)

    def reveal_top(self):
        a_card = self.stock[self.pointer]
        a_card.visible = True
        print(a_card)
        return a_card

    def pop(self):
        a_card = self.stock[self.pointer]
        print(a_card)
        self.pointer += 1
        return a_card















