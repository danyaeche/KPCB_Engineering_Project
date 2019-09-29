from hand import hand
from card import card


class tableau(object):
    def __init__(self):
        self.pile_1 = []
        self.pile_2 = []
        self.pile_3 = []
        self.pile_4 = []
        self.pile_5 = []
        self.pile_6 = []
        self.pile_7 = []
        self.pile_dict = {1:self.pile_1, 2:self.pile_2, 3:self.pile_3, 4:self.pile_4, 5:self.pile_5, 6:self.pile_6, 7:self.pile_7}

    def add_pile_1(self, input_card_list):
        for x in input_card_list:
            self.pile_dict[1].append(x)

        self.pile_dict[1][-1].visble == True
        print(self.pile_dict[1])

    def add_pile_2(self, input_card_list):
        for x in input_card_list:
            self.pile_dict[2].append(x)

        self.pile_dict[1][-1].visble == True
        print(self.pile_dict[1])

    def add_pile_3(self, input_card_list):
        for x in input_card_list:
            self.pile_dict[3].append(x)

        self.pile_dict[1][-1].visble == True
        print(self.pile_dict[1])

    def add_pile_4(self, input_card_list):
        for x in input_card_list:
            self.pile_dict[1].append(x)

        self.pile_dict[1][-1].visble == True
        print(self.pile_dict[1])

    def add_pile_5(self, input_card_list):
        for x in input_card_list:
            self.pile_dict[1].append(x)

        self.pile_dict[1][-1].visble == True
        print(self.pile_dict[1])

    def add_pile_6(self, input_card_list):
        for x in input_card_list:
            self.pile_dict[1].append(x)

        self.pile_dict[1][-1].visble == True
        print(self.pile_dict[1])

    def add_pile_7(self, input_card_list):
        for x in input_card_list:
            self.pile_dict[1].append(x)

        self.pile_dict[1][-1].visble == True
        print(self.pile_dict[1])

    def valid_transaction(self,from_pile_n, end_pile_n):
        if hand.self_pile[from_pile_n].suit < 3 and self.pile_dict[end_pile_n] > 2:
            return True
        elif hand.self_pile[end_pile_n].suit < 3 and self.pile_dict[from_pile_n] > 2:
            return True
        else:
            return False

    def add_card_pile(self,pile_number, c):
        c.visble
        hand.pile_dict[pile_number].append(c)

    def remove_card_pile(self, pile_number):
        a_card = hand.pile_dict[pile_number][-1]
        hand.pile_dict[pile_number] = hand.pile_dict[pile_number][:-1]
        hand.pile_dict[pile_number][-1].visible
        return a_card







