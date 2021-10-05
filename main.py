from app import Cards, Computer, Player, Table


def duraka():
    cards = Cards()
    table_cards = Table()
    first_deal = cards.dealing()
    print(first_deal)
    player = Player(first_deal[:6])
    computer = Computer(first_deal[6:])
    trump = cards.trump()

duraka()


