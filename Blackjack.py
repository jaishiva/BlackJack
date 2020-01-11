import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':1}


class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.suit + ' of ' + self.rank

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))
    
    def __str__(self):
        deck_cards = ''
        for card in self.deck:
            deck_cards  = deck_cards + card.__str__() +'\n'
        return deck_cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.single_card = self.deck.pop()
        return self.single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.aces = 0
        self.value = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_aces(self):
        pass


class chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


while True:
    print('Welcome to BlackJack - by Jai')
    print(f"Value of Ace is {values['Ace']}")
    deck = Deck()
    deck.shuffle()
    print(deck)
    player = Hand()
    hand = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    hand.add_card(deck.deal())
    hand.add_card(deck.deal())
    # while play:
    break
