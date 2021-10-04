import random

values = ['6','7','8','9','10','11','12','13','14']
suites = ['H', 'C', 'D', 'S']

deck = [v + s for s in suites for v in values]

random.shuffle(deck)
print(deck)


class Cards():
    def __init__(self) -> None:
        self.cards = deck
    
    def darigeba(self):
        self.playing_cards = self.cards[-12:]

        for card in self.playing_cards:
            self.cards.pop(self.cards.index(card))

        self.koziri = self.cards.pop()
        self.cards.append(self.koziri)
        print(self.koziri, len(self.cards))

    def amateba(self):
        self.playing_cards.append(self.cards.pop())
        print(self.playing_cards)

    def table_cards(self, card):
        self.table = []
        self.table.append(card)
        print(self.table)

    def shetenva(self):
        pass

    def card_gone(self):
        for card in self.playing_cards:
            self.cards.pop(self.cards.index(card))


cards = Cards()

cards.table_cards('7H')

class Player():
    def __init__(self, cards: list) -> None:
        self.cards = cards

    def svla(self):
        print(f'you have: {self.cards}')
        card = input("choose card: ")
        self.cards.pop(card)
    
    def shetenva(self, c):
        self.cards += c


class Computer():
    def __init__(self, cards: list) -> None:
        self.cards = cards

    def svla(self):

        self.cards.pop()

    