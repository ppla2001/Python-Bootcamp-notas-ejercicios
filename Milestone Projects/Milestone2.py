import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#cree las cartas 
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}' 

#cree el mazo con las cartas 
class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return f'The deck has:{deck_comp}'
    def deal_cards(self):
        return self.all_cards.pop()

'''my_deck = Deck()
print(my_deck)
my_deck.shuffle_deck()
print(my_deck)
my_deck.deal_cards()
print(my_deck)'''

#cree lo que puede hacer el jugador sin tomar las apuestas
class Player():
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.value = 0 
        self.aces = 0
    def hit(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.values -= 10
            self.aces -= 1

#cree las apuestas
class Apuesta():
    def __init__(self,bet):
        self.total = 100
        self.bet = 0 
    def win_bet(self):
        self.total += self.bet * 2
    def lose_bet(self):
        self.total -= self.bet

#defino las funciones para poder hacer acciones 

#empezamos con las apuestas
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please provide your bet: '))
        except:
            print('Bet could not be accepted, try again!')
            continue
        else:
            if chips.bet > chips.total:
                print('Bet is bigger than balance. Pleas try again!')
            else:
                return 'Bet accepted! You are betting ${}'.format(chips.bet)

#pedir cartas 
def hit(deck,hand):
    hand.hit(deck.deal_cards())
    hand.adjust_ace()

# preguntar si pide o si se queda 
jugando = True
def hit_or_stand(deck,hand):
    global jugando
    while True:
        preguntar = input('Hit or Stand? Enter (H-S): ')
        if preguntar.lower().startswith('h'):
            hand.hit(deck.deal_cards())
        elif preguntar.lower().startswith('s'):
            print('Dealer is playing!')
            jugando = False
        else:
            print('Please try again!')
            continue
        break

#mostrar las cartas 
def show_some(player,dealer):
    player.cards

#para mostrar algunas cartas tengo q agarrar player y decir hand (tengo que mostrar las dos)
#mientras que para mostrar las cartas de dealer tengo que mostrar solo una y la otra no