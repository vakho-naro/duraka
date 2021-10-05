import random

values = ['6', '7', '8', '9', '10', '11', '12', '13', '14']
suites = ['H', 'C', 'D', 'S']

deck = [v + s for s in suites for v in values]

random.shuffle(deck)


class Cards:
    def __init__(self) -> None:
        self.cards = deck
    
    def dealing(self):
        self.playing_cards = self.cards[-12:]
        for card in self.playing_cards:
            self.cards.pop(self.cards.index(card))
        return self.playing_cards

    def trump(self):
        self.trump = self.cards.pop()
        self.cards.insert(0, self.trump)
        print(f'trump card is {self.trump}')
        return self.trump[-1]

    def add_card(self):
        self.playing_cards.append(self.cards.pop())
        print(self.playing_cards)


cards = Cards()


class Table:
    def __init__(self):
        self.table = []

    def table_cards(self, card):
        self.table.append(card)
        print(self.table)

    def pick_up(self):
        self.table = []

    def card_gone(self):
        for card in self.table:
            self.playing_cards.pop(self.playing_cards.index(card))
        self.table = []


class Player:
    def __init__(self, c: list) -> None:
        self.cards = c
        print(self.cards)

    def turn(self):
        print(f'you have: {self.cards}')
        card = input("choose card: ")
        self.cards.remove(card)
    
    def pick_up(self, c):
        self.cards += c


class Computer:
    def __init__(self, c: list) -> None:
        self.cards = c
        print(self.cards)

    def turn(self):

        self.cards.pop()
