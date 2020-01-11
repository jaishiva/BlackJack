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
 


class chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def ask_for_bet(chips):
    while True:
        try:
            bet = int(input('Enter your bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if bet > chips.total:
                print("Sorry, your bet shouldn't exceed",chips.total)
            else:
                return bet

def hit_or_stand():
    while True:
        player_input = input('Press "h" for hit "s" for stand ').lower()
        if player_input == 'h':
            return True
        elif player_input == 's':
            print("Dealer's turn ...hold on")
            return False
        else:
            print("Please enter a valid input, try again")


def show_all_cards(player,dealer):
    print("Dealer's cards =\n",*dealer.cards,sep='\n ')
    print("Dealer's Hand =\n",dealer.value)
    print("Player's cards =\n",*player.cards,sep='\n ')
    print("Player's Hand =\n",player.value)

def show_some_cards(player,dealer):
    print("Dealer's Hand :")
    print("Dealer's card =\n", dealer.cards[1])
    print("Player's Hand :")
    print("Player's cards =\n", *player.cards,sep='\n ')
    
def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")


def ask_for_ace_value():
    while True:
        try:
            ace_value = int(input('What value do you want to assign to Ace, enter 1 or 11 \n'))
        except:
            print('Sorry only 1 and 11 are allowed')
        else:
            if ace_value == 1 or ace_value == 11:
                return ace_value
            else:
                print('Sorry only 1 and 11 are allowed')
chips = chips()    
while True:
    print('Welcome to BlackJack - by Jai \n')
    values['Ace'] = ask_for_ace_value()
    deck = Deck()
    deck.shuffle()
    print(deck)

    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    
    chips.bet = ask_for_bet(chips)
    show_some_cards(player,dealer)
    print("Player's value ",player.value)
    print("Dealer's value ",dealer.value)
    while hit_or_stand():
        player.add_card(deck.deal())
        print(*player.cards)
        print("Player's value ",player.value)
        if player.value > 21:
            player_busts(chips)
            break
    if player.value <= 21:
        while dealer.value <17:
            dealer.add_card(deck.deal())

        if dealer.value >21:
            dealer_busts(chips)
        elif player.value > dealer.value:
            player_wins(chips)
        elif player.value < dealer.value:
            player_busts(chips)
        else:
            push()

    print("Player's Chips Stands at ", chips.total)
    
    play_again = input("Would you like to play again? Enter 'y' for yes , 'n'for no ").lower()

    if play_again != 'y':
        print("Thank you for Playing")
        break